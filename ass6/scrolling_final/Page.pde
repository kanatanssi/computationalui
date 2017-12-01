class Page {
  PImage originalImage;

  int pw;
  int ph;
  int clock;
  float life;
  int drawObjectNumber;

  Page(PImage _originalImage) {
    originalImage=createImage(width, height, RGB);
    _originalImage.loadPixels();
    originalImage.loadPixels();        
    arrayCopy(_originalImage.get().pixels, originalImage.pixels);

    pw=originalImage.width;
    ph=originalImage.height;
  }

  void draw() {      
    image(originalImage, 0, 0);
  }
}