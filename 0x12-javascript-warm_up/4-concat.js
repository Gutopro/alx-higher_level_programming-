#!/usr/bin/node
function printArgument () {
  const args1 = process.argv[2];
  const args2 = process.argv[3];
  console.log(`${args1} is ${args2}`);
}
printArgument();
