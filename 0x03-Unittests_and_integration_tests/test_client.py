#!/usr/bin/env python3
"""
This class and implement the test_org method
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')  # Adjust based on where get_json is located
    def test_org(self, org_name, mock_get_json):
        """Test GithubOrgClient.org method"""

        # Define the mock return value
        mock_get_json.return_value = {
            "repos_url": f"https://api.github.com/orgs/{org_name}/repos"
        }

        # Create an instance of GithubOrgClient
        client = GithubOrgClient(org_name)

        # Call the org method
        result = client.org

        # Check that get_json was called once with the expected URL
        expected_url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.assert_called_once_with(expected_url)

        # Check the result returned by the org method
        self.assertEqual(result, mock_get_json.return_value)


if __name__ == "__main__":
    unittest.main()
