import re
import time
import sys
from prometheus_client import start_http_server, Gauge
from articles import Articles

PORT = 8000
g = Gauge('latest_article_diff', 'Date elapsed since most recent article')


def get_metrics(request_url: str, sleep_time: int):
    articles = Articles(request_url)
    articles_diff = articles.latest_diff_date()
    g.set(articles_diff)
    time.sleep(sleep_time)


if __name__ == '__main__':
    if len(sys.argv) != 2 or not re.match("https?://[\w/:%#\$&\?\(\)~\.=\+\-]+", sys.argv[1]):
        print('The second argument must be a URL.')
        exit(1)

    start_http_server(PORT)
    print('Started server(port: ' + str(PORT) + ')')
    while True:
        get_metrics(sys.argv[1], 30)
