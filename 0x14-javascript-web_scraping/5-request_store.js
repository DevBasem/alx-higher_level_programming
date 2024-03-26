#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    fs.writeFileSync(filePath, body, 'utf-8');
  } else {
    console.error('Error:', error || `Invalid response: ${response.statusCode}`);
  }
});
