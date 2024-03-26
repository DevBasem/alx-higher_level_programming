#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const characterId = '18';

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('Error occurred while making the request:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Unexpected status code:', response.statusCode);
    return;
  }

  let filmsData;
  try {
    filmsData = JSON.parse(body).results;
  } catch (parseError) {
    console.error('Error parsing API response:', parseError);
    return;
  }

  if (!Array.isArray(filmsData)) {
    console.error('Unexpected API response format: filmsData is not an array');
    return;
  }

  let count = 0;
  for (const film of filmsData) {
    if (!Array.isArray(film.characters)) {
      console.error('Unexpected film format: characters list not found or not an array');
      continue;
    }
    if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)) {
      count++;
    }
  }

  console.log(count);
});
