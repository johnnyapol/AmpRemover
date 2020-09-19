import requests

# TODO: switch to asyncio


def check_if_appl(text):
    return "apple.news" in text


def get_urls(text):
    urls = []
    split = text.split(" ")
    for x in split:
        if check_if_appl(x):
            try:
                urls.append(get_actual_url(x))
            except:
                pass
    return urls


def get_actual_url(news_link):
    news = requests.get(news_link).text
    token = "redirectToUrlAfterTimeout("
    token_len = len(token)

    start = news.find(token)
    news = news[(start + token_len + 1) :]
    url = news[: news.find('"')]
    return url
