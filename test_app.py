import pytest
import requests

def test_home():
    response = requests.get("http://127.0.0.1:5000/")
    assert response.status_code == 200
    assert response.json()["message"] == "Witaj w moim API!"

def test_moja_strona():
    response = requests.get("http://127.0.0.1:5000/mojastrona")
    assert response.status_code == 200
    assert response.json()["message"] == "To jest moja strona!"

