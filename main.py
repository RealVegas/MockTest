import requests


def get_dog_picture() -> str | None:

    pic_url: str = 'https://api.thedogapi.com/v1/images/search'
    response: requests = requests.get(pic_url)

    if response.status_code == 200:
        return response.json()[0]['url']
    else:
        return None


if __name__ == '__main__':
     print(get_dog_picture())