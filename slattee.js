
const p5 = require('p5/lib/p5.js');
p5.createP5();
function setup() {
  createCanvas(400, 400);
  background(220);

  // Set initial apple position and size
  let appleX = width / 2;
  let appleY = 50;
  let appleSize = 20;

  // Initialize translation amount for gravity
  let gravityForce = 0.5; // This value determines the "gravity strength"
    let handX, handY, handSize;

// Define initial hand position and size based on apple's position
    handX = appleX;
    handY = appleY - appleSize * 3; // Adjust based on desired hand size and position relative to apple
    handSize = appleSize * 2; // Adjust hand size relative to apple

}


function draw() {
  // Translate the canvas down by the gravity force
  translate(0, gravityForce);

  // Draw the apple using the ellipse function with the translated coordinates
  fill(255, 0, 0);
  ellipse(appleX, appleY, appleSize, appleSize);

  // Draw the hand's fingers and arm
  stroke(200, 150, 100); // Set hand color
  strokeWeight(3); // Set hand line thickness
  line(handX, handY, handX, handY + handSize); // Draw finger
  line(handX, handY + handSize, handX + handSize / 3, handY + handSize * 2);
  line(handX, handY + handSize, handX - handSize / 3, handY + handSize * 2);
  arc(handX, handY - handSize / 2, handSize, handSize, 0, PI); // Draw curved arm
}
