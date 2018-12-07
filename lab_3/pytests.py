import pytest
import requests


def test_root():
    test = requests.get('http://127.0.0.1:5000/')
    test.raise_for_status()
    assert test.status_code == 200
    assert not test.is_redirect


def test_fail():
    test = requests.get('http://127.0.0.1:5000/some')
    assert test.status_code == 404
    assert not test.is_redirect


def test_register():
    test = requests.post('http://127.0.0.1:5000/register', data=({'password': '123456',
                                                                  'email': 'danik@gmail.com',
                                                                  'username': 'Danylo Zasymenko'}))
    test.raise_for_status()
    assert test.status_code == 200
    assert test.text


def test_logout():
    test = requests.get('http://127.0.0.1:5000/logout')
    test.raise_for_status()
    assert test.status_code == 200


def test_good_delete():
    test = requests.get('http://127.0.0.1:5000/good-delete', data=({'good_id': 1}))
    test.raise_for_status()
    assert test.status_code == 200


def test_account():
    test = requests.post('http://127.0.0.1:5000/account', data=({'email': 'danik@gmail.com',
                                                                  'username': 'Danylo Zasymenko'}))
    test.raise_for_status()
    assert test.status_code == 200


def test_login():
    test = requests.post('http://127.0.0.1:5000/login', data=({'username': 'Danylo Zasymenko',
                                                               'password': '123456'}))
    test.raise_for_status()
    assert test.status_code == 200
