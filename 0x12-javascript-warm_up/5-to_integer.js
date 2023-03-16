#!/usr/bin/node
const args = process.argv[2];
if (/^\d+$/.test(args)) {
  console.log(`My Number: ${parseInt(args)}`);
} else if (/^\d*\.\d+$/.test(args)) {
  console.log(`My Number: ${(parseInt(args))}`);
} else {
  console.log('Not a Number');
}
