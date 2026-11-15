import pytest

from app import app


@pytest.mark.parametrize(
    ("query", "expected"),
    [
        ({}, "Hello World!"),
        ({"name": "Ana"}, "Hello Ana!"),
        ({"name": "María López"}, "Hello María López!"),
        ({"name": ""}, "Hello !"),
        ({"name": "<b>Ana</b>"}, "Hello <b>Ana</b>!"),
    ],
)
def test_greet(query, expected):
    with app.test_client() as client:
        response = client.get("/greet", query_string=query)

    assert response.status_code == 200
    assert response.mimetype == "text/plain"
    assert response.get_data(as_text=True) == expected
