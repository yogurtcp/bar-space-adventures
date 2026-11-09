// A readable, not-to-scale sky chart. Galaxies are far beyond the Solar System.
const planetIds=['mercury','venus','earth','mars','jupiter','saturn','uranus','neptune'];
export function chart(tall=false){
 const width=tall?1500:2200,height=tall?2200:1600,cx=tall?500:650,cy=tall?680:520;
 const radii=tall?[150,190,230,270,310,350,395,440]:[150,220,290,360,430,500,570,640];
 const angles=tall?[200,300,60,235,155,340,90,47]:[200,315,65,240,150,340,90,30];
 const flatten=tall?1.2:.55;
 const orbits=radii.map((rx,i)=>({id:planetIds[i],cx,cy,rx,ry:rx*flatten}));
 const sizes={mercury:48,venus:70,earth:74,mars:64,jupiter:118,saturn:152,uranus:78,neptune:76};
 const positions={sun:{x:cx,y:cy,size:140,width:142}};
 for(let i=0;i<planetIds.length;i++){const a=angles[i]*Math.PI/180,id=planetIds[i];positions[id]={x:cx+radii[i]*Math.cos(a),y:cy+radii[i]*flatten*Math.sin(a),size:sizes[id],width:id==='saturn'?180:160};}
 positions.moon={x:positions.earth.x+155,y:positions.earth.y,size:38,width:142};
 Object.assign(positions,tall?{
  pluto:{x:140,y:150,size:58,width:150},asteroid:{x:180,y:560,size:64,width:168},comet:{x:835,y:180,size:92,width:158},stars:{x:480,y:100,size:98,width:178},nebula:{x:840,y:1290,size:125,width:184},milkyway:{x:155,y:1290,size:148,width:200},andromeda:{x:500,y:1370,size:130,width:208}
 }:{
  pluto:{x:155,y:248,size:58,width:150},asteroid:{x:279,y:446,size:64,width:168},comet:{x:980,y:110,size:92,width:158},stars:{x:1360,y:130,size:98,width:178},nebula:{x:1460,y:410,size:132,width:200},milkyway:{x:1430,y:860,size:154,width:210},andromeda:{x:1030,y:900,size:130,width:212}
 });
 // Extend the same sky around the existing Solar System; keep old coordinates relocatable.
 const shift=250;
 for(const p of Object.values(positions)){p.x+=shift;p.y+=shift;}
 for(const orbit of orbits){orbit.cx+=shift;orbit.cy+=shift;}
 Object.assign(positions,tall?{
  betelgeuse:{x:120,y:170,size:108,width:240},sirius:{x:420,y:100,size:94,width:180},polaris:{x:780,y:100,size:94,width:226},satellite:{x:1250,y:170,size:116,width:210},iss:{x:1360,y:500,size:160,width:272},hubble:{x:1370,y:900,size:140,width:206},webb:{x:1360,y:1290,size:145,width:200},perseverance:{x:1370,y:1710,size:140,width:278},curiosity:{x:1160,y:2040,size:140,width:242},ingenuity:{x:780,y:2040,size:140,width:256},voyager:{x:400,y:1940,size:145,width:230},blackhole:{x:140,y:1750,size:145,width:245},quasar:{x:120,y:1180,size:132,width:210}
 }:{
  betelgeuse:{x:300,y:140,size:108,width:240},sirius:{x:680,y:140,size:94,width:180},polaris:{x:1050,y:130,size:94,width:226},satellite:{x:1400,y:130,size:116,width:210},iss:{x:1810,y:130,size:160,width:272},hubble:{x:2010,y:440,size:140,width:206},webb:{x:2030,y:770,size:145,width:200},perseverance:{x:2030,y:1110,size:140,width:278},curiosity:{x:1870,y:1430,size:140,width:242},ingenuity:{x:1490,y:1430,size:140,width:256},voyager:{x:1090,y:1430,size:145,width:230},blackhole:{x:320,y:1230,size:145,width:245},quasar:{x:140,y:940,size:132,width:210}
 });
 const center={cx:cx+shift,cy:cy+shift};
 const plutoOrbit={...center,a:tall?510:730,e:.249,inclination:17.16,flatten};
 plutoOrbit.points=Array.from({length:241},(_,i)=>plutoPoint(plutoOrbit,i*Math.PI*2/240));
 const pluto=plutoPoint(plutoOrbit,4);positions.pluto={x:pluto.x,y:pluto.y,size:58,width:164};
 return{width,height,...center,orbits,positions,plutoOrbit,belt:{...center,rx:(radii[3]+radii[4])/2,ry:(radii[3]+radii[4])/2*flatten},moonOrbit:{cx:positions.earth.x,cy:positions.earth.y,rx:155,ry:65},tall};
}
// Eccentric orbital plane, tilted before the chart projection; Sun remains the focus.
export function plutoPoint(o,anomaly){const r=Math.PI/180,w=45*r,node=-25*r,i=o.inclination*r;
 const x=o.a*(Math.cos(anomaly)-o.e),y=o.a*Math.sqrt(1-o.e*o.e)*Math.sin(anomaly);
 const xp=x*Math.cos(w)-y*Math.sin(w),yp=x*Math.sin(w)+y*Math.cos(w);
 const X=xp*Math.cos(node)-yp*Math.cos(i)*Math.sin(node),Y=xp*Math.sin(node)+yp*Math.cos(i)*Math.cos(node),Z=yp*Math.sin(i);
 return{x:o.cx+X,y:o.cy+o.flatten*Y-.5*Z};
}
export function fitView(c,w,h){return{cx:c.width/2,cy:c.height/2,z:1,scale:Math.min(w/c.width,h/c.height)*.95};}
