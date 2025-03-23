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

from gencove_client.api.upload_api import UploadApi


class TestUploadApi(unittest.TestCase):
    """UploadApi unit test stubs"""

    def setUp(self) -> None:
        self.api = UploadApi()

    def tearDown(self) -> None:
        pass

    def test_upload_credentials_create(self) -> None:
        """Test case for upload_credentials_create"""
        pass

    def test_uploads_delete_unassigned_create(self) -> None:
        """Test case for uploads_delete_unassigned_create"""
        pass

    def test_uploads_list(self) -> None:
        """Test case for uploads_list"""
        pass

    def test_uploads_post_data_create(self) -> None:
        """Test case for uploads_post_data_create"""
        pass

    def test_uploads_presigned_post_data_create(self) -> None:
        """Test case for uploads_presigned_post_data_create"""
        pass

    def test_uploads_read(self) -> None:
        """Test case for uploads_read"""
        pass

    def test_uploads_url_create(self) -> None:
        """Test case for uploads_url_create"""
        pass


if __name__ == "__main__":
    unittest.main()
