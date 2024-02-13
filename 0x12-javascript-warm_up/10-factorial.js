#!/usr/bin/node

// get the factorial
const firstArg = parseInt(process.argv[2]);

function factorial (number) {
  if (number >= 1) {
    return number * factorial(number - 1);
  }

  return 1;
}

console.log(factorial(firstArg));
