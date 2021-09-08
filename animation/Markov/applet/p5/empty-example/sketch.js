//2 Dimensional Random Walk , coin flip, visualized on a coordinate graph 
var angle = 0;
function setup() {
  createCanvas(800, 800);
  slider = createSlider(0, 1, 1 / 2, 1 / 10);
  slider.changed(draw);
  button = createButton("next")
  button.mousePressed(draw)
  drift = createInput("0")
  drift.changed(draw)
  noLoop();

}
function coordinateSytem() {
  return line(10, 0, 10, 600), line(10, 0, 10, 600)
}
function randomWalk() {
  d = drift.value()
  prob = slider.value();
  states = (Array(100 - prob * 100).fill(-1)).concat((Array(prob * 100).fill(1)))
  start = [10, 400]
  currentPos = start
  for (i = 0; i < 800; i += 30) {
    fill(255)
    currentPos = [currentPos[0] + 30, currentPos[1] + random(states) * 30 + i * parseInt(d)]
    strokeWeight(5)
    point(currentPos[0], currentPos[1])
  }

}
function coordinateSytem() {
  strokeWeight(1)
  fill(255)
  //vertical axis
  line(10, 0, 10, 800)
  //HORIZONTAL axis
  line(10, 400, 800, 400)
  //POS VERTICAL
  var c = 1
  for (var i = 370; i > 0; i -= 30) {
    line(5, i, 15, i)
    text(c.toString(), 20, i - 5, 100, 100)
    c += 1
  }
  //NEG VERTICAL
  c = 1
  for (var i = 430; i < 800; i += 30) {
    line(5, i, 15, i)
    text((-1 * c).toString(), 20, i - 5, 100, 100)
    c += 1
  }
  //HORIZONTAL
  c = 1
  for (var i = 30; i < 800; i += 30) {
    line(i + 10, 395, i + 10, 405)
    text(c.toString(), i + 10 - 5, 380, 100, 100)
    c += 1
  }
}
function draw() {
  background(0)
  prob = slider.value();
  stroke(255);
  //add distance variable
  coordinateSytem()
  randomWalk()


}
