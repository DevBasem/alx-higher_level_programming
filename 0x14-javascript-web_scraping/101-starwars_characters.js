#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const film = JSON.parse(body);
    const charactersUrls = film.characters;
    const charactersNames = [];

    // Function to fetch character name from URL
    const fetchCharacterName = function (characterUrl) {
      return new Promise((resolve, reject) => {
        request(characterUrl, function (err, res, body) {
          if (!err && res.statusCode === 200) {
            const character = JSON.parse(body);
            resolve(character.name);
          } else {
            reject(err || `Status code: ${res.statusCode}`);
          }
        });
      });
    };

    // Fetch character names sequentially
    const fetchCharacters = async function () {
      for (const characterUrl of charactersUrls) {
        try {
          const characterName = await fetchCharacterName(characterUrl);
          charactersNames.push(characterName);
        } catch (err) {
          console.error('Error fetching character:', err);
        }
      }
      // Print character names in order
      charactersNames.forEach(name => console.log(name));
    };

    fetchCharacters();
  } else {
    console.error('Error fetching movie:', error || `Status code: ${response.statusCode}`);
  }
});
