#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (let i = 0; list.length > i; i++) {
    if (list[i] === searchElement) {
      count++;
    }
  }
  return count;
}
