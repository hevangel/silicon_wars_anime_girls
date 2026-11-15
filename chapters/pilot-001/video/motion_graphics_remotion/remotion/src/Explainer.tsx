import React from 'react';
import {AbsoluteFill, interpolate, useCurrentFrame} from 'remotion';
const tiles = ['core 0','core 1','I/O die','cache'];
const box:React.CSSProperties={borderRadius:22,background:'#1c456d',border:'4px solid #8ccbf1',boxShadow:'0 20px 40px #0005',padding:25,color:'white'};
export const Explainer: React.FC=()=>{
 const frame=useCurrentFrame();
 const grow=interpolate(frame,[0,90],[0,1],{extrapolateLeft:'clamp',extrapolateRight:'clamp'});
 const isIntel=frame<240,isAmd=frame>=240&&frame<480;
 const chipletMove=interpolate(frame,[240,420],[160,0],{extrapolateLeft:'clamp',extrapolateRight:'clamp'});
 const fakeProgress=interpolate(frame,[480,540],[0,.1],{extrapolateLeft:'clamp',extrapolateRight:'clamp'});
 return <AbsoluteFill style={{background:'linear-gradient(120deg,#081b38,#30254f)',color:'#eff7ff',fontFamily:'Arial,sans-serif',padding:92}}>
   <div style={{fontSize:51,fontWeight:900}}>SILICON WARS · CHIPLET CONFRONTATION</div>
   <div style={{fontSize:29,opacity:.8}}>Fictional cartoon explanation. No measured benchmark numbers.</div>
   {isIntel&&<div style={{display:'flex',gap:28,marginTop:142,transform:`scale(${.82+.18*grow})`}}>{['Old code','x86 compatibility','Modern CPU'].map(label=><div key={label} style={{...box,flex:1,textAlign:'center',fontSize:39}}>{label}</div>)}</div>}
   {isAmd&&<div style={{display:'flex',gap:38,marginTop:120}}>{tiles.map((x,i)=><div key={x} style={{...box,flex:1,fontSize:34,textAlign:'center',background:'#902c53',transform:`translateY(${i%2?chipletMove:-chipletMove}px)`}}>{x}</div>)}</div>}
   {!isIntel&&!isAmd&&<div style={{marginTop:133,fontSize:56}}>TESTBENCH PROGRESS (COMEDIC FICTION)<div style={{...box,marginTop:45,height:84,padding:0,overflow:'hidden'}}><div style={{width:(fakeProgress*100)+'%',height:'100%',background:'#efab6e'}} /></div><div style={{textAlign:'right',fontSize:38}}>{fakeProgress.toFixed(1)}%</div></div>}
   <div style={{position:'absolute',left:92,bottom:85,fontSize:33,color:'#f2d79c'}}>{isIntel?'INTEL: “The old code stays.”':isAmd?'AMD: “Then I’ll build around it.”':'Compiling joke, not a hardware performance result.'}</div>
 </AbsoluteFill>;
};
