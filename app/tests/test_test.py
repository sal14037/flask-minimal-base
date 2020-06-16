import logging
import os
import json
import unittest

from flask_testing import TestCase

from manage import app

class TestAuth(TestCase):

    def create_app(self):
        """
        Instructs Flask to run these commands when we request this group of tests to be run.
        """
        # Sets the configuration of the application to 'TestingConfig' in order
        # that the tests use db_test, not db_dev or db_prod.
        app.config.from_object('config.TestingConfig')

        # Sets the logger to only show ERROR level logs and worse. We don't want
        # to print a million things when running tests.
        # logger.setLevel(logging.ERROR)

        return app

    def setUp(self):
        """Defines what should be done before every single test in this test group."""
        pass

    def tearDown(self):
        """Defines what should be done after every single test in this test group."""
        pass

    def test_health(self):
        """
        Every single test in this test group should be defined as a method of this class.
        """
        with self.client:
            response = self.client.get('/v1/')
            self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
