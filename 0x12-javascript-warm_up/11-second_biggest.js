#!/usr/bin/node

// Find biggest second number in a list
const numberOfArgs = process.argv.length;
const listOfNumbers = process.argv.slice(2);
const indexOfBiggestSecondNumber = listOfNumbers.length - 2;

function findBiggestSecondNumber (numbers) {
  if (numberOfArgs < 4) {
    console.log(0);
    return;
  }

  const sortedNumbers = numbers.sort((a, b) => a - b);
  const BiggestSecondNumber = sortedNumbers[indexOfBiggestSecondNumber];
  return BiggestSecondNumber;
}

console.log(findBiggestSecondNumber(listOfNumbers));
