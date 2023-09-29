#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];

const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;
request(url, async function (error, response, body) {
  if (error) console.error(error);

  const object = JSON.parse(body);
  const charactersList = object.characters;

  for (const url of charactersList) {
    await new Promise(function (resolve, reject) {
      request(url, function (error, response, body) {
        if (error) {
          console.error(error);
          reject(error);
        }
        const object = JSON.parse(body);
        console.log(object.name);
        resolve();
      });
    });
  }
});
