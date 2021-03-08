
# AXIBO API Client

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi(swagger_client.ApiClient(configuration))

try:
    # Retrives an pose overlay image with a timestamp
    api_response = api_instance.get_pose_image()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->get_pose_image: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://10.42.0.1:2200/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ImagesApi* | [**get_pose_image**](docs/ImagesApi.md#get_pose_image) | **GET** /imaging/pose | Retrives an pose overlay image with a timestamp
*ImagesApi* | [**get_raw_image**](docs/ImagesApi.md#get_raw_image) | **GET** /imaging/cam | Retrives a raw image with a timestamp
*MotionApi* | [**config_motors**](docs/MotionApi.md#config_motors) | **PUT** /direct-control/config | Move AXIBO to relative position
*MotionApi* | [**get_motion_status**](docs/MotionApi.md#get_motion_status) | **GET** /direct-control/motion-status | Move AXIBO to relative position
*MotionApi* | [**move_absolute**](docs/MotionApi.md#move_absolute) | **PUT** /direct-control/move-absolute | Move AXIBO to absolute position
*MotionApi* | [**move_relative**](docs/MotionApi.md#move_relative) | **PUT** /direct-control/move-relative | Move AXIBO to relative position
*MotionApi* | [**set_homing**](docs/MotionApi.md#set_homing) | **PUT** /direct-control/home | Home AXIBO to set defualt limits
*SystemApi* | [**delete_wifi**](docs/SystemApi.md#delete_wifi) | **DELETE** /system/wifi | Delete WIFI network from the saved list
*SystemApi* | [**get_current_wifi**](docs/SystemApi.md#get_current_wifi) | **GET** /system/wifiInfo | Retreive AXIBO current wifi connection
*SystemApi* | [**get_progress**](docs/SystemApi.md#get_progress) | **GET** /system/status | Retreive the entire status of AXIBO
*SystemApi* | [**list_wifis**](docs/SystemApi.md#list_wifis) | **GET** /system/wifi | List all the available and saved WIFIs connections
*SystemApi* | [**set_wifi**](docs/SystemApi.md#set_wifi) | **PUT** /system/wifi | Connect to WIFI network


## Documentation For Models

 - [ApiResponse](docs/ApiResponse.md)
 - [ConnectWifi](docs/ConnectWifi.md)
 - [ControlCMD](docs/ControlCMD.md)
 - [ControlCMDPosition](docs/ControlCMDPosition.md)
 - [Errors](docs/Errors.md)
 - [ImageRes](docs/ImageRes.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [MotorConfig](docs/MotorConfig.md)
 - [MotorHome](docs/MotorHome.md)
 - [SystemMsg](docs/SystemMsg.md)
 - [Wifi](docs/Wifi.md)
 - [WifiList](docs/WifiList.md)
 - [WifiName](docs/WifiName.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author

contact@axibo.com

