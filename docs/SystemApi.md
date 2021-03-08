# swagger_client.SystemApi

All URIs are relative to *http://10.42.0.1:2200*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_wifi**](SystemApi.md#delete_wifi) | **DELETE** /system/wifi | Delete WIFI network from the saved list
[**get_current_wifi**](SystemApi.md#get_current_wifi) | **GET** /system/wifiInfo | Retreive AXIBO current wifi connection
[**get_progress**](SystemApi.md#get_progress) | **GET** /system/status | Retreive the entire status of AXIBO
[**list_wifis**](SystemApi.md#list_wifis) | **GET** /system/wifi | List all the available and saved WIFIs connections
[**set_wifi**](SystemApi.md#set_wifi) | **PUT** /system/wifi | Connect to WIFI network


# **delete_wifi**
> ApiResponse delete_wifi(wifi_name=wifi_name)

Delete WIFI network from the saved list



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SystemApi()
wifi_name = swagger_client.WifiName() # WifiName | Status object that needs to be added to the database (optional)

try:
    # Delete WIFI network from the saved list
    api_response = api_instance.delete_wifi(wifi_name=wifi_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->delete_wifi: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wifi_name** | [**WifiName**](WifiName.md)| Status object that needs to be added to the database | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_wifi**
> Wifi get_current_wifi()

Retreive AXIBO current wifi connection

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SystemApi()

try:
    # Retreive AXIBO current wifi connection
    api_response = api_instance.get_current_wifi()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->get_current_wifi: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Wifi**](Wifi.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_progress**
> SystemMsg get_progress()

Retreive the entire status of AXIBO



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SystemApi()

try:
    # Retreive the entire status of AXIBO
    api_response = api_instance.get_progress()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->get_progress: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SystemMsg**](SystemMsg.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_wifis**
> WifiList list_wifis()

List all the available and saved WIFIs connections

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SystemApi()

try:
    # List all the available and saved WIFIs connections
    api_response = api_instance.list_wifis()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->list_wifis: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WifiList**](WifiList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_wifi**
> ApiResponse set_wifi(wifi_config=wifi_config)

Connect to WIFI network



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SystemApi()
wifi_config = swagger_client.ConnectWifi() # ConnectWifi | BSSID, SSID, and Password (optional)

try:
    # Connect to WIFI network
    api_response = api_instance.set_wifi(wifi_config=wifi_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->set_wifi: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wifi_config** | [**ConnectWifi**](ConnectWifi.md)| BSSID, SSID, and Password | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

