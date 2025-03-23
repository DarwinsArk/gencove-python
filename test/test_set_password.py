# coding: utf-8

"""
    Gencove Back API

    API for Gencove REST service. Visit <a href='https://gencove.com/'>gencove.com</a> and <a href='https://docs.gencove.com/'>docs.gencove.com</a> for more information. <br><hr><p>To work with Insomnia, you can generate a Gencove API key by <a target='_blank' href='https://web.gencove.com/account?filter=api-keys'>clicking here</a>. Once you have the API key and have imported the project in Insomnia as a <i>Request Collection</i>, enter the key in Insomnia under <i>Manage Environment</i>.</p><a href='https://insomnia.rest/run/?label=back_api2&uri=https%3A%2F%2Fv2-api-files-prod.s3.amazonaws.com%2Fpublic%2Finsomnia%2Finsomnia_gencove_prod.json' target='_blank'>Run in Insomnia</a><hr>

    The version of the OpenAPI document: v2
    Contact: info@gencove.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from gencove_client.models.set_password import SetPassword


class TestSetPassword(unittest.TestCase):
    """SetPassword unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SetPassword:
        """Test SetPassword
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `SetPassword`
        """
        model = SetPassword()
        if include_optional:
            return SetPassword(
                new_password = '0',
                current_password = '0'
            )
        else:
            return SetPassword(
                new_password = '0',
                current_password = '0',
        )
        """

    def testSetPassword(self):
        """Test SetPassword"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
