#!/usr/bin/node

const request = require('request')

const id = process.argv[2];

const base =  'https://swapi-api.alx-tools.com/api/';
const fullUrl = `${base}films/${id}`;

request(fullUrl, { json: true }, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    // console.log(body)
    //  console.log("____----____")
    // console.log(JSON.parse(body).characters)
    // console.log(body.characters)
    // console.log("____----____")
    // console.log("____----____")
    const characters = body.characters;
    for (const ch of characters) {
      const chid = ch.split('/')[5];
      //  console.log(ch_id);

      const charUrl = `${base}people/${chid}`;
      request(charUrl, { json: true }, (error, response, body) => {
        if (error) { console.log(error); } else {
          console.log(body.name);
        }
      });
    }
    // console.log(body.character);
  }
});
