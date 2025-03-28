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

from gencove_client.api.jwt_api import JwtApi


class TestJwtApi(unittest.TestCase):
    """JwtApi unit test stubs"""

    def setUp(self) -> None:
        self.api = JwtApi()

    def tearDown(self) -> None:
        pass

    def test_jwt_create_create(self) -> None:
        """Test case for jwt_create_create"""
        pass

    def test_jwt_logout_create(self) -> None:
        """Test case for jwt_logout_create"""
        pass

    def test_jwt_refresh_create(self) -> None:
        """Test case for jwt_refresh_create"""
        pass

    def test_jwt_verify_create(self) -> None:
        """Test case for jwt_verify_create"""
        pass


if __name__ == "__main__":
    unittest.main()
