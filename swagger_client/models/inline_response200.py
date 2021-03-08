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


class InlineResponse200(object):
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
        'pan_homed': 'bool',
        'tilt_homed': 'bool',
        'pan_pos': 'int',
        'tilt_pos': 'int'
    }

    attribute_map = {
        'pan_homed': 'panHomed',
        'tilt_homed': 'tiltHomed',
        'pan_pos': 'panPos',
        'tilt_pos': 'tiltPos'
    }

    def __init__(self, pan_homed=None, tilt_homed=None, pan_pos=None, tilt_pos=None):  # noqa: E501
        """InlineResponse200 - a model defined in Swagger"""  # noqa: E501

        self._pan_homed = None
        self._tilt_homed = None
        self._pan_pos = None
        self._tilt_pos = None
        self.discriminator = None

        if pan_homed is not None:
            self.pan_homed = pan_homed
        if tilt_homed is not None:
            self.tilt_homed = tilt_homed
        if pan_pos is not None:
            self.pan_pos = pan_pos
        if tilt_pos is not None:
            self.tilt_pos = tilt_pos

    @property
    def pan_homed(self):
        """Gets the pan_homed of this InlineResponse200.  # noqa: E501


        :return: The pan_homed of this InlineResponse200.  # noqa: E501
        :rtype: bool
        """
        return self._pan_homed

    @pan_homed.setter
    def pan_homed(self, pan_homed):
        """Sets the pan_homed of this InlineResponse200.


        :param pan_homed: The pan_homed of this InlineResponse200.  # noqa: E501
        :type: bool
        """

        self._pan_homed = pan_homed

    @property
    def tilt_homed(self):
        """Gets the tilt_homed of this InlineResponse200.  # noqa: E501


        :return: The tilt_homed of this InlineResponse200.  # noqa: E501
        :rtype: bool
        """
        return self._tilt_homed

    @tilt_homed.setter
    def tilt_homed(self, tilt_homed):
        """Sets the tilt_homed of this InlineResponse200.


        :param tilt_homed: The tilt_homed of this InlineResponse200.  # noqa: E501
        :type: bool
        """

        self._tilt_homed = tilt_homed

    @property
    def pan_pos(self):
        """Gets the pan_pos of this InlineResponse200.  # noqa: E501


        :return: The pan_pos of this InlineResponse200.  # noqa: E501
        :rtype: int
        """
        return self._pan_pos

    @pan_pos.setter
    def pan_pos(self, pan_pos):
        """Sets the pan_pos of this InlineResponse200.


        :param pan_pos: The pan_pos of this InlineResponse200.  # noqa: E501
        :type: int
        """

        self._pan_pos = pan_pos

    @property
    def tilt_pos(self):
        """Gets the tilt_pos of this InlineResponse200.  # noqa: E501


        :return: The tilt_pos of this InlineResponse200.  # noqa: E501
        :rtype: int
        """
        return self._tilt_pos

    @tilt_pos.setter
    def tilt_pos(self, tilt_pos):
        """Sets the tilt_pos of this InlineResponse200.


        :param tilt_pos: The tilt_pos of this InlineResponse200.  # noqa: E501
        :type: int
        """

        self._tilt_pos = tilt_pos

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
        if issubclass(InlineResponse200, dict):
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
        if not isinstance(other, InlineResponse200):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other