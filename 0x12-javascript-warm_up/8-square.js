#!/usr/bin/node

// Print a square
const character = 'X';
const size = parseInt(process.argv[2]);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    console.log(character.repeat(size));
  }
}
