# coding: utf-8

# flake8: noqa

"""
    AXIBO OPENSOURCE API

    No description provided   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: contact@axibo.com
    
"""


from __future__ import absolute_import

# import apis into sdk package
from swagger_client.api.images_api import ImagesApi
from swagger_client.api.motion_api import MotionApi
from swagger_client.api.system_api import SystemApi

# import ApiClient
from swagger_client.api_client import ApiClient
from swagger_client.configuration import Configuration
# import models into sdk package
from swagger_client.models.api_response import ApiResponse
from swagger_client.models.connect_wifi import ConnectWifi
from swagger_client.models.control_cmd import ControlCMD
from swagger_client.models.control_cmd_position import ControlCMDPosition
from swagger_client.models.errors import Errors
from swagger_client.models.image_res import ImageRes
from swagger_client.models.inline_response200 import InlineResponse200
from swagger_client.models.motor_config import MotorConfig
from swagger_client.models.motor_home import MotorHome
from swagger_client.models.system_msg import SystemMsg
from swagger_client.models.wifi import Wifi
from swagger_client.models.wifi_list import WifiList
from swagger_client.models.wifi_name import WifiName
