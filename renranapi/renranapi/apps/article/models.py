from django.db import models
from renranapi.utils.models import BaseModel
from users.models import User
from django.utils.safestring import mark_safe


# Create your models here.

class ArticleCollection(BaseModel):
    user = models.ForeignKey(User, related_name="mycollections", on_delete=models.DO_NOTHING, verbose_name="用户")
    name = models.CharField(max_length=150, db_index=True, verbose_name="文集名称")

    class Meta:
        db_table = "rr_article_collection"
        verbose_name = "文集"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Article(BaseModel):
    title = models.CharField(max_length=150, db_index=True, verbose_name="文章")
    content = models.TextField(null=True, blank=True, verbose_name="文章内容")
    html_content = models.TextField(null=True, blank=True, verbose_name="文章内容[html格式]")
    user = models.ForeignKey(User,related_name="myarticles", on_delete=models.DO_NOTHING, verbose_name="作者")
    collection = models.ForeignKey(ArticleCollection, related_name="article_list", on_delete=models.CASCADE, verbose_name="文集")
    pub_date = models.DateTimeField(null=True,blank=True, default=None, verbose_name="发布时间")
    access_pwd = models.CharField(max_length=15, null=True, blank=True, verbose_name="访问密码")
    read_count = models.IntegerField(default=0, null=True, blank=True, verbose_name="阅读量")
    like_count = models.IntegerField(default=0, null=True, blank=True, verbose_name="点赞量")
    collect_count = models.IntegerField(default=0, null=True, blank=True, verbose_name="收藏量")
    comment_count = models.IntegerField(default=0, null=True, blank=True, verbose_name="评论量")
    reward_count = models.IntegerField(default=0, null=True, blank=True, verbose_name="赞赏量")
    is_public = models.BooleanField(default=False, verbose_name="是否公开")

    class Meta:
        db_table = "rr_article"
        verbose_name = "文章"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class ArticleSpecial(BaseModel):
    """专题模型"""
    name = models.CharField(max_length=50, unique=True, verbose_name="专题名称")
    image = models.ImageField(null=True, blank=True, verbose_name="封面图片")
    notice = models.TextField(null=True, blank=True, verbose_name="专题公告")
    article_count = models.IntegerField(default=0, null=True, blank=True, verbose_name="文章总数")
    follow_count = models.IntegerField(default=0, null=True, blank=True, verbose_name="关注数量")
    user = models.ForeignKey(User, related_name="myspecials", on_delete=models.DO_NOTHING, verbose_name="创建人")

    class Meta:
        db_table = "rr_article_special"
        verbose_name = "专题"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def check_post_status(self, article_id):
        """判断当前文章对于专题的收录状态"""
        try:
            self.myarticles.get(article_id=int(article_id), status=2)
            return True
        except:
            return False

    def image_html(self):
        if self.image:
            return mark_safe(
                f'<img style="border-radius: 0%;max-height: 60px; max-width: 200px;" src="{self.image.url}">')
        return ""

    image_html.short_description = "封面图片"
    image_html.allow_tags = True
    image_html.admin_order_field = "image"


class ArticlePostSpecial(BaseModel):
    """文章和专题的绑定关系"""
    STATUS_OPTION = (
        (0, "投稿中"),
        (1, "等待审核"),
        (2, "审核通过"),
        (3, "审核不通过"),
    )
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="文章")
    special = models.ForeignKey(ArticleSpecial, related_name="myarticles", on_delete=models.CASCADE, verbose_name="专题")
    status = models.SmallIntegerField(choices=STATUS_OPTION, default=0, verbose_name="审核状态")
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING, verbose_name="审核管理员")
    post_time = models.DateTimeField(default=None, null=True, blank=True, verbose_name="投稿时间")

    class Meta:
        db_table = "rr_article_post_special"
        verbose_name = "专题的文章"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.article.title


class SpecialManager(BaseModel):
    """专题管理员"""
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="用户")
    special = models.ForeignKey(ArticleSpecial, related_name="mymanager", on_delete=models.CASCADE, verbose_name="专题")

    class Meta:
        db_table = "rr_special_manager"
        verbose_name = "专题管理员"
        verbose_name_plural = verbose_name


class SpecialFocus(BaseModel):
    """专题关注"""
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="用户")
    special = models.ForeignKey(ArticleSpecial, on_delete=models.CASCADE, verbose_name="专题")

    class Meta:
        db_table = "rr_special_focus"
        verbose_name = "专题粉丝"
        verbose_name_plural = verbose_name


class ArticleImage(BaseModel):
    """文章图片素材库"""
    group = models.CharField(max_length=15, null=True, blank=True, verbose_name="组名")
    image = models.ImageField(null=True, blank=True, verbose_name="图片地址")
    sha1_files = models.CharField(max_length=64, null=True, blank=True, verbose_name="文件指纹")

    class Meta:
        db_table = "rr_article_image"
        verbose_name = "文章图片"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.group
