#!/usr/bin/node

// nodejs args
const numberOfArgs = process.argv.length - 1;

if (isNaN(parseInt(process.argv[numberOfArgs]))) {
  console.log ('Not a number');
} else {
  console.log(`My number: ${parseInt(process.argv[numberOfArgs])}`);
}
