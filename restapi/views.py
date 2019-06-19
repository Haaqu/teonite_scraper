from blogscraper.models import BlogPost, Author
from rest_framework.response import Response
from rest_framework.decorators import api_view
from restapi.counter import countwords
from django.shortcuts import get_object_or_404


@api_view()
def show(request):
    authors = dict(Author.objects.all().values_list('nickname', 'name'))
    return Response(authors)

@api_view()
def common_words(request):
    article = BlogPost.objects.all()
    most_common = countwords(article)
    return Response(most_common)

@api_view()
def author_words(request, author):
    user = get_object_or_404(Author, nickname=author)
    user_common = countwords(user.articles.all())
    return Response(user_common)
