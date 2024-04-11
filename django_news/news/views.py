from django.shortcuts import render
from django.views.generic.base import View
from .models import New, Category
from django.views.generic import ListView, DetailView


# Create your views here.

class CategDate:
    def get_category(self):
        return Category.objects.all()

    def get_date(self):
        return New.objects.filter(draft = False).values('date')


class NewsView(CategDate, ListView):
    model = New
    queryset = New.objects.filter(draft = False)
    template_name = 'news/news_list.html'
    paginate_by = 3

    def get_queryset(self):
        # Возвращаем новости, отсортированные по дате публикации в убывающем порядке
        return New.objects.filter(draft=False).order_by('-article_date')




class NewDetailView(CategDate, DetailView):
    model = New
    slug_field = 'url'


class FilterNewsView(ListView):
    template_name = 'news/news_list.html'
    def get_queryset(self):

        queryset = New.objects.filter(
            category__in = self.request.GET.getlist('category')
        )
        return queryset

class Search(ListView):
    template_name = 'news/news_list.html'
    paginate_by = 3

    def get_queryset(self):
        return New.objects.filter(title__icontains = self.request.GET.get('q'))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = f"q={self.request.GET.get('q')}&"
        return context