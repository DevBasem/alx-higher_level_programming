#!/usr/bin/node

const originalDict = require('./101-data').dict;

const newDict = {};

for (const userId in originalDict) {
  const occurrences = originalDict[userId];

  if (!(occurrences in newDict)) {
    newDict[occurrences] = [];
  }

  newDict[occurrences].push(userId);
}

console.log(newDict);
