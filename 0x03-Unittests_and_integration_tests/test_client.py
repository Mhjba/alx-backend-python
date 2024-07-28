#!/usr/bin/env python3
"""Test for the clinet module"""
import unittest
from unittest.mock import PropertyMock, patch
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
from unittest.mock import patch
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Tests the `GithubOrgClient` class."""

    @parameterized.expand(
        [
            ("google", {"org": "google"}),
            ("abc", {"org": "abc"}),
        ]
    )
    @patch("client.get_json")
    def test_org(self, org_name, output, mock_get_json) -> None:
        """Tests the `org` method."""
        test = GithubOrgClient(org_name)
        mock_get_json.return_value = output
        self.assertEqual(output, test.org)
        mock_get_json.assert_called_once()

    @patch("client.get_json")
    def test_public_repos_url(self, mock_get_json) -> None:
        """Tests the `_public_repos_url` property."""
        tests = GithubOrgClient("test")
        output = {"repos_url": "www.test.com"}
        mock_get_json.return_value = output
        self.assertEqual(tests._public_repos_url, output["repos_url"])

    @patch("client.get_json")
    def test_public_repos(self, mock_public_repos_url, mock_get_json) -> None:
        """Tests the `public_repos` method."""
        test = GithubOrgClient("test")
        mock_public_repos_url.return_value = "www.test.com"
        lis = {"repos": ["r1", "r2", "r3", "...etc"]}
        mock_get_json.return_value = lis
        self.assertEqual(test.repos_payload, lis)
        mock_get_json.assert_called_once()

    @parameterized.expand(
        [
            ({"license": {"key": "my_license"}}, "my_license", True),
            ({"license": {"key": "other_license"}}, "my_license", False),
        ]
    )
    def test_has_license(self, repo, license_key, output) -> None:
        """Tests the `has_license` method."""
        license = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(license, output)


class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration test for GithubOrgClient
    """

    class setUpClass:
        """
        Set up class for integration test
        """

        @patch("client.get_json")
        def setUp(self, mock_get_json):
            """
            Set up method for class
            """
            self.test_class = GithubOrgClient("test")
            self.org_payload = {"repos_url": "www.test.com"}
            self.repos_payload = [
                {"name": "repo1", "license": {"key": "my_license"}},
                {"name": "repo2", "license": {"key": "other_license"}},
            ]
            mock_get_json.side_effect = [
                self.org_payload,
                self.repos_payload,
            ]


@parameterized_class(

    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Performs integration tests for the `GithubOrgClient` class."""

    @classmethod
    def setUpClass(cls) -> None:
        """Sets up class fixtures before running tests."""
        r_payload = {
            "return_value.json.side_effect": [
                cls.org_payload,
                cls.repos_payload,
                cls.org_payload,
                cls.repos_payload,
            ]
        }
        cls.get_patcher = patch("requests.get", **r_payload)

        cls.mock = cls.get_patcher.start()

    def test_public_repos(self) -> None:
        """Tests the `public_repos` method."""
        self.assertEqual(
            GithubOrgClient("google").public_repos(),
            self.expected_repos,
        )


    def test_public_repos_with_license(self) -> None:
        """Tests the `public_repos` method with a license."""
        self.assertEqual(
            GithubOrgClient("google").public_repos(license="apache-2.0"),
            self.apache2_repos,
        )

    @classmethod
    def tearDownClass(cls) -> None:
        """Removes the class fixtures after running all tests."""
        cls.get_patcher.stop()
