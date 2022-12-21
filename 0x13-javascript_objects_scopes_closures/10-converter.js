#!/usr/bin/node
// JS Script
exports.converter = function (base) {
  return function mainConvert (num) {
    return num.toString(base);
  };
};
