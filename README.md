# at_test

at_test is a compact and lightweight framework to test AT commands on any modem. Its features are as below:
- It is written with Python.
- It's object-oriented and easy to extend.
- It's based on Python standard unittest lib and has provided necessary utility interfaces for handling AT command， so it is very convenient to add new test cases.

Pre-build conditions:
- Python 2.7 (you may do few change to make it work on other Python versions)
- pyserial 3.4

File overview:
- attestapp.py: 
This file is the start entry of this framework. It opens/closes serial port and loads/starts test cases.
- atcommand.py: 
This file is the core module to provide AT command utility interfaces.
- demotestcase.py:
This file is just an AT test case demo.
