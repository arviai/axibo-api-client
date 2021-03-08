# swagger_client.ImagesApi

All URIs are relative to *http://10.42.0.1:2200*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_pose_image**](ImagesApi.md#get_pose_image) | **GET** /imaging/pose | Retrives an pose overlay image with a timestamp
[**get_raw_image**](ImagesApi.md#get_raw_image) | **GET** /imaging/cam | Retrives a raw image with a timestamp


# **get_pose_image**
> ImageRes get_pose_image()

Retrives an pose overlay image with a timestamp

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()

try:
    # Retrives an pose overlay image with a timestamp
    api_response = api_instance.get_pose_image()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->get_pose_image: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ImageRes**](ImageRes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_raw_image**
> ImageRes get_raw_image()

Retrives a raw image with a timestamp

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ImagesApi()

try:
    # Retrives a raw image with a timestamp
    api_response = api_instance.get_raw_image()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->get_raw_image: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ImageRes**](ImageRes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

