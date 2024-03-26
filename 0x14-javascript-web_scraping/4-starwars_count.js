#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Invalid response:', response.statusCode);
  } else {
    const films = JSON.parse(body).results;
    let count = 0;
    for (const filmIndex in films) {
      const filmChars = films[filmIndex].characters;
      for (const charIndex in filmChars) {
        if (filmChars[charIndex].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
