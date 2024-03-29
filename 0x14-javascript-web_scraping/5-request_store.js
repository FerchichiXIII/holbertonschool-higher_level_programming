#!/usr/bin/node
// gets the contents of a webpage and stores it in a file.

const request = require('request');
const fs = require('fs');

request(process.argv[2], function (_err, rest, body) {
  fs.writeFile(process.argv[3], body, 'utf8', function (err) {
    if (err) {
      console.log(err);
    }
  });
});
