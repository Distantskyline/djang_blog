from django.db import models
from django.contrib.auth.models import User
from DjangoUeditor.models import UEditorField
# Create your models here.


class Category(models.Model):
    name = models.CharField('博客分类',max_length=30)
    class Meta:
        verbose_name = '博客分类'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField('文章标签',max_length=30)
    class Meta:
        verbose_name = '文章标签'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

class Tui(models.Model):
    name = models.CharField('推荐位',max_length=30)
    class Meta:
        verbose_name = '推荐位'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

class Banner(models.Model):
    text_info = models.CharField('标题',max_length=100)
    img = models.ImageField('轮播图',upload_to='banner/')
    link_url = models.URLField('图片链接',max_length=100)
    is_active = models.BooleanField('是否为cative',default=False)
    def __str__(self):
        return self.text_info
    class Meta():
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name

class Link(models.Model):
    name = models.CharField('链接名称',max_length=20)
    link_url = models.URLField('网址',max_length=100)
    class Meta():
        verbose_name = '链接名称'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField('标题',max_length=100)
    excerpt = models.TextField('摘要', max_length=200, blank=True)
    category = models.ForeignKey(Category,on_delete=models.DO_NOTHING,verbose_name='分类',blank=True,null=True)
    tags = models.ManyToManyField(Tag,verbose_name='标签',blank=True)
    body = UEditorField('内容', width=800, height=500,
                        toolbars="full", imagePath="upimg/", filePath="upfile/",
                        upload_settings={"imageMaxSize": 1204000},
                        settings={}, command=None, blank=True
                        )
    img = models.ImageField(upload_to='img/',verbose_name='缩略图',null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='作者')
    views = models.PositiveIntegerField('阅读量',default=0)
    tui = models.ForeignKey(Tui,on_delete=models.DO_NOTHING,verbose_name='推荐', blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField('修改时间', auto_now_add=True)

    class Meta():
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title