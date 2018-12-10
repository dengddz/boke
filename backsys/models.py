from django.db import models

# Create your models here.


class SuperUser(models.Model):
    username = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=20)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'db_superuser'


class ArticleType(models.Model):
    type = models.CharField(max_length=20, unique=True)

    class Meta:
        db_table = 'db_articletype'


class Article(models.Model):
    a_title = models.CharField(max_length=20, unique=True)
    a_content = models.TextField()
    a_keywords = models.CharField(max_length=30)
    a_describe = models.CharField(max_length=100)
    # 保存图片的路径，type为 char。上传到article中 media
    a_titlepic = models.ImageField(upload_to='article', null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    a_f = models.ForeignKey(ArticleType)

    class Meta:
        db_table = 'db_article'

