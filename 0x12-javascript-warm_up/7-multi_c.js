#!/usr/bin/node

const args = parseInt(process.argv[2]);
if (!args) {
  console.log('Missing number of ocassions');
} else {
  for (let i = 0; i < Math.abs(args); i++) {
    console.log('Cis fun');
  }
}
