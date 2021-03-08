# coding: utf-8

"""
    AXIBO OPENSOURCE API

    No description provided   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: contact@axibo.com
    
"""


import pprint
import re  # noqa: F401

import six


class ImageRes(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'timestamp': 'int',
        'image': 'str'
    }

    attribute_map = {
        'timestamp': 'timestamp',
        'image': 'image'
    }

    def __init__(self, timestamp=None, image=None):  # noqa: E501
        """ImageRes - a model defined in Swagger"""  # noqa: E501

        self._timestamp = None
        self._image = None
        self.discriminator = None

        if timestamp is not None:
            self.timestamp = timestamp
        if image is not None:
            self.image = image

    @property
    def timestamp(self):
        """Gets the timestamp of this ImageRes.  # noqa: E501


        :return: The timestamp of this ImageRes.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this ImageRes.


        :param timestamp: The timestamp of this ImageRes.  # noqa: E501
        :type: int
        """

        self._timestamp = timestamp

    @property
    def image(self):
        """Gets the image of this ImageRes.  # noqa: E501


        :return: The image of this ImageRes.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this ImageRes.


        :param image: The image of this ImageRes.  # noqa: E501
        :type: str
        """

        self._image = image

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ImageRes, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ImageRes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
