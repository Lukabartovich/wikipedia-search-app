import requests
from selectorlib import Extractor
from StringSort import StringSort
import wikipedia


def getting_data(what, split, lang):
    if lang == 'en':
        wikipedia.set_lang('en')
        text = wikipedia.summary(str(what).capitalize())

        s = StringSort(str(text))
        s1 = s.delete('1234567890', ']')
        s2 = StringSort(str(s1))
        s3 = s2.delete('[]')
        s4 = StringSort(s3)
        s5 = s4.split(split)
        s6 = StringSort(s5)
        s7 = s6.delete(' ', ' ')


        list1 = []
        list1.append(str(what).capitalize())
        list1.append(s7)
        return list1
    else:
        wikipedia.set_lang('ru')
        text = wikipedia.summary(str(what).capitalize())
        s = StringSort(str(text))
        s1 = s.delete('1234567890', ']')
        s2 = StringSort(str(s1))
        s3 = s2.delete('[]')
        s4 = StringSort(s3)
        s5 = s4.split(split)
        s6 = StringSort(s5)
        s7 = s6.delete(' ', ' ')

        list1 = []
        list1.append(str(what).capitalize())
        list1.append(s7)
        return list1

def get_images(what, lang):
    url_en = 'https://en.wikipedia.org/wiki/' + str(what).capitalize()
    url_ru = 'https://ru.wikipedia.org/wiki/' + str(what).capitalize()

    if lang == 'ru':
        source = requests.get(url_ru).text

        resource = Extractor.from_yaml_file('files/paths.yaml')
        not_full_result = resource.extract(source)

        path = not_full_result['Image']
        return path
    if lang == 'en':
        source = requests.get(url_en).text

        resource = Extractor.from_yaml_file('files/paths.yaml')
        not_full_result = resource.extract(source)

        path = not_full_result['Image']
        return path