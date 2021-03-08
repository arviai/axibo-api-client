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


class ControlCMDPosition(object):
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
        'pan': 'list[float]',
        'tilt': 'list[float]'
    }

    attribute_map = {
        'pan': 'pan',
        'tilt': 'tilt'
    }

    def __init__(self, pan=None, tilt=None):  # noqa: E501
        """ControlCMDPosition - a model defined in Swagger"""  # noqa: E501

        self._pan = None
        self._tilt = None
        self.discriminator = None

        if pan is not None:
            self.pan = pan
        if tilt is not None:
            self.tilt = tilt

    @property
    def pan(self):
        """Gets the pan of this ControlCMDPosition.  # noqa: E501


        :return: The pan of this ControlCMDPosition.  # noqa: E501
        :rtype: list[float]
        """
        return self._pan

    @pan.setter
    def pan(self, pan):
        """Sets the pan of this ControlCMDPosition.


        :param pan: The pan of this ControlCMDPosition.  # noqa: E501
        :type: list[float]
        """

        self._pan = pan

    @property
    def tilt(self):
        """Gets the tilt of this ControlCMDPosition.  # noqa: E501


        :return: The tilt of this ControlCMDPosition.  # noqa: E501
        :rtype: list[float]
        """
        return self._tilt

    @tilt.setter
    def tilt(self, tilt):
        """Sets the tilt of this ControlCMDPosition.


        :param tilt: The tilt of this ControlCMDPosition.  # noqa: E501
        :type: list[float]
        """

        self._tilt = tilt

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
        if issubclass(ControlCMDPosition, dict):
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
        if not isinstance(other, ControlCMDPosition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
