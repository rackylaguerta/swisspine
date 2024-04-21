import unittest
from app import app

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_mirror_word(self):
        # Test with a word 'hello'
        response = self.app.get('/api/mirror?word=hello')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'OLLEH')

        # Test with an empty word
        response = self.app.get('/api/mirror')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'Please provide a word to mirror.')

if __name__ == '__main__':
    unittest.main()
