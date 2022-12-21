#!/usr/bin/node
const args = process.argv
  .slice(2)
  .map(arg => Number.parseInt(arg))
  .sort((a, b) => b - a);
const val = args.length < 2 ? 0 : args[1];

console.log(val);
