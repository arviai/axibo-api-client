# coding: utf-8

"""
    AXIBO OPENSOURCE API

    No description provided   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: contact@axibo.com
    
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.motion_api import MotionApi  # noqa: E501
from swagger_client.rest import ApiException


class TestMotionApi(unittest.TestCase):
    """MotionApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.motion_api.MotionApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_config_motors(self):
        """Test case for config_motors

        Move AXIBO to relative position  # noqa: E501
        """
        pass

    def test_get_motion_status(self):
        """Test case for get_motion_status

        Move AXIBO to relative position  # noqa: E501
        """
        pass

    def test_move_absolute(self):
        """Test case for move_absolute

        Move AXIBO to absolute position  # noqa: E501
        """
        pass

    def test_move_relative(self):
        """Test case for move_relative

        Move AXIBO to relative position  # noqa: E501
        """
        pass

    def test_set_homing(self):
        """Test case for set_homing

        Home AXIBO to set defualt limits  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
