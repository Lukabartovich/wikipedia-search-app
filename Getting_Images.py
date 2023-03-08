from wikiapi import WikiApi
from translate import Translator

import requests

import urllib.request

wiki = WikiApi()

def getWikiImage(entity, lang):
    if lang == 'en':
        results = wiki.find(str(entity).capitalize())

        if len(results):
            article = wiki.get_article(results[0])
            return article.image
    if lang == 'ru':
        translating_lang = Translator(from_lang='Russian', to_lang='English')
        translation = str(translating_lang.translate(str(entity))).capitalize()

        results = wiki.find(str(translation))
        if len(results):
            article = wiki.get_article(results[0])
            return article.image

def download(path):
    ex = path[-4:]
    link = 'images/image' + str(ex)
    urllib.request.urlretrieve(path, link)

    return link