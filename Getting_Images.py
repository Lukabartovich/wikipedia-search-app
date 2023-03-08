import wget
from wikiapi import WikiApi
from translate import Translator
import requests
import shutil


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

def shutil_getting(path):
    image_url = path
    filename = image_url.split("/")[-1]

    r = requests.get(image_url, stream=True)

    if r.status_code == 200:
        r.raw.decode_content = True


        with open(filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)


        print('Image sucessfully Downloaded: ', filename)

        return filename
    else:
        name = wget.download(image_url, 'images/')
        return name