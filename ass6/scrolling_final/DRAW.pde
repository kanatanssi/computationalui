void draw() {
  background(255);  
  pushMatrix();
  translate(0, animatedScroll);
  pushMatrix();
  translate(0, -h);
  if (pageScroll>1) {
    pages[pageScroll-1].draw();
  }
  popMatrix();
  println(pageScroll);
  pages[pageScroll].draw();
  
  pushMatrix();
  translate(0, h);
  if (pageScroll<pageN-1) {
    pages[pageScroll+1].draw();
  }
  popMatrix();
  popMatrix();
}