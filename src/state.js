import {objects} from './objects.js';
export const SAVE_KEY='bar-space-v1';const ids=new Set(objects.map(o=>o.id));
export function loadState(storage){let s={};try{s=JSON.parse(storage.getItem(SAVE_KEY))||{}}catch{}return{zone:s.zone==='deep'?'deep':'solar',selected:ids.has(s.selected)?s.selected:'earth',visited:[...new Set((Array.isArray(s.visited)?s.visited:[]).filter(x=>ids.has(x)))],muted:!!s.muted};}
