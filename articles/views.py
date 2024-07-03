from django.shortcuts import render
from .models import Article


from django.shortcuts import render, get_object_or_404
from .models import Article

def article_search_view(request):
    query_dict = request.GET

    try:
        query = int(query_dict.get("q"))
    except (TypeError, ValueError):
        query = None

    article_obj = None
    if query is not None:
        try:
            article_obj = Article.objects.get(id=query)
        except Article.DoesNotExist:
            article_obj = None

    context = {
        "object": article_obj,
    }
    return render(request, "articles/search.html", context=context)



# Create your views here.
def article_detail_view(request, id=None):
    article_obj = None
    if id is not None:
        article_obj = Article.objects.get(id=id)
    context = {
        "object":  article_obj, 
    }
    return render(request, "articles/detail.html", context=context)

# def article_detail_view(request, id=None):
#     article_obj = None
#     if id is not None:
#         article_obj = Article.objects.get(id = id)
#     context = {
#         "oject": article_obj,
#     }
#     return render(request, "articles/detail.html", context=context)
