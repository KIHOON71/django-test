from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from books.models import Book, Author, Publisher
# Create your views here.

#Templateview
class BooksModelView(TemplateView):
    template_name = 'books/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_list'] = ['Book', 'Author', 'Publisher']
        return context

#ListView
class Booklist(ListView):
    model = Book
    # book_list.html
    # object_list
class PublisherList(ListView):
    model = Publisher
class AuthorList(ListView):
    model = Author

#--- DetailView
class BookDetail(DetailView):
    model = Book
    # object
    # book_detail.html
class AuthorDetail(DetailView):
    model = Author
class PublisherDetail(DetailView):
    model = Publisher