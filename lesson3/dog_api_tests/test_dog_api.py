import pytest
import requests


def test_random_img():
    """
    Метод:https://dog.ceo/api/breeds/image/random
    Проверка различия выдаваемых URL  функцией random
    """
    r = requests.get('https://dog.ceo/api/breeds/image/random')
    j = r.json()
    msg1 = j['message']
    r = requests.get('https://dog.ceo/api/breeds/image/random')
    j = r.json()
    msg2 = j['message']
    assert not (msg1 == msg2)


def test_success_reply():
    """
        Метод:https://dog.ceo/api/breeds/image/random
        Проверка статуса кода на метод рандомного  изображения и содержания в ответе success
        """
    r = requests.get('https://dog.ceo/api/breeds/image/random')
    j = r.json()
    status = j['status']
    assert status == "success"
    assert r.status_code == 200


@pytest.mark.parametrize("test_input", ["terrier", "pointer", "hound", "spaniel"])
class Test_with_breed:

    # Все функци должны использовать аргумент
    def test_img_by_breed(self, test_input):
        """
        Пример Запроса:https://dog.ceo/api/breed/hound/images
        Проверка соответствия выборки изображений согласно породе ..
        :param test_input:
        """
        url = "https://dog.ceo/api/breed/" + test_input + "/images"
        r = requests.get(url)
        img = r.json()['message']
        errors = 0
        for i in img:
            if not (test_input in i):
                print(test_input + " == " + i)
                errors += 1
        assert errors == 0

    def test_random_img_by_breed(self, test_input):
        """
        Пример Запроса:https://dog.ceo/api/breed/hound/images/random
        Проверка соответствия рандомного изображения согласно породе ..
        :param test_input:
        """
        url = "https://dog.ceo/api/breed/" + test_input + "/images/random"
        r = requests.get(url)
        img = r.json()['message']
        assert test_input in img

    def test_random_count(self, test_input, p_number):
        """
        Пример Запроса:https://dog.ceo/api/breed/hound/images/random/3
        Проверка количества выдаваемых изображений
        :param test_input:
        """
        url = "https://dog.ceo/api/breed/" + test_input + "/images/random/" + p_number
        r = requests.get(url)
        img = r.json()['message']
        assert len(img) == int(p_number)
