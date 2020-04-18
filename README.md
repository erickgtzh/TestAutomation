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

[![Foo](https://lh3.googleusercontent.com/ucDx_P8LJNxUL8WH62G8jWari53vMrGG4pThsivz4weXixnWl3ws1-_09wucJ6C_XMh3NY2fEIk2eaMbodnBoj6nKqd3acvGQMEhWqiu4gcOmjKpPd0BZVCiQQJ0rsNMNFk5mCO6XsMqn4PAKHFJHjR8TKOAhHVhvkJRgifc_1RVmOZ8XSY4J5x38-q7KHYdWs9V9EPyihev3_961FCA_3hzwK3ajnK-RKUPZuamBZpUqL9eL4311IhZOXSHf9gKigH7mmhGN0dUYcmXVmTdAprNbgevttlq8mGZXjgw_20EXrpiE30KdKssAjHvF6Eac61Pe3_gL75fKPF-2vKfMyIY_zct-bhXdY8rHIbup7vDL5KXQaa7HaA4UJrxEYfMCPSj_GOfyb51GUz4i24GfLGIvsdnebri3HvdldvPaWhp9qwlHQ56stun_CTPUsWRkQuq0psL5AoqQtKyZnINB4LIuVjdtxQc7_c3oMKILo7kgoByB9P3pf_Z9MLSlDx9W1K-QWU1p8MHs6v0E4Y5F874ZNfVziC6YJuy_1SwQpIscZPZ2l97kPvBpYOg8Uycmk7A3JHLKAvHEVZwyDdtf1xEGXFwxWRjCbBnW1CH0F4V2gxBDyMCKJNZsJQErOGpf6iRzmdJhqwmXC1XbnrqhJCVLBZ3YkORq3oCtMk7iR0UHSufpidTrqlQCINI=w589-h283-no)](https://lh3.googleusercontent.com/ucDx_P8LJNxUL8WH62G8jWari53vMrGG4pThsivz4weXixnWl3ws1-_09wucJ6C_XMh3NY2fEIk2eaMbodnBoj6nKqd3acvGQMEhWqiu4gcOmjKpPd0BZVCiQQJ0rsNMNFk5mCO6XsMqn4PAKHFJHjR8TKOAhHVhvkJRgifc_1RVmOZ8XSY4J5x38-q7KHYdWs9V9EPyihev3_961FCA_3hzwK3ajnK-RKUPZuamBZpUqL9eL4311IhZOXSHf9gKigH7mmhGN0dUYcmXVmTdAprNbgevttlq8mGZXjgw_20EXrpiE30KdKssAjHvF6Eac61Pe3_gL75fKPF-2vKfMyIY_zct-bhXdY8rHIbup7vDL5KXQaa7HaA4UJrxEYfMCPSj_GOfyb51GUz4i24GfLGIvsdnebri3HvdldvPaWhp9qwlHQ56stun_CTPUsWRkQuq0psL5AoqQtKyZnINB4LIuVjdtxQc7_c3oMKILo7kgoByB9P3pf_Z9MLSlDx9W1K-QWU1p8MHs6v0E4Y5F874ZNfVziC6YJuy_1SwQpIscZPZ2l97kPvBpYOg8Uycmk7A3JHLKAvHEVZwyDdtf1xEGXFwxWRjCbBnW1CH0F4V2gxBDyMCKJNZsJQErOGpf6iRzmdJhqwmXC1XbnrqhJCVLBZ3YkORq3oCtMk7iR0UHSufpidTrqlQCINI=w589-h283-no)


 - **Manual:** user inputs

[![Foo](https://lh3.googleusercontent.com/ucDx_P8LJNxUL8WH62G8jWari53vMrGG4pThsivz4weXixnWl3ws1-_09wucJ6C_XMh3NY2fEIk2eaMbodnBoj6nKqd3acvGQMEhWqiu4gcOmjKpPd0BZVCiQQJ0rsNMNFk5mCO6XsMqn4PAKHFJHjR8TKOAhHVhvkJRgifc_1RVmOZ8XSY4J5x38-q7KHYdWs9V9EPyihev3_961FCA_3hzwK3ajnK-RKUPZuamBZpUqL9eL4311IhZOXSHf9gKigH7mmhGN0dUYcmXVmTdAprNbgevttlq8mGZXjgw_20EXrpiE30KdKssAjHvF6Eac61Pe3_gL75fKPF-2vKfMyIY_zct-bhXdY8rHIbup7vDL5KXQaa7HaA4UJrxEYfMCPSj_GOfyb51GUz4i24GfLGIvsdnebri3HvdldvPaWhp9qwlHQ56stun_CTPUsWRkQuq0psL5AoqQtKyZnINB4LIuVjdtxQc7_c3oMKILo7kgoByB9P3pf_Z9MLSlDx9W1K-QWU1p8MHs6v0E4Y5F874ZNfVziC6YJuy_1SwQpIscZPZ2l97kPvBpYOg8Uycmk7A3JHLKAvHEVZwyDdtf1xEGXFwxWRjCbBnW1CH0F4V2gxBDyMCKJNZsJQErOGpf6iRzmdJhqwmXC1XbnrqhJCVLBZ3YkORq3oCtMk7iR0UHSufpidTrqlQCINI=w589-h283-no
)](https://lh3.googleusercontent.com/ucDx_P8LJNxUL8WH62G8jWari53vMrGG4pThsivz4weXixnWl3ws1-_09wucJ6C_XMh3NY2fEIk2eaMbodnBoj6nKqd3acvGQMEhWqiu4gcOmjKpPd0BZVCiQQJ0rsNMNFk5mCO6XsMqn4PAKHFJHjR8TKOAhHVhvkJRgifc_1RVmOZ8XSY4J5x38-q7KHYdWs9V9EPyihev3_961FCA_3hzwK3ajnK-RKUPZuamBZpUqL9eL4311IhZOXSHf9gKigH7mmhGN0dUYcmXVmTdAprNbgevttlq8mGZXjgw_20EXrpiE30KdKssAjHvF6Eac61Pe3_gL75fKPF-2vKfMyIY_zct-bhXdY8rHIbup7vDL5KXQaa7HaA4UJrxEYfMCPSj_GOfyb51GUz4i24GfLGIvsdnebri3HvdldvPaWhp9qwlHQ56stun_CTPUsWRkQuq0psL5AoqQtKyZnINB4LIuVjdtxQc7_c3oMKILo7kgoByB9P3pf_Z9MLSlDx9W1K-QWU1p8MHs6v0E4Y5F874ZNfVziC6YJuy_1SwQpIscZPZ2l97kPvBpYOg8Uycmk7A3JHLKAvHEVZwyDdtf1xEGXFwxWRjCbBnW1CH0F4V2gxBDyMCKJNZsJQErOGpf6iRzmdJhqwmXC1XbnrqhJCVLBZ3YkORq3oCtMk7iR0UHSufpidTrqlQCINI=w589-h283-no
)

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