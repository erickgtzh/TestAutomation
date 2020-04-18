# TestAutomation Project

Clone repo from:


    https://github.com/erickgtzh/TestAutomation



Go to the project root, in my case is:


   cd C:\Users\01936\Documents\GitHub\TestAutomation



Set up environment running the following commands (change username for your pc user)


   virtualenv -p /home/username/opt/python-2.7.15/bin/python venv


Activate your environment:


   source venv/bin/activate


Here we’ve two options, run our automated suite or manual suite tests, after decide it go to:


   cd folder



and run for the automated test:

python automated_test.py


for the manual test:

python manual_test.py



[2.4]

If we want to change the default runs of our scripts, we need to go to some of our desired classes, for automated test cd python automated_test.py and for manual testing go to python manual_test.py

python manual_test.py

Automated test
Contains all the runnable scripts by pytest, there are just three cases: local calls, national calls and manage wifi status, you could skip or add suites in this class, they run in order.

Manual test
It contains all the runnable scripts that are tested by manual inputs for the calls, there is a script manager where we put all suites that we want to run, so if you decide to skip or add suites by here. 



[2.5]


Device environment

Serial: 	DXU7N18614000580
Brand: 	Huawei
Model: 	CLT-L04
OS:      	EMUI Android 9.1.0
Device:	HUAWEI P20 Pro
Build 
number:  	9.1.0.388(C69E9R1P11)


In this release you can find the suite for testing the following scripts:

get device connected by using adb shell
adb call for local numbers
adb call for national numbers
adb call for international numbers
adb call for emergency numbers
adb and uiautomator call for local numbers
adb and uiautomator call for national numbers
adb and uiautomator call for international numbers
adb and uiautomator call for emergency numbers
detect wifi status 
change wifi status or not, depending on input

It was tested in two ways:
Manual and automated

Manual: user inputs

Automated: pytest library (for local and national calls)*
* Library in pytest used to simulate input doesn't work with no unicode in Python 2.7, so '*' and '+' are not allowed

Versions for the scripts:

    name = 'call by adb'
    version = '1.3 (04/17/20)'
    info = 'script: {0} \nversion: {1}'.format(name, version)

    name = 'call by adb and ui automator'
    version = '1.3 (04/17/20)'
    info = 'script: {0} \nversion: {1}'.format(name, version)
    
    name = 'toggle wifi status'
    version = '1.3 (04/17/20)'
    info = 'script: {0} \nversion: {1}'.format(name, version)
