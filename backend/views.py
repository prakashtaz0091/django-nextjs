from django.shortcuts import render

# myapp/views.py
from django_nextjs.render import render_nextjs_page_sync


def index(request):
    return render_nextjs_page_sync(request)