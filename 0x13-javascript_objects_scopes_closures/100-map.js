#!/usr/bin/node

const { list } = require('./100-data');

require('./100-data.js');
const map1 = list.map((x, index) => x * index);
console.log(list);
console.log(map1);
