#!/usr/bin/node
let answer = 1;
if (isNaN(process.argv[2])) {
  console.log('1');
} else {
  for (let i = 1; i <= process.argv[2]; i++) {
    answer *= i;
  }
  console.log(answer);
}
