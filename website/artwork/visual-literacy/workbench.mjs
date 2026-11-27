import {buildGraph,composePrompt,makeAnalysisPrompt,validateAnalysis,normalize} from "./graph-core.mjs";
const $=id=>document.getElementById(id), el=(tag,text,cls)=>{const x=document.createElement(tag);if(text!==undefined)x.textContent=text;if(cls)x.className=cls;return x;};
const read=async path=>{const r=await fetch(path);if(!r.ok)throw Error(path+" HTTP "+r.status);return r.json();};
const button=(label,fn)=>{const b=el("button",label);b.type="button";b.addEventListener("click",fn);return b;};
const link=(label,href)=>{const a=el("a",label);a.href=href;return a;};
const picture=(p)=>{const im=el("img");im.src=p.thumb||p.src;im.alt=p.label||"Course illustration";im.loading="lazy";return im;};
const copy=async text=>{try{await navigator.clipboard.writeText(text);}catch{const t=el("textarea");t.value=text;document.body.append(t);t.select();document.execCommand("copy");t.remove();}};
let graph,byId,selection=new Map(),limit=36,uploaded=null,quizIndex=0,score=0,answered=0;
function renderCatalog(){
  const q=normalize($("searchConcept").value),course=$("courseFilter").value,layer=$("layerFilter").value;
  const list=graph.nodes.filter(n=>(!course||n.course===course)&&(!layer||String(n.layer)===layer)&&(!q||normalize([n.name,n.definition,n.lesson,n.classes?.join(" ")].join(" ")).includes(q)));
  $("resultCount").textContent=list.length+" concepts and examples";
  $("catalog").replaceChildren(...list.slice(0,limit).map(n=>{
    const card=el("article",undefined,"work-card");if(n.images?.length)card.append(picture(n.images[0]));
    card.append(el("h3",n.name),el("small",n.course+" · "+n.type+" · L"+n.layer),button("Explore",()=>showDetail(n.id)),button(selection.has(n.id)?"Remove":"Add to prompt",()=>toggle(n)));return card;
  }));$("more").hidden=list.length<=limit;
}
function showDetail(id){
  const n=byId.get(id);if(!n)return;const d=$("detail");d.replaceChildren(el("h3",n.name),el("p",n.definition),el("small",n.type+" · Layer "+n.layer));
  if(n.href)d.append(link("Open course lesson",n.href));
  if(n.look?.length){d.append(el("h4","What to look for"));for(const t of n.look)d.append(el("p",t));}
  if(n.alternatives)d.append(el("p","Alternative readings: "+n.alternatives));
  const gallery=el("div",undefined,"work-gallery");for(const p of n.images||[]){const f=el("figure");f.append(picture(p),el("figcaption",p.label||"Study"));gallery.append(f);}d.append(gallery);
  d.append(button(selection.has(id)?"Remove from prompt":"Add to prompt",()=>{toggle(n);showDetail(id);}),el("h4","Related concepts"));
  const edges=graph.edges.filter(e=>e.from===id||e.to===id);for(const e of edges){const other=byId.get(e.from===id?e.to:e.from);const row=el("p");row.append(button(other.name,()=>showDetail(other.id)),document.createTextNode(" — "+e.relation.replaceAll("_"," ")+" · "+e.evidence));d.append(row);}
  if(!edges.length)d.append(el("p","No explicit graph relationships yet."));
  d.scrollIntoView({block:"nearest",behavior:"smooth"});
}
function toggle(n){if(selection.has(n.id))selection.delete(n.id);else selection.set(n.id,n);renderSelection();renderCatalog();}
function renderSelection(){
  $("selected").replaceChildren(...[...selection.values()].map(n=>button(n.name+" ×",()=>toggle(n))));
  $("prompt").value=composePrompt({subject:$("subject").value,purpose:$("purpose").value,constraints:$("constraints").value,selected:[...selection.values()]});
  const styles=[...selection.values()].filter(n=>n.course==="I");
  $("composerWarning").textContent=styles.length>1?"Multiple artistic languages selected: decide which is primary or specify a deliberate blend.":"";
}
function downloadGraph(){
  const a=el("a");const url=URL.createObjectURL(new Blob([JSON.stringify(graph,null,2)],{type:"application/json"}));a.href=url;a.download="tsmc-visual-ontology.json";a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);
}
function renderAnalysis(raw){
  const r=validateAnalysis(raw,graph),root=$("analysisResult");root.replaceChildren(el("h3","Visible observations"));
  r.observations.forEach(s=>root.append(el("p",s)));
  root.append(el("h3","Matched course concepts"));
  for(const m of r.matches){const n=byId.get(m.id),card=el("article",undefined,"work-detail");card.append(el("h4",n.name+" · "+m.confidence+" confidence"),el("p",m.evidence));if(n.images?.length)card.append(picture(n.images[0]));if(n.href)card.append(link("Study this concept",n.href));card.append(button("Add to composer",()=>toggle(n)));root.append(card);}
  root.append(el("h3","Possible meanings"));for(const m of r.possible_meanings)root.append(el("p",m.reading+" — "+m.evidence+" | Alternative: "+m.alternative));
  root.append(el("h3","Unknowns"));r.unknowns.forEach(s=>root.append(el("p",s)));
  $("analysisStatus").textContent="Validated against course IDs. "+r.unrecognized+" unrecognized IDs discarded. Confidence is model-reported, not calibrated.";
}
const parseAnalysis=()=>{try{renderAnalysis(JSON.parse($("analysisJson").value));}catch(e){$("analysisStatus").textContent=e.message;}};
async function runVision(){
  const status=$("analysisStatus");if(!uploaded){status.textContent="Choose an image first.";return;}
  let endpoint;try{endpoint=new URL($("endpoint").value);if(endpoint.protocol!=="https:"&&!(endpoint.protocol==="http:"&&["localhost","127.0.0.1","[::1]"].includes(endpoint.hostname)))throw Error();}catch{status.textContent="Use HTTPS or a loopback HTTP endpoint.";return;}
  const model=$("model").value.trim(),key=$("apiKey").value;if(!model){status.textContent="Enter the vision model ID.";return;}
  if(!confirm("Send the uploaded image and course vocabulary to "+endpoint.origin+"?"))return;
  $("analyze").disabled=true;status.textContent="Analyzing…";try{
    const headers={"Content-Type":"application/json"};if(key)headers.Authorization="Bearer "+key;
    const r=await fetch(endpoint.href,{method:"POST",headers,body:JSON.stringify({model,messages:[{role:"user",content:[{type:"text",text:makeAnalysisPrompt(graph.nodes)},{type:"image_url",image_url:{url:uploaded}}]}]})});
    if(!r.ok)throw Error("Endpoint HTTP "+r.status);const data=await r.json();const content=data.choices?.[0]?.message?.content;if(typeof content!=="string")throw Error("Expected a chat completion with JSON text.");
    $("analysisJson").value=content.trim().replace(/^\x60{3}(?:json)?\s*/i,"").replace(/\s*\x60{3}$/,"");parseAnalysis();
  }catch(e){status.textContent="Analysis unavailable: "+e.message+". Check model, CORS and endpoint, or use manual mode.";}finally{$("analyze").disabled=false;}
}
const questions=[
{correct:"decision:side-light",choices:["decision:side-light","decision:rim-light","decision:front-light"],ask:"Which course lighting study is shown?",why:"Look for illumination on one side of the subject and shadow on the other; this example also changes hardness and fill."},
{correct:"style:baroque",choices:["style:baroque","style:cubism","style:ukiyo-e"],ask:"Which artistic language is this study intended to illustrate?",why:"Dramatic contrast, sweeping diagonals and theatrical staging are common Baroque conventions."},
{correct:"decision:centered-symmetry",choices:["decision:centered-symmetry","decision:rule-of-thirds","decision:diagonal"],ask:"Which compositional concept is the intended example?",why:"Look for a centered arrangement and balance around a central axis."},
{correct:"group:l21-g01",choices:["group:l21-g01","group:l21-g02","group:l21-g03"],ask:"Which semantic experiment contains this example? Consider alternative readings.",why:"The empty café and isolated figure suggest loneliness, but could also suggest peaceful solitude."},
{correct:"group:l22-g01",choices:["group:l22-g01","group:l22-g02","group:l22-g03"],ask:"Which experiment uses a recurring visual element across different meanings?",why:"Red can support different meanings when the surrounding context changes."}
];
function renderQuiz(){
  const root=$("quiz");root.replaceChildren();const valid=questions.filter(q=>byId.get(q.correct)?.images?.length&&q.choices.every(id=>byId.has(id)));
  if(!valid.length){root.append(el("p","No assessment examples available."));return;}
  if(quizIndex>=valid.length){root.append(el("h3","Recognition practice: "+score+" / "+answered),button("Restart",()=>{quizIndex=score=answered=0;renderQuiz();}));return;}
  const q=valid[quizIndex],n=byId.get(q.correct);root.append(el("p","Question "+(quizIndex+1)+" of "+valid.length),el("h3",q.ask));
  const im=picture(n.images[0]);im.alt="Unlabeled assessment illustration";root.append(im);const feedback=el("p"),choices=el("div",undefined,"work-fields");
  for(const id of [...q.choices].sort((a,b)=>byId.get(a).name.localeCompare(byId.get(b).name))){
    choices.append(button(byId.get(id).name,()=>{answered++;if(id===q.correct)score++;for(const b of choices.querySelectorAll("button"))b.disabled=true;feedback.textContent=(id===q.correct?"Correct. ":"The intended example is "+n.name+". ")+q.why;root.append(button("Next",()=>{quizIndex++;renderQuiz();}));}));
  }root.append(choices,feedback);
}
async function init(){
  const [a,b,c,d]=await Promise.all([read("../tsmc-styles/artwork.json"),read("../tsmc-seeing/seeing.json"),read("../tsmc-storytelling/storytelling.json"),read("concepts.json")]);graph=buildGraph(a,b,c,d);byId=new Map(graph.nodes.map(n=>[n.id,n]));
  $("status").textContent=graph.nodes.length+" nodes · "+graph.edges.length+" relationships · "+graph.unresolvedBridges.length+" unresolved proposed bridges";
  for(const id of ["searchConcept","courseFilter","layerFilter"])$(id).addEventListener("input",()=>{limit=36;renderCatalog();});
  $("more").onclick=()=>{limit+=36;renderCatalog();};$("exportGraph").onclick=downloadGraph;
  for(const id of ["subject","purpose","constraints"])$(id).addEventListener("input",renderSelection);
  $("copyPrompt").onclick=()=>copy($("prompt").value);$("clearSelection").onclick=()=>{selection.clear();renderSelection();renderCatalog();};
  $("upload").onchange=()=>{const f=$("upload").files[0];uploaded=null;$("preview").hidden=true;$("preview").removeAttribute("src");if(!f)return;if(!["image/jpeg","image/png","image/webp"].includes(f.type)||f.size>10*1024*1024){$("analysisStatus").textContent="Unsupported image or file exceeds 10 MB.";return;}const reader=new FileReader();reader.onload=()=>{uploaded=reader.result;$("preview").src=uploaded;$("preview").hidden=false;};reader.onerror=()=>$("analysisStatus").textContent="Could not read image.";reader.readAsDataURL(f);};
  $("analyze").onclick=runVision;$("copyAnalysis").onclick=()=>copy(makeAnalysisPrompt(graph.nodes));$("importAnalysis").onclick=parseAnalysis;
  $("showRubric").onclick=()=>{const i=["Loneliness","Authority","Suspense","Hope","Vulnerability"].indexOf($("intent").value),n=byId.get("group:l21-g0"+(i+1)),r=$("rubric");r.hidden=false;r.replaceChildren(el("p","Self-assess: identify the intended reading (0–2); specify two concrete visual mechanisms (0–2); preserve constraints (0–2); explain an alternate reading or a test with an audience (0–2). This is a rubric, not an automatic artistic score."));if(n){r.append(el("p",n.definition));for(const p of n.images){const f=el("figure");f.append(picture(p),el("figcaption",p.label));r.append(f);}r.append(link("Study the comparison",n.href));}};
  renderCatalog();renderSelection();renderQuiz();
}
init().catch(e=>{$("status").textContent="Could not load workbench: "+e.message;console.error(e);});
