import unittest
from mock import patch
import requests
from pyrest_client.rest_client import RestClient, _Executable, _Callable


class RestClientTestCases(unittest.TestCase):
    def setUp(self):
        self.root_url = "http://test.com/api/v2"
        self.rest_client = RestClient(self.root_url)

    def test_returns_builtin_attr(self):
        result = self.rest_client.__str__
        self.assertEqual(result(), RestClient.__str__(self.rest_client))

    def test_returns_custom_attr(self):
        result = self.rest_client.some_attr
        self.assertTrue(isinstance(result, _Callable))

    def test_returns_generated_url(self):
        result = self.rest_client.users.show.generate_url()
        self.assertEqual("http://test.com/api/v2/users/show", result)

    def test_returns_meaningful_string_when_its_callable_object(self):
        callable_object = self.rest_client.users.show
        result = str(callable_object)
        self.assertEqual(result, '_Callable (%s)' % callable_object.generate_url())

    def test_returns_meaningful_string_when_its_executable_object(self):
        callable_object = self.rest_client.users.show.get
        result = str(callable_object)
        expected_result = '_Executable (get http://test.com/api/v2/users/show)'
        self.assertEqual(result, expected_result)

    @patch.object(_Executable, '_make_request')
    def test_call_service_with_get_method(self, mock_call_service):
        mock_call_service.return_value = 'test response'

        result = self.rest_client.users.show.matt.get()

        called_url = "http://test.com/api/v2/users/show/matt"
        mock_call_service.assert_called_once_with(called_url, 'get')
        self.assertEqual(result, 'test response')

    @patch.object(_Executable, '_make_request')
    def test_call_service_with_post_method(self, mock_call_service):
        mock_call_service.return_value = 'test response'
        post_data = {'user': 'matt'}
        result = self.rest_client.users.post(data=post_data)

        called_url = "http://test.com/api/v2/users"
        mock_call_service.assert_called_once_with(called_url, 'post', data=post_data)
        self.assertEqual(result, 'test response')

    @patch.object(requests, 'get')
    def test_should_call_requests_with_right_method(self, mock_requests):
        mock_requests.return_value = 'test response'

        result = self.rest_client.users.show.get()

        called_url = "http://test.com/api/v2/users/show"
        self.assertEqual(result, 'test response')
        mock_requests.assert_called_once_with(called_url)

