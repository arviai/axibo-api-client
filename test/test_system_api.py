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
from swagger_client.api.system_api import SystemApi  # noqa: E501
from swagger_client.rest import ApiException


class TestSystemApi(unittest.TestCase):
    """SystemApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.system_api.SystemApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_wifi(self):
        """Test case for delete_wifi

        Delete WIFI network from the saved list  # noqa: E501
        """
        pass

    def test_get_current_wifi(self):
        """Test case for get_current_wifi

        Retreive AXIBO current wifi connection  # noqa: E501
        """
        pass

    def test_get_progress(self):
        """Test case for get_progress

        Retreive the entire status of AXIBO  # noqa: E501
        """
        pass

    def test_list_wifis(self):
        """Test case for list_wifis

        List all the available and saved WIFIs connections  # noqa: E501
        """
        pass

    def test_set_wifi(self):
        """Test case for set_wifi

        Connect to WIFI network  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
