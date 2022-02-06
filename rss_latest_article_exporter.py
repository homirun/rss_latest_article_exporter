import time
from prometheus_client import start_http_server, Gauge
from articles import Articles

g = Gauge('latest_article_diff', 'Date elapsed since most recent article')


def get_metrics(sleep_time: int):
    articles = Articles("https://blog.homi.run/")
    articles_diff = articles.latest_diff_date()
    g.set(articles_diff)
    time.sleep(sleep_time)


if __name__ == '__main__':
    start_http_server(8000)
    while True:
        get_metrics(30)
