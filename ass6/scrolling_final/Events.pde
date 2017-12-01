


// This function uses Mac's in-built gain function. 
// You can comment it out to try it out
//void mouseWheel(MouseEvent event) {
//  float amount = event.getCount();
//  makeScroll(amount);  
//}

// This one implements a custom scroller using the mouse pressed and dragged events

void mousePressed() {
  prevY = mouseY;
}

// PID controller
// PV = process variable, prevY
// SP = SetPoint, mouseY
// OP = output, adjustment var for, and grows in propotion to PV

// The goal of tuning a PID loop is to make it stable, responsive and to minimize overshooting. These goals - especially the last two - conflict with each other

float gainP = 0.06;
float gainI = 0.00001;
float gainD = 0.1;
float summedError = 0;
float controllerOutput = 0;
float prevError = 0;

void mouseReleased(){
//  gainP = 0.0;
//  gainI = 0;
//  gainD = 0;
  summedError = 0;
  controllerOutput = 0;
  prevError = 0;
}

void mouseDragged(){
  float error = prevY - mouseY;
  summedError += error;
  controllerOutput = error * gainP + summedError * gainI + (error - prevError) * gainD;
  prevError = error;
  
  makeScroll(controllerOutput);  
}

void makeScroll(float e) {  
  if (pageScroll==0&&animatedScroll>0) {
    animatedScroll=0;
  } else if ((pageScroll==0&&animatedScroll==0&&e<0) ) {
  } else if (pageScroll==(pageN-1)&&animatedScroll<0) {
    animatedScroll=0;
  } else if ((pageScroll==(pageN-1)&&animatedScroll==0&&e>0) ) {
  } else {  
    // This is the gain (initially set to 1)
    animatedScroll-=1*e;
    wholeScrollAmount-=1*e;
  }

  if ((animatedScroll)<=-h) {
    animatedScroll%=-h;
    pageScroll++;
  } else if ((animatedScroll)>=h) {
    animatedScroll%=h;
    pageScroll--;
  }
}