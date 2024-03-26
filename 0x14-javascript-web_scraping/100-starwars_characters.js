#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const film = JSON.parse(body);
    film.characters.forEach(characterUrl => {
      request(characterUrl, function (err, res, body) {
        if (!err && res.statusCode === 200) {
          const character = JSON.parse(body);
          console.log(character.name);
        } else {
          console.error('Error fetching character:', err || `Status code: ${res.statusCode}`);
        }
      });
    });
  } else {
    console.error('Error fetching movie:', error || `Status code: ${response.statusCode}`);
  }
});
