# swagger_client.MotionApi

All URIs are relative to *http://10.42.0.1:2200/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**config_motors**](MotionApi.md#config_motors) | **PUT** /direct-control/config | Move AXIBO to relative position
[**get_motion_status**](MotionApi.md#get_motion_status) | **GET** /direct-control/motion-status | Move AXIBO to relative position
[**move_absolute**](MotionApi.md#move_absolute) | **PUT** /direct-control/move-absolute | Move AXIBO to absolute position
[**move_relative**](MotionApi.md#move_relative) | **PUT** /direct-control/move-relative | Move AXIBO to relative position
[**set_homing**](MotionApi.md#set_homing) | **PUT** /direct-control/home | Home AXIBO to set defualt limits


# **config_motors**
> ApiResponse config_motors(motorConfig=motorConfig)

Move AXIBO to relative position

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MotionApi()
motorConfig = swagger_client.MotorConfig() # MotorConfig | Specify the position and the speed to move AXIBO (optional)

try:
    # Move AXIBO to relative position
    api_response = api_instance.config_motors(motorConfig=motorConfig)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MotionApi->config_motors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **motorConfig** | [**MotorConfig**](MotorConfig.md)| Specify the position and the speed to move AXIBO | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_motion_status**
> InlineResponse200 get_motion_status()

Move AXIBO to relative position

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MotionApi()

try:
    # Move AXIBO to relative position
    api_response = api_instance.get_motion_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MotionApi->get_motion_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_absolute**
> ApiResponse move_absolute(motorConfig=motorConfig)

Move AXIBO to absolute position

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MotionApi()
motorConfig = swagger_client.ControlCMD() # ControlCMD | Specify the position and the speed to move AXIBO (optional)

try:
    # Move AXIBO to absolute position
    api_response = api_instance.move_absolute(motorConfig=motorConfig)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MotionApi->move_absolute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **motorConfig** | [**ControlCMD**](ControlCMD.md)| Specify the position and the speed to move AXIBO | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_relative**
> ApiResponse move_relative(motorConfig=motorConfig)

Move AXIBO to relative position

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MotionApi()
motorConfig = swagger_client.ControlCMD() # ControlCMD | Specify the position and the speed to move AXIBO (optional)

try:
    # Move AXIBO to relative position
    api_response = api_instance.move_relative(motorConfig=motorConfig)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MotionApi->move_relative: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **motorConfig** | [**ControlCMD**](ControlCMD.md)| Specify the position and the speed to move AXIBO | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_homing**
> ApiResponse set_homing(motorConfig=motorConfig)

Home AXIBO to set defualt limits

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MotionApi()
motorConfig = swagger_client.MotorHome() # MotorHome | Home AXIBO motors (optional)

try:
    # Home AXIBO to set defualt limits
    api_response = api_instance.set_homing(motorConfig=motorConfig)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MotionApi->set_homing: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **motorConfig** | [**MotorHome**](MotorHome.md)| Home AXIBO motors | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

