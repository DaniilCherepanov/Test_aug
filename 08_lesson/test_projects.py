import pytest
import requests
import json
import uuid

BASE_URL = "https://ru.yougile.com/api-v2"

VALID_USERNAME = "ВАШ ЛОГИН"
VALID_PASSWORD = "ВАШ ПАРОЛЬ"
COMPANY_ID = "fa604740-0963-44e2-b73f-60238507570b"

AUTH_KEY = None

def get_auth_key():
    global AUTH_KEY
    if AUTH_KEY is None:
        url = f"{BASE_URL}/auth/keys"
        data = {
            "login": VALID_USERNAME,
            "password": VALID_PASSWORD,
            "companyId": COMPANY_ID
        }
        headers = {"Content-Type": "application/json"}
        try:
            response = requests.post(url, headers=headers, json=data)
            if response.status_code == 201:
                AUTH_KEY = response.json().get("key")
            else:
                raise Exception(f"Ошибка получения ключа: {response.status_code} - {response.text}")
        except Exception as e:
            raise Exception(f"Произошла ошибка: {e}")
    return AUTH_KEY

@pytest.fixture
def valid_headers():
    key = get_auth_key()
    return {
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json"
    }

@pytest.fixture
def invalid_headers():
    return {
        "Authorization": "Bearer invalid_token",
        "Content-Type": "application/json"
    }

def test_create_project_positive(valid_headers):
    valid_user_id = "a3d34a2d-0600-4fb5-b2c2-ee079ec0a51c"
    payload = {
        "title": f"Тестовый проект {uuid.uuid4()}",
        "users": {valid_user_id: "worker"}
    }

    response = requests.post(f"{BASE_URL}/projects", headers=valid_headers, json=payload)
    assert response.status_code == 201
    data = response.json()
    assert 'id' in data
    assert data['title'] == payload['title']

def test_create_project_invalid_token(invalid_headers):
    payload = {
        "title": "Некорректный проект",
        "users": {}
    }

    response = requests.post(f"{BASE_URL}/projects", headers=invalid_headers, json=payload)
    assert response.status_code == 401
    assert response.json().get("error") is not None


def test_update_project_positive(valid_headers):
    valid_user_id = "a3d34a2d-0600-4fb5-b2c2-ee079ec0a51c"
    create_payload = {
        "title": f"Проект для обновления {uuid.uuid4()}",
        "users": {valid_user_id: "worker"}
    }
    create_response = requests.post(f"{BASE_URL}/projects", headers=valid_headers, json=create_payload)
    project_id = create_response.json()['id']

    update_payload = {
        "title": f"Обновлённый проект {uuid.uuid4()}",
        "users": {valid_user_id: "worker"}
    }
    response = requests.put(f"{BASE_URL}/projects/{project_id}", headers=valid_headers, json=update_payload)
    assert response.status_code == 200
    assert response.json()['id'] == project_id
    assert response.json()['title'] == update_payload['title']

def test_update_project_invalid_id(valid_headers):
    invalid_id = "invalid_id"
    payload = {
        "title": "Некорректный проект",
        "users": {}
    }

    response = requests.put(f"{BASE_URL}/projects/{invalid_id}", headers=valid_headers, json=payload)
    assert response.status_code == 404
    assert response.json().get("error") == "Проект не найден"

def test_get_project_by_id(valid_headers):
    valid_user_id = "a3d34a2d-0600-4fb5-b2c2-ee079ec0a51c"
    payload = {
        "title": f"Проект для получения {uuid.uuid4()}",
        "users": {valid_user_id: "worker"}
    }
    create_response = requests.post(f"{BASE_URL}/projects", headers=valid_headers, json=payload)
    project_id = create_response.json()['id']

    response = requests.get(f"{BASE_URL}/projects/{project_id}", headers=valid_headers)
    assert response.status_code == 200
    data = response.json()
    assert data['id'] == project_id
    assert data['title'] == payload['title']

def test_get_project_by_invalid_id(valid_headers):
    invalid_id = "invalid_id"
    response = requests.get(f"{BASE_URL}/projects/{invalid_id}", headers=valid_headers)
    assert response.status_code == 404
    assert response.json().get("error") == "Проект не найден"
