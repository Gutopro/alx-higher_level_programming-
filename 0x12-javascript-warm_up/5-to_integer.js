#!/usr/bin/node
let args = parseInt(process.argv[2]);
if (args) {
  console.log('My Number: ' + args);
} else {
  console.log('Not a Number');
}
