function randomExponential(rate,randomUniform){
  rate = rate || 1
  var U = randomUniform 
  if (typeof randomUniform == 'function') U=randomUniform() ;
  if (!U) U=Math.random();
  return -Math.log(U)/rate; 
}
function poisson(la,limit){
  N = []
  for (i=0 ; i<limit ; i++){
    v = 1 
    k = -1 
    while (v>Math.expl(-la)){
      v = Math.random()
      k = k+1
    }
    N.push(k)
  }
} 
function setup(){
  createCanvas(400,400);
  noLoop()
}
function draw(){
  background(220);
  L = 400 
  a = 0.8 
  N = poisson(a*L,1)[0]
  console.log(N)
}
