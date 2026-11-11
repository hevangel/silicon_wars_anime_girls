// A renderer-neutral, deterministic and bounded avatar state machine (#84).
export const ALLOWED={
 expression:new Set(["neutral","skeptical","smile"]),
 gesture:new Set(["idle","point","open_hand"]),
 gaze:new Set(["left","center","right"]),
 talking:new Set([false,true])
};
export class PresenterMachine {
 constructor(){this.reset()}
 reset(){this.queue=[];this.remaining=0;this.state={expression:"neutral",gesture:"idle",gaze:"center",talking:false};this.history=[]}
 enqueue(event){
  if(!event||typeof event!=="object")throw new TypeError("Command must be an object");
  if(event.type==="reset"){this.reset();return}
  if(!Object.hasOwn(ALLOWED,event.type))throw new RangeError("Unknown command type");
  if(!ALLOWED[event.type].has(event.value))throw new RangeError("Invalid input value");
  if(!Number.isInteger(event.duration_frames)||event.duration_frames<1||event.duration_frames>240)throw new RangeError("duration_frames must be 1..240");
  if(this.queue.length>=12)throw new RangeError("Queue at capacity; prevent agent overload");
  this.queue.push({type:event.type,value:event.value,duration_frames:event.duration_frames});
 }
 cancel(){this.queue.length=0;this.remaining=0;this.state.gesture="idle";this.state.talking=false}
 tick(){
  if(this.remaining===0&&this.queue.length){const event=this.queue.shift();this.state[event.type]=event.value;this.remaining=event.duration_frames;this.history.push({...event})}
  if(this.remaining>0)this.remaining--;
  return {...this.state};
 }
}
