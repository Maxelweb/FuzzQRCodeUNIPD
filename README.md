# FuzzQR

![FuzzQR banner](https://user-images.githubusercontent.com/34033090/152697122-2000350a-edfa-4129-b70a-15025e45162e.png)


## QR Code Fuzzer Toolkit for Green Pass Checkers and Smartphone Apps

### Abstract

In recent years, QR codes become popular for different
applications such as Green Pass checking, used for COVID-
19 swab and vaccination verification. The personal QR code is
scanned with a smartphone application that certifies whether
the Green Pass is valid or not. Though, QR codes can be
manipulated by adding malicious code inside the payload. Hence,
we developed a toolkit, FuzzQR, for testing multiple QR codes in
an automated way on a particular set of fuzzing strings that may
crash the target app. In our experiments, we tested VerificaC19
on Android with 5 dictionaries of words containing symbols and
ASCII characters. Our tests on 344 words showed that our toolkit
correctly scanned 98.6% of the given QR Codes, with an average
scan time of 3-4 seconds. Moreover, FuzzQR can be adapted for
applications on both Android or iOS and custom dictionaries of
fuzzing strings.

Computer &amp; Network Security Course @ UniPD 2021-2022

## Build status

[![Python Checker](https://github.com/Maxelweb/FuzzQR/actions/workflows/python-checker.yml/badge.svg)](https://github.com/Maxelweb/FuzzQR/actions/workflows/python-checker.yml)

## Installation

Checkout each folder with the respective `README.md` file for the instructions.

- `docs` contains documentation on green passes
- `extra` contains extra script and git submodules of the used libraries

## Progress

**2022-02-02**

- General bugfix
- Moved old scripts inside `/extra`

**2022-01-27**

- Appium client and QR code visualizer are working
- Test on new fuzzing dictionaries

**2022-01-15**

- QR Code fuzzer for the Android app using Appium
- Fake Green Pass generator


**2021-12-28**

> Try to hack the QRCode library or try to hack operations before the sign checking

- Analysis on QR Code Literature
- General analysis on VerificaC19 app (on Android)
- Script creation to generate malevolous QR codes

## Credits

The extra tools and libraries used for this projects are inside `extra/` folder. Credits are given to the respective authors.

This project was developed by:

- Federico Carboni
- Mariano Sciacco
- Denis Donadel (project leader)
