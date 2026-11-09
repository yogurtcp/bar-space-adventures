// A readable, not-to-scale sky chart. Galaxies are far beyond the Solar System.
const planetIds=['mercury','venus','earth','mars','jupiter','saturn','uranus','neptune'];
export function chart(tall=false){
 const width=tall?1000:1600,height=tall?1540:1080,cx=tall?500:650,cy=tall?680:520;
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
 return{width,height,cx,cy,orbits,positions,belt:{cx,cy,rx:(radii[3]+radii[4])/2,ry:(radii[3]+radii[4])/2*flatten},moonOrbit:{cx:positions.earth.x,cy:positions.earth.y,rx:155,ry:65},tall};
}
export function fitView(c,w,h){return{cx:c.width/2,cy:c.height/2,z:1,scale:Math.min(w/c.width,h/c.height)*.95};}
