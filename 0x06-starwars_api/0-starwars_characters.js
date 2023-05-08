#!/usr/bin/node

/* A acript that prints all the characters of star wars movies */

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

function getCharacter (charactersUrl) {
  return new Promise((resolve, reject) => {
    request(charactersUrl, (err, res, body) => {
      if (err) reject(err);
      resolve(JSON.parse(body).name);
    });
  });
}

request(url, async (err, res, body) => {
  if (err) console.log(err);
  const characters = JSON.parse(body).characters;
  for (const character of characters) {
    console.log(await getCharacter(character));
  }
});
