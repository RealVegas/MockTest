from main import get_dog_picture


def test_picture_success(mocker) -> None:
    mock_get = mocker.patch('main.requests.get')

    # Успешный ответ с корректной структурой
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [{'url': 'https://cdn2.thedogapi.com/images/ZRQ0TYzz6.jpg'}]

    dog_picture = get_dog_picture()
    assert dog_picture == 'https://cdn2.thedogapi.com/images/ZRQ0TYzz6.jpg'


def test_picture_failure(mocker) -> None:
    mock_get = mocker.patch('main.requests.get')

    mock_get.return_value.status_code = 404
    mock_get.return_value.json.return_value = []

    dog_picture = get_dog_picture()
    assert dog_picture is None