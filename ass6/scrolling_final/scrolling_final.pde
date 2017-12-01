void setup() {
  size(719, 900, P2D);

  bg = color(255);
  w=width;
  h=height;
  prevY = mouseY;
  PImage temp;
  pages=new Page[pageN];
  for (int i=0; i< (pageN); i++) {
    temp=loadImage("pages-"+i+".jpg");
    pages[i]=new Page(temp);
    println(i+"th page processed");
  }
}