#!/usr/bin/node
const request = require('request');
const urlFilm = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
const urlPeople = 'https://swapi-api.alx-tools.com/api/people/?page=';

request(urlFilm, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const characters = JSON.parse(body).characters;
    const people = {};
    for (let index = 1; index < 10; index++) {
      request(urlPeople + index, function (err, res, body) {
        if (err) {
          console.log(err);
        } else {
          const tmpRes = JSON.parse(body).results;
          tmpRes.forEach(element => {
            people[element.url] = element.name;
          });
          if (Object.keys(people).length === JSON.parse(body).count) {
            characters.forEach(character => {
              console.log(people[character]);
            });
          }
        }
      });
    }
  }
});
