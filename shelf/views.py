from django.shortcuts import render
from django.views.generic import ListView, DetailView,TemplateView
from django.http import HttpResponse

from .models import Author, Book


# Create your views here.

# pierwszy sposób:

# class MainPageView(View):
 #   def get(self, request, *args, **kwargs):
  #      return HttpResponse('ok')

# index_view = MainPageView.as_view() to przy drugim sposobie

class MainPageView(TemplateView):
    template_name = 'index.html'



class AuthorListView(ListView):
    model = Author


class AuthorDetailView(DetailView):
    model = Author


class BookListView(ListView):
    model = Book


class BookDetailView(DetailView):
    model = Book
