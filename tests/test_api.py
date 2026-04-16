import unittest

from api import create_app


class TestApi(unittest.TestCase):
    def setUp(self):
        self.client = create_app().test_client()

    def test_health(self):
        response = self.client.get('/health')
        self.assertEqual(response.status_code, 200)

    def test_predict_invalid_steps(self):
        response = self.client.get('/predict?steps=0')
        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()
