"""
To render html pages
"""

from django.http import HttpResponse


html_string = " <h1>Hello World</h1>"

def home_view(request):
    return HttpResponse(html_string)