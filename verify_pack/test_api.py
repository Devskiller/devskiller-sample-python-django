from http import HTTPStatus


def test_add(client):
    a, b, = 1, 2
    response = client.get(f'/add/{a}/{b}/')
    assert response.status_code == HTTPStatus.OK
    assert response.json()['result'] == a + b


def test_subtract(client):
    a, b, = 5, 3
    response = client.get(f'/subtract/{a}/{b}/')
    assert response.status_code == HTTPStatus.OK
    assert response.json()['result'] == a - b


def test_multiply(client):
    a, b, = 2, 3
    response = client.get(f'/multiply/{a}/{b}/')
    assert response.status_code == HTTPStatus.OK
    assert response.json()['result'] == a * b


def test_divide(client):
    a, b, = 6, 2
    response = client.get(f'/divide/{a}/{b}/')
    assert response.status_code == HTTPStatus.OK
    assert response.json()['result'] == a / b


def test_divide_by_zero(client):
    a, b, = 1, 0
    response = client.get(f'/divide/{a}/{b}/')
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json()['error'] == "Division by zero!"
