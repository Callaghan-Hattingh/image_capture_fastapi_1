from fastapi.testclient import TestClient


def test_tag_creation(client: TestClient):
    response = client.post("/api/tag/", json={"tag": "Pond 1"})
    assert response.status_code == 201
    assert response.json()["tag"] == "Pond 1"
    assert response.json()["id"] == 1


def test_image_creation(client: TestClient):
    filename_1 = "test/test_data/-W1.png"
    filename_2 = "test/test_data/-W2.png"
    files = [
        ("files", ("W1", open(filename_1, "rb"), "image/png")),
        # ("files", ("W2", open(filename_2, "rb"), "image/png")),
    ]
    # print(files)
    response = client.post(
        "/api/image/",
        data={
            "image": "test/test_data/-W1.png",
            "message": "FSU",
        },
        files=files,
    )
    # print(response.json())
    assert True
