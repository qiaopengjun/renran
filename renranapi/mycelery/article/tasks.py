from mycelery.main import app
from article.models import Article
from django.utils import timezone as datetime
from article.views import ArticleAPIView


@app.task(name="interval_pub_article")
def interval_pub_article():
    """定时发布"""
    article_list = Article.objects.filter(pub_date__lte=datetime.now())
    print(article_list)
    for article in article_list:
        article.is_public = True
        article.pub_date = None
        article.save()
        # 推送feed流
        article.push_feed()
        # ArticleAPIView.push_feed(article)
        print("文章《%s》发布成功" % article.title)
