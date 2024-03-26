#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const characterId = '18';
const characterUrl = `https://swapi-api.alx-tools.com/api/people/${characterId}/`;

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  const filmsData = JSON.parse(body).results;
  const count = filmsData.reduce((acc, film) => {
    if (film.characters.find(character => character === characterUrl)) {
      return acc + 1;
    }
    return acc;
  }, 0);
  console.log(count);
});
