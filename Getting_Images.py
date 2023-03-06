from wikiapi import WikiApi
wiki = WikiApi()


import requests
import shutil


def getWikiImage(entity):
    results = wiki.find(entity)
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
        print('Image Couldn\'t be retreived')