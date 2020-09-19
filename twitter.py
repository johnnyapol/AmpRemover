import requests

# TODO: switch to asyncio


def check_if_tco(text):
    return "t.co/" in text


def get_urls(text):
    urls = []
    split = text.split(" ")
    for x in split:
        if check_if_tco(x):
            try:
                urls.append(get_actual_url(x))
            except:
                pass
    return urls


def get_actual_url(news_link):
    return requests.get(news_link).url
