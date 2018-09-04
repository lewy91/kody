function setup() {
  // put setup code here
  createCanvas(1000, 1000);
}

function draw() {
  // put drawing code here
  strokeWeight(11);
  stroke(254,255,73);
  fill(255, 0, 0);
   ellipse(100, 100, 100, 60);

  strokeWeight(3);
  stroke(63,17,73);
  fill(0,255,0);
  ellipse(110, 200, 800, 100);

  strokeWeight(8);
  stroke(255,173,73);
  fill(255, 204, 0);
  rect(120, 20, 55, 55, 20);

  strokeWeight(14);
  stroke(0,17,73);
  fill(0, 255,0 );
  triangle(30, 75, 58, 20, 86, 75);


noFill();
noStroke();
  if (mouseIsPressed) {
    if (mouseButton === LEFT){
    r = random(255);
    g = random(255);
    b = random(255);
   strokeWeight(20);
   fill(r,g,b,127);
   stroke(r,g,b);
 }
 if(mouseButton === CENTER) {
   strokeWeight (20);
   fill(255,255,255);
   stroke(255,255,255);
   rect(mouseX-10,mouseY-10,20,20);
 }
  } else {
    noFill();
    noStroke();
  }
  point(mouseX,mouseY);
}

function mouseClicked() {
  if (mouseButton === LEFT) {
    rect(mouseX-10,mouseY-10,20,20);
  } else {
    ellipse(mouseX-10,mouseY-10,20,20);
  }
}
