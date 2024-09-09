# from django.http import HttpResponse
# from django.shortcuts import render
#
# from .models import Author,Article,AuthorExtension
#
# # Create your views here.
#
# def article_test(request):
#     # author=Author(name="罗贯中",email="3048808457@qq.com",bio="sads")
#     # author.save()
#     # article=Article(title="三国演义",content="sadsad",author=author)
#     # article.save()
#
#     # article=Article.objects.first()
#
#     author = Author.objects.first()
#
#     articles = author.article_set.all()
#
#     for article in articles:
#         print(article.published_date)
#
#     return HttpResponse('2323')
#
#
# def AuthorExtensionTest(request):
#     author = Author(name="吴承恩", email="3048808457@qq.com", bio="西游记")
#     author.save()
#     author_extension = AuthorExtension(university="清华大学", author=author)
#     author_extension.save()
#
#
