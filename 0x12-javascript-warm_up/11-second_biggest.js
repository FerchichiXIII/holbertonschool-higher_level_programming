#!/usr/bin/node
const { argv } = require('yargs');
if (!argv[3]) {
  console.log(0);
} else {
  argv.shift();
  argv.shift();
  const arr = argv.map(x => parseInt(x));
  arr.sort((a, b) => b - a);
  arr.pop();
  console.log(arr[arr.length - 1]);
}
