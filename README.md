# RSS latest article exporter
This is a Prometheus Exporter that can output the number of days elapsed since the latest article.

## Description
- Python 3.8.1
- requests 2.23.0
- prometheus-client 0.13.1

## Usage
Start the http server on port 8000

```
python ./bin/rss_latest_article_exporter.py "https://example.com/?rss"
```

`latest_article_diff` will be output.
