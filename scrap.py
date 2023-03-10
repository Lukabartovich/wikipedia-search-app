import requests
from selectorlib import Extractor
from StringSort import StringSort


def getting_data(what, split, lang):
    url_en = 'https://en.wikipedia.org/wiki/' + str(what).title()
    url_ru = 'https://ru.wikipedia.org/wiki/' + str(what).title()

    if lang == 'en':

        source = requests.get(url_en).text

        resource = Extractor.from_yaml_file('files/paths.yaml')
        not_full_result = resource.extract(source)

        name = not_full_result['Name']
        text = not_full_result['Text']
        more_info = not_full_result['MoreInfo']


        if more_info != None:
            s = StringSort(str(text) + str(more_info))
            s1 = s.delete('1234567890', ']')
            s2 = StringSort(str(s1))
            s3 = s2.delete('[]')
            s4 = StringSort(s3)
            s5 = s4.split(split)
            s6 = StringSort(s5)
            s7 = s6.delete(' ', ' ')


            list1 = []
            list1.append(name)
            list1.append(s7)
            return list1
        else:
            s = StringSort(str(text))
            s1 = s.delete('1234567890', ']')
            s2 = StringSort(str(s1))
            s3 = s2.delete('[]')
            s4 = StringSort(s3)
            s5 = s4.split(split)
            s6 = StringSort(s5)
            s7 = s6.delete(' ', ' ')

            list1 = []
            list1.append(name)
            list1.append(s7)
            return list1
    else:
        source = requests.get(url_ru).text

        resource = Extractor.from_yaml_file('files/paths.yaml')
        not_full_result = resource.extract(source)

        name = not_full_result['NameRu']
        text = not_full_result['TextRu']
        more_info = not_full_result['MoreInfoRu']

        if more_info != None:
            s = StringSort(str(text) + str(more_info))
            s1 = s.delete('1234567890', ']')
            s2 = StringSort(str(s1))
            s3 = s2.delete('[]')
            s4 = StringSort(s3)
            s5 = s4.split(split)
            s6 = StringSort(s5)
            s7 = s6.delete(' ', ' ')

            list1 = []
            list1.append(name)
            list1.append(s7)
            return list1
        else:
            s = StringSort(str(text))
            s1 = s.delete('1234567890', ']')
            s2 = StringSort(str(s1))
            s3 = s2.delete('[]')
            s4 = StringSort(s3)
            s5 = s4.split(split)
            s6 = StringSort(s5)
            s7 = s6.delete(' ', ' ')

            list1 = []
            list1.append(name)
            list1.append(s7)
            return list1

def get_images(what):
    path = f'https://www.google.com/search?q=' + what + '&sxsrf=AJOqlzV4_4Ty7Nw8nJDPRuJvFC-P8G72Xg:1678306870289&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiP7c6mlM39AhX-57sIHaJjBzkQ_AUoAXoECAEQAw&biw=1350&bih=635&dpr=1'

    source = requests.get(path).text

    resource = Extractor.from_yaml_file('files/paths.yaml')
    reresource = resource.extract(source)

    link_for_image = reresource['ImagesEn']

    return link_for_image
