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

from gencove_client.models.user_api_keys_list200_response import UserApiKeysList200Response


class TestUserApiKeysList200Response(unittest.TestCase):
    """UserApiKeysList200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserApiKeysList200Response:
        """Test UserApiKeysList200Response
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `UserApiKeysList200Response`
        """
        model = UserApiKeysList200Response()
        if include_optional:
            return UserApiKeysList200Response(
                meta = gencove_client.models.basespace_project_biosamples_read_200_response_meta.basespace_project_biosamples_read_200_response_meta(
                    count = 56,
                    next = '',
                    previous = '', ),
                results = [
                    gencove_client.models.api_key.APIKey(
                        revoked = True,
                        id = '0',
                        name = '0',
                        prefix = '0',
                        expiry_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                        has_expired = '',
                        ip_range = gencove_client.models.ip_range.Ip range(), )
                    ]
            )
        else:
            return UserApiKeysList200Response(
                results = [
                    gencove_client.models.api_key.APIKey(
                        revoked = True,
                        id = '0',
                        name = '0',
                        prefix = '0',
                        expiry_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                        has_expired = '',
                        ip_range = gencove_client.models.ip_range.Ip range(), )
                    ],
        )
        """

    def testUserApiKeysList200Response(self):
        """Test UserApiKeysList200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
