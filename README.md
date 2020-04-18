# Test Automation Project

Test Automation is a class project that contains the following general scripts:
  - ADB Call
  - ADB and UIAutomator call
  - Wi-Fi state change

# Set Up

**Clone repo:**

    https://github.com/erickgtzh/TestAutomation

**Go to the project root, in my case is:**

    cd C:\Users\01936\Documents\GitHub\TestAutomation

**Clone repo:**

    https://github.com/erickgtzh/TestAutomation

**Set up environment running the following commands (change username for your pc user):**

    virtualenv -p /home/username/opt/python-2.7.15/bin/python venv

**Activate your environment:**

    source venv/bin/activate
    
**Here we’ve two options, run our automated suite or manual suite tests, after decide it go to:**

    cd folder
        
**For the automated inputs:**

    python automated_test.py
    
**or the manual test:**

    python automated_test.py
    

# Release notes

**Test cases:**

    - adb call for local numbers
    - adb call for national numbers
    - adb call for international numbers
    - adb call for emergency numbers
    - adb and uiautomator call for local numbers
    - adb and uiautomator call for national numbers
    - adb and uiautomator call for international numbers
    - adb and uiautomator call for emergency numbers
    - detect wifi status
    - change wifi status or not, depending on input

**Ways to test:**
 - **Automated:** pytest library (for local and national calls)\* 
* (\*) Library in pytest used to simulate input doesn't work with no unicode in Python 2.7, so '\*' and '+' are not allowed*

![alt text](https://lh3.googleusercontent.com/yB9bRrF6NDc2sr526SQlTGgV8TnxJfU_02JXoyRvxmJkFakyaHXFwqJRmfLyft1k_lVUlIYGlrsS9-ZBYcyAX6gOtLE-8b1o8F27ru4Wx3wLZcCTOCCXoHCZ8qCHZ6R7ev5nd7Izwp2VOqJh1P2hLlZWBuRhOypZwkEFyeBgV7n2WAT6TfuEqLNj6CbWm6okeKmwtw1-S-zKqckkoeBOgYoGxaa-UrmF8RqJkInZ5kJpcMvNhHBpWgn80hTBwvryZjURghguowd_tXcsG59-znOLh8iUEaHL8R9o_HpCnh7u42Vnbf499EwuWv3SqqVqnp-ZVq-VIy2izywB3kC0Lj7NUi3P4_GxVA8sbB_acJ42RJjQbL5OS3enHCp4P1LiuaFLWBr_3qWMHDAsFdJTKMOK4Y_z8ysGYOqeLJr2ND_aM4hczv6tXlrVSMA-k4zGmiqeoOtfcCKZppgFvyCnRQy1tfJktZ1WDiw3d72_qJYl3hx8T3S0UF41jjiFVQcyjGdjsU_ZK9DzKORE-baxS4tKX64rkpvbqPCo3dXyAP2hpISk6rGOlaQDF-NYW7vhrIY-agP0GrOJ-1S_QYxX3K8nOq7MR7lDI56ywg3ZDDFxg4Y3w5gwo_wqzGlOXz7hGgseHhOjNmFIe1nsjqu_EDfIg3u2q-YA8boIgJSmJixXd1pZg_kDAW-8MGCo=w589-h283-no)



 - **Manual:** user inputs

![alt text](https://lh3.googleusercontent.com/CkbWOHf6RvGAxRSO87PbAPOCOiY5RbN2zny2xHY1CRvEGvwthIrtp59I8U-QXqz8fIdO_I2I9rCociJRK2RYwbbMBiweoH_5g3gE_u9eTEXhzYPHcHpyxY5erFL4d1FR4_Xi9X7nj2NW9AlH3ThJyJFc57c2qWs7jlIW5Y7ZjNqlbqnDO9_tWHZmskYW-vaiAHdoGuFmSMt2EcFq_5xwizkdMmIAcynT8Txi1y3r8XxErsJS8owelqJmIG4EUyaWKw_ZijHuOMzlQdTItoNEkTwVrlJ2j6KDfk07vItCJyokIOmKnYqTkCbsQckr22F6ELEvm_fLpjh2xVsIqdStR5FzAXijN-JK1MJzZdIM1mYdIzcP2wDMbSsZPjaukxOS2Geh67MkW7WW8Vis_RN84c8xz5cKc0fyRn95_eKxK3vEbQ6zt4stJwIxtOzFyAlPQOd3XvzojAjh2gECZmqRroorAYg3a4d3AKTPaY3KMcSNgEP6EhWPCGRyQ4GLlrWB0nyP0itXr59F6T99vzzhc32MSDC3svqJeWAml4nBE61F9-hf3nYy4XdVDHiX3TYA86Ofrcam8ZGuv3NDanHCSVpiByCF_I2Wnehp6uvvDGSI7q09wbFWdQvAmXGmyXw7c1HOCgHPT7XPdKJPrFklbE46TbFZAcNKRzOIHf1CIa8iNghIiRcaUGHdNQ3S=w599-h439-no)



Those are the general results...

** Results for each test cases:**

|                                                               | TC Pasados | TC Fallados | TC Module | %       | Blocked | Bugs |
|---------------------------------------------------------------|------------|-------------|-----------|---------|---------|------|
| Call local number                                             | 4          | 0           | 4         | 100,00% | 0       | 0    |
| Call national numbers                                         | 4          | 0           | 4         | 100,00% | 0       | 0    |
| Call international numbers                                    | 2          | 2           | 4         | 50,00%  | 0       | 2    |
| Call emergency numbers                                        | 2          | 2           | 4         | 50,00%  | 0       | 2    |
| Call number with special characters                           | 4          | 0           | 4         | 100,00% | 0       | 0    |
| Call when another app is in foreground                        | 2          | 2           | 4         | 50,00%  | 0       | 2    |
| Turn On wifi                                                  | 2          | 0           | 2         | 100,00% | 0       | 0    |
| Turn Off wifi                                                 | 2          | 0           | 2         | 100,00% | 0       | 0    |
| Turn On WiFi when WiFi is On                                  | 2          | 0           | 2         | 100,00% | 0       | 0    |
| Turn Off WiFi when Wifi is Off                                | 2          | 0           | 2         | 100,00% | 0       | 0    |
| Turn On WiFi while another app is foreground and Wifi is On   | 2          | 0           | 2         | 100,00% | 0       | 0    |
| Turn Off WiFi while another app is foreground and Wifi is On  | 2          | 0           | 2         | 100,00% | 0       | 0    |
| Turn On WiFi while another app is foreground and Wifi is Off  | 2          | 0           | 2         | 100,00% | 0       | 0    |
| Turn Off WiFi while another app is foreground and Wifi is Off | 2          | 0           | 2         | 100,00% | 0       | 0    |


**Abstract**

|              |         | TC Passed | TC Failed | TC Blocked |
|--------------|---------|-----------|-----------|------------|
| Total TC     | 40      | 34        | 6         | 0          |
| % Test Cases | 100,00% | 75,00%    | 15,00%    | 0          |



# Project Structure

- model 
Folder help, we get all the methods
- suite 
Is where we have the suite information (suite methods, name, version, etc).
- test
Let us run all of them and get the results. 
- docs
All project documentation

**Scripts versions**

    name = 'call by adb'
    version = '1.3 (04/17/20)'
    info = 'script: {0} \nversion: {1}'.format(name, version)

    name = 'call by adb and ui automator'
    version = '1.3 (04/17/20)'
    info = 'script: {0} \nversion: {1}'.format(name, version)

    name = 'toggle wifi status'
    version = '1.3 (04/17/20)'
    info = 'script: {0} \nversion: {1}'.format(name, version)


### Todos

 - Release 1.1

License
----

[Erick Gutiérrez](https://github.com/erickgtzh)
