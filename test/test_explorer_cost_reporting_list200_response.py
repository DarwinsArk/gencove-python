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

from gencove_client.models.explorer_cost_reporting_list200_response import ExplorerCostReportingList200Response


class TestExplorerCostReportingList200Response(unittest.TestCase):
    """ExplorerCostReportingList200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ExplorerCostReportingList200Response:
        """Test ExplorerCostReportingList200Response
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ExplorerCostReportingList200Response`
        """
        model = ExplorerCostReportingList200Response()
        if include_optional:
            return ExplorerCostReportingList200Response(
                meta = gencove_client.models.basespace_project_biosamples_read_200_response_meta.basespace_project_biosamples_read_200_response_meta(
                    count = 56,
                    next = '',
                    previous = '', ),
                results = [
                    gencove_client.models.explorer_cost_report_record.ExplorerCostReportRecord(
                        id = '',
                        start_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                        end_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                        report_amount = '',
                        is_current_report = '',
                        report_is_finalized = True,
                        last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                        files = [
                            gencove_client.models.file_nested.FileNested(
                                id = '',
                                s3_path = '',
                                size = -9223372036854775808,
                                download_url = '',
                                file_type = '',
                                checksum_sha256 = '',
                                shadow_mode = True, )
                            ], )
                    ]
            )
        else:
            return ExplorerCostReportingList200Response(
                results = [
                    gencove_client.models.explorer_cost_report_record.ExplorerCostReportRecord(
                        id = '',
                        start_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                        end_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                        report_amount = '',
                        is_current_report = '',
                        report_is_finalized = True,
                        last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                        files = [
                            gencove_client.models.file_nested.FileNested(
                                id = '',
                                s3_path = '',
                                size = -9223372036854775808,
                                download_url = '',
                                file_type = '',
                                checksum_sha256 = '',
                                shadow_mode = True, )
                            ], )
                    ],
        )
        """

    def testExplorerCostReportingList200Response(self):
        """Test ExplorerCostReportingList200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
