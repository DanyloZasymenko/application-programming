import unittest

import requests


class FlaskTestCase(unittest.TestCase):

    def test_root(self):
        test = requests.get('http://127.0.0.1:5000/')
        return self.assertEqual(test.status_code, 200)

    def test_fail(self):
        test = requests.get('http://127.0.0.1:5000/some')
        return self.assertEqual(test.status_code, 404)

    def test_register(self):
        test = requests.post('http://127.0.0.1:5000/register', data=({'password': '123456',
                                                                      'email': 'danik@gmail.com',
                                                                      'username': 'Danylo Zasymenko'}))
        return self.assertEqual(test.status_code, 200)

    def test_logout(self):
        test = requests.get('http://127.0.0.1:5000/logout')
        return self.assertEqual(test.status_code, 200)

    def test_good_delete(self):
        test = requests.get('http://127.0.0.1:5000/good-delete', data=({'good_id': 1}))
        return self.assertEqual(test.status_code, 200)

    def test_account(self):
        test = requests.post('http://127.0.0.1:5000/account', data=({'email': 'danik@gmail.com',
                                                                     'username': 'Danylo Zasymenko'}))
        return self.assertEqual(test.status_code, 200)

    def test_login(self):
        test = requests.post('http://127.0.0.1:5000/login', data=({'username': 'Danylo Zasymenko',
                                                                   'password': '123456'}))
        return self.assertEqual(test.status_code, 200)


if __name__ == '__main__':
    unittest.main()
