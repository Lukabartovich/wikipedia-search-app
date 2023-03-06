import requests
from selectorlib import Extractor
from StringSort import StringSort


def getting_data(what, split):
    url = 'https://en.wikipedia.org/wiki/' + str(what).title()

    source = requests.get(url).text

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