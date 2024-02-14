#!/usr/bin/node

let count = 0;

exports.logMe = function (item) {
  count++;
  console.log(`${count}: ${item}`);
};
