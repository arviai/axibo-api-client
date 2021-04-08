from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
from configuration import Configuration
# create an instance of the API class
config=Configuration()
api_instance = swagger_client.SystemApi(swagger_client.ApiClient(config))
try:
    # Retrives an pose overlay image with a timestamp
    api_response = api_instance.list_wifis()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->get_pose_image: %s\n" % e)
