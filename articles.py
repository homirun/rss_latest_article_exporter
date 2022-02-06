import requests
import xml.etree.ElementTree as Et
import datetime


class Articles:
    def __init__(self, url: str):
        self.url = url + "?feed=rss2"

    def latest_diff_date(self) -> datetime:
        parsed_articles = self._parse_rss_xml(requests.get(self.url).content)
        target_et = parsed_articles.find('channel').find('item').find('pubDate').text
        dt_article_latest = datetime.datetime.strptime(target_et, '%a, %d %b %Y %H:%M:%S %z')
        return abs(datetime.datetime.now(datetime.timezone.utc) - dt_article_latest).days

    @staticmethod
    def _parse_rss_xml(response_xml: bytes) -> Et:
        root = Et.fromstring(response_xml)
        return root


if __name__ == '__main__':
    article = Articles('https://blog.homi.run/')
    print(article.latest_diff_date())
