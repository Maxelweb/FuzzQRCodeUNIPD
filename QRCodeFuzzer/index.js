const wdio = require("webdriverio");
const assert = require("assert");

var fuzzer = require('./fuzzerFile.js')

// {
//   "platformName": "Android",
//   "platformVersion": "11.0",
//   "deviceName": "TestDevice",
//   "app": "verificac19.apk",
//   "appPackage": "it.ministerodellasalute.verificaC19",
//  "appActivity": "ui.FirstActivity",
//   "automationName": "UiAutomator2"
// }

const opts = {
  path: '/wd/hub',
  port: 4723,
  capabilities: {
    "platformName": "Android",
    "platformVersion": "11.0",
    "deviceName": "TestDevice",
    "app": "verificac19.apk",
    "appPackage": "it.ministerodellasalute.verificaC19",
   "appActivity": "ui.FirstActivity",
    "automationName": "UiAutomator2"
  }
};



async function main () {
  const driver = await wdio.remote(opts); 

  let el2 = await driver.findElement("id", "it.ministerodellasalute.verificaC19:id/scan_mode_button");
  await driver.elementClick(el2.ELEMENT);
  let el3 = await driver.findElement("xpath", "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[1]");
  await driver.elementClick(el3.ELEMENT);
  // await driver.setTimeout({'pageLoad': 5000,'script': 1000 });
  let el4 = await driver.findElement("id", "it.ministerodellasalute.verificaC19:id/settings");
  await driver.elementClick(el2.ELEMENT);
  let el5 = await driver.findElement("id", "it.ministerodellasalute.verificaC19:id/totem_switch");
  await driver.elementClick(el5.ELEMENT);
  let el6 = await driver.findElement("id", "it.ministerodellasalute.verificaC19:id/back_image");
  await driver.elementClick(el6.ELEMENT);
  let el7 = await driver.findElement("id", "it.ministerodellasalute.verificaC19:id/qrButton");
  await driver.elementClick(el7.ELEMENT);
  let el8 = await driver.findElement("id", "android:id/button1");
  await driver.elementClick(el8.ELEMENT);
  let el9 = await driver.findElement("id", "com.android.permissioncontroller:id/permission_allow_foreground_only_button");
  await driver.elementClick(el9.ELEMENT);
  let el10 = await driver.findElement("xpath", "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.View");
  await driver.elementClick(el10.ELEMENT);
  let el11 = await driver.findElement("id", "it.ministerodellasalute.verificaC19:id/back_image");
  await driver.elementClick(el11.ELEMENT);
  let el12 = await driver.findElement("id", "it.ministerodellasalute.verificaC19:id/qrButton");
  await driver.elementClick(el12.ELEMENT);


//   let el2 = driver.element("it.ministerodellasalute.verificaC19:id/scan_mode_button");
// el2.click();
// let el3 = driver.element("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[1]");
// el3.click();
// let el4 = driver.element("it.ministerodellasalute.verificaC19:id/settings");
// el4.click();
// let el5 = driver.element("it.ministerodellasalute.verificaC19:id/totem_switch");
// el5.click();
// let el6 = driver.element("it.ministerodellasalute.verificaC19:id/back_image");
// el6.click();
// let el7 = driver.element("it.ministerodellasalute.verificaC19:id/qrButton");
// el7.click();
// let el8 = driver.element("android:id/button1");
// el8.click();
// let el9 = driver.element("com.android.permissioncontroller:id/permission_allow_foreground_only_button");
// el9.click();
// let el10 = driver.element("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.View");
// el10.click();
// let el11 = driver.element("it.ministerodellasalute.verificaC19:id/back_image");
// el11.click();
// let el12 = driver.element("it.ministerodellasalute.verificaC19:id/qrButton");
// el12.click();


  // const field = await client.$("android.widget.EditText");
  // await field.setValue("Hello World!");
  // const value = await field.getText();

  // assert.strictEqual(value,"Hello World!");

 // await driver.deleteSession();

}


main();


