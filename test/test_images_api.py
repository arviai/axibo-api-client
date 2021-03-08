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
from swagger_client.api.images_api import ImagesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestImagesApi(unittest.TestCase):
    """ImagesApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.images_api.ImagesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_pose_image(self):
        """Test case for get_pose_image

        Retrives an pose overlay image with a timestamp  # noqa: E501
        """
        pass

    def test_get_raw_image(self):
        """Test case for get_raw_image

        Retrives a raw image with a timestamp  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
