const fs = require('fs');
const { get } = require('http');
const _fuzzer_file = "./fuzzer.json";

// Logic of status
//  0 = keep the same QR code shown
//  1 = change the QR code to the next one

let _fuzzer = { status: 0, file: "none", size: 0}

function readFuzzer() {
  let rawdata = fs.readFileSync(_fuzzer_file);
  let fuzzer = JSON.parse(rawdata);
  _fuzzer = fuzzer;
  return fuzzer;
}

function requestNewQRFuzzer() {
  _fuzzer.status = 1;
  fs.writeFileSync(_fuzzer_file, JSON.stringify(_fuzzer));
}

function getSize() {
  readFuzzer()
  return _fuzzer.size;
}

exports._fuzzer_file = _fuzzer_file;
exports._fuzzer = _fuzzer;
exports.readFile = readFuzzer;
exports.requestNewQR = requestNewQRFuzzer;
exports.size = getSize;