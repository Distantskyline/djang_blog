from django.shortcuts import render
from blog import models
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger #自动分页包

# Create your views here.


def index(request):
    fenlei = models.Category.objects.all()
    img = models.Banner.objects.filter(is_active=True)
    tags = models.Tag.objects.all()
    tuijian = models.Article.objects.filter(tui__id=1)[:3]
    tuijian2 = models.Article.objects.filter(tui__id=2)[:3]
    allarticle = models.Article.objects.all().order_by('-id')[0:4]
    Url = models.Link.objects.all()
    hot = models.Article.objects.all().order_by('-views')[:5]
                            # 通过浏览数进行排序,加个 - 由高到低排序
    content = {
        'A': fenlei,
        'B': img,
        'D': tags,
        'Url': Url,
        'E': tuijian,
        'F': tuijian2,
        'new': allarticle,
        'hot': hot
    }
    return render(request, 'index.html', content, )


#列表页
def list(request,lid):
    fenlei = models.Category.objects.all()
    weizhi1 = models.Category.objects.get(pk=lid)
    wenzhang = models.Article.objects.filter(category__id=lid).order_by('-id')
    tags = models.Tag.objects.all()
    tuijian = models.Article.objects.filter(tui__id=2)[:3]
    Tag = models.Tag.objects.filter(article__id=lid)
    hot = models.Article.objects.all().order_by('-views')[:5]
                            # 通过浏览数进行排序,加个 - 由高到低排序

    page = request.GET.get('page')  # 在URL中获取当前页面数
    paginator = Paginator(wenzhang, 2)  # 对查询到的数据对象list进行分页，设置超过5条数据就分页
    try:
        wenzhang = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        wenzhang = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        wenzhang = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容

    content = {
        'A': fenlei,
        'weizhi': weizhi1,
        'C': wenzhang,

        'D': tags,
        'F': tuijian,
        'Tag': Tag,
        'hot': hot,
    }
    return render(request,'list.html',content,)

#内容页
def show(request,sid):
    fenlei = models.Category.objects.all() # 键A,base页面的，所有分类
    category_id = models.Article.objects.get(pk=sid).category_id  #取出文章的id所对应的的分类表id
    weizhi1 = models.Category.objects.get(pk=category_id) #利用文章id-分列表id取出文章所属的分类，键weizhi1 (您的位置： 首页 » weizhi1 » 正文)
    body = models.Article.objects.get(pk=sid) #show页面取出文章的具体内容，使用 {{ body.body|safe }} 取出富文本编辑器的内容
    tags = models.Tag.objects.all() #键D，侧边栏的所有标签
    tuijian = models.Article.objects.filter(tui__id=2)[:3]  #键F，侧边栏的热门推荐
    wenzhang = models.Article.objects.get(pk=sid)  #取出sid对应的文章所有信息
    fenlei2 = models.Article.objects.get(pk=sid).category #<a href="/list-{{ fenlen2.id }}.html">{{ weizhi1 }}</a> 跳转链接用
    category_id2 = models.Article.objects.get(pk=sid).category_id   #根据文章id取出文章对应的分类ID
    tonglei = models.Article.objects.filter(category_id=category_id2)  #根据文章的分类ID，过滤和他同类的文章信息
    user_id = models.Article.objects.get(pk=sid).user_id  #取出文章的User_id
    user = models.User.objects.get(pk=user_id).username  #取出文章的具体作者
    Tag = models.Tag.objects.filter(article__id=sid)  #键Tag，取出文章所属于的所有标签
    body.views = body.views + 1 #对访问量 + 1
    body.save() #保存
    hot = models.Article.objects.all().order_by('-views')[:5]
                        #通过浏览数进行排序,加个 - 由高到低排序
    previous_blog = models.Article.objects.filter(created_time__gt=body.created_time, category=body.category.id).first()
    #前一偏
    next_blog = models.Article.objects.filter(created_time__lt=body.created_time, category=body.category.id).last()
    #后一偏

    content = {
        'A': fenlei,
        'weizhi1': weizhi1,
        'wenzhang': wenzhang,
        'body': body,
        'tonglei': tonglei,
        'D': tags,
        'F': tuijian,
        'fenlen2': fenlei2,
        'username': user,
        'Tag': Tag,
        'hot': hot,
        'syp': previous_blog,
        'next': next_blog,
    }
    return render(request,'show.html',content)


#标签页
def tag(request, tag):
    tag_id = models.Tag.objects.get(name=tag)
    fenlei = models.Category.objects.all()
    wenzhang = models.Article.objects.filter(tags=tag_id).order_by('-id')
    tags = models.Tag.objects.all()
    tuijian = models.Article.objects.filter(tui__id=2)[:3]
    hot = models.Article.objects.all().order_by('-views')[:5]

    page = request.GET.get('page')  # 在URL中获取当前页面数
    paginator = Paginator(wenzhang, 2)  # 对查询到的数据对象list进行分页，设置超过5条数据就分页
    try:
        wenzhang = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        wenzhang = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        wenzhang = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    content = {
        'A': fenlei,
        'wenzhang': wenzhang,
        'D': tags,
        'F': tuijian,
        'tag_id': tag_id,
        'Tag': tag,
        'hot': hot,
    }
    return render(request,'tag.html',content)


# 搜索页
def search(request):
    fenlei = models.Category.objects.all()  # 键A,base页面的，所有分类
    guanjianci = request.GET.get('search') #获取搜索的关键词
    list = models.Article.objects.filter(title__icontains=guanjianci) #获取到搜索关键词公国标题比配
    remen = models.Article.objects.filter(tui__id=2)[:6]
    allcategory = models.Category.objects.all()
    page = request.GET.get('page')
    tags = models.Tag.objects.all()
    tuijian = models.Article.objects.filter(tui__id=2)[:3]
    hot = models.Article.objects.all().order_by('-views')[:5]
    paginator = Paginator(list, 2) #每一页最多显示的文章数量
    try:
        list = paginator.page(page) # 获取当前页码的记录
    except PageNotAnInteger:
        list = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        list = paginator.page(paginator.num_pages)   # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容

    content = {
        'A': fenlei,
        'guanjianci': guanjianci,
        'list': list, #分页用
        'remen': remen,
        'allcategory': allcategory,
        'page': page,
        'D': tags,
        'F': tuijian,
        'hot': hot,
    }
    return render(request, 'search.html', content)




# 关于我们
def about(request):
    fenlei = models.Category.objects.all()
    content = {
        'A': fenlei,
    }
    return render(request,'page.html',content)