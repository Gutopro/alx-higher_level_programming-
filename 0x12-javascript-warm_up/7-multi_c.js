#!/usr/bin/node

const args = process.argv[2];
if (/^\d+$/.test(args)) {
  const x = parseInt(args);
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurences');
}
