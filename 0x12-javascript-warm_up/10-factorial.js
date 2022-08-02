#!/usr/bin/node
function factorial (n) {
  let answer = 1;
  if (isNaN(n)) {
    return answer;
  } else {
    for (let i = n; i >= 1; i--) {
      answer = answer * i;
    }
    return answer;
  }
}
console.log(factorial(process.argv[2]));
