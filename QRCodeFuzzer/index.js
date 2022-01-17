const wdio = require("webdriverio");
const assert = require("assert");

var fuzzer = require('./fuzzerFile.js')

const opts = {
  path: '/wd/hub',
  port: 4723,
  capabilities: {
    "platformName": "Android",
    "platformVersion" : "9.0",
    // "platformVersion": "10.0",
    // "platformVersion": "11.0",
    // "platformVersion": "12.0",
    "deviceName": "TestDevice",
    "app": "verificac19.apk",
    "appPackage": "it.ministerodellasalute.verificaC19",
   "appActivity": "ui.FirstActivity",
    "automationName": "UiAutomator2",
    "noReset": "true"
  }
};



async function main () {
  const driver = await wdio.remote(opts); 

  await driver.setTimeout({ 'implicit': 1000 });

  // Click "Scan QR" button
  let el7 = await driver.findElement("id", "it.ministerodellasalute.verificaC19:id/qrButton");
  await driver.elementClick(el7.ELEMENT);

  for (i=0; i<fuzzer.size(); ++i){
    // Wait for the qr to be scanned
    await driver.setTimeout({ 'implicit': 5000 });

    // Wait result window 
    // ------------ FIXME: maybe to change 
    await driver.findElement("id", "it.ministerodellasalute.verificaC19:id/scrollView3");

    await driver.setTimeout({ 'implicit': 1000 });

    // Take screenshot
    let image = await driver.takeScreenshot();

    // Save screenshot to file
    let path = "screen/" + fuzzer.readFile().file + ".png";
    require('fs').writeFile(path, image, 'base64', function(err) {
        console.log(err);
    });

    // Update QR
    fuzzer.requestNewQR();

    // Go back
    await driver.back();
  }
}


main();


