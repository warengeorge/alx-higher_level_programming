#!/usr/bin/node
const myObj = {
  type: 'object',
  value: 12
};
console.log(myObj);
myObj.incr = function () {
  this.value++;
};
myObj.incr();
console.log(myObj);
myObj.incr();
console.log(myObj);
myObj.incr();
console.log(myObj);
