import feedparser
import urllib.request
import ssl

def fetch_news_feed(url, headers):
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE

    req = urllib.request.Request(url, headers=headers)
    feed = feedparser.parse(urllib.request.urlopen(req, context=ssl_context))
    entries = feed.entries

    for entry in entries:
        title = entry.title
        link = entry.link
        published = entry.published
        category = entry.category
        description = entry.description

        print("Title:", title)
        print("Link:", link)
        print("Published:", published)
        print("category:", category)
        print("description:", description)
        print()

# 뉴스 피드 URL
economy_news_feed_url = "https://www.yonhapnewstv.co.kr/category/news/economy/feed/"
browse_news_feed_url = "http://www.yonhapnewstv.co.kr/browse/feed/"
headline_news_feed_url = "http://www.yonhapnewstv.co.kr/category/news/headline/feed/"


# User-Agent 헤더 추가
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}

# 뉴스 피드 가져오기
print("경제 뉴스 피드")
fetch_news_feed(economy_news_feed_url, headers)
print("최신 뉴스 피드")
fetch_news_feed(browse_news_feed_url, headers)
print("헤드라인 뉴스 피드")
fetch_news_feed(headline_news_feed_url, headers)