#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log('No number');
} else {
  console.log('My number: ' + parseInt(process.argv[2]));
}
