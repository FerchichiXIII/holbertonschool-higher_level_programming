#!/usr/bin/node
// prints the title of a Star Wars movie where the episode number matches a given integer.

const request = require('request');
const argv = process.argv;
const url = 'https://swapi-api.hbtn.io/api/films/';

request.get(url + argv[2], function (err, reponse, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
