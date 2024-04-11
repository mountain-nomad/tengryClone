from django.db import models
from datetime import date

from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField("Категория", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique= True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Author(models.Model):
    name = models.CharField("Имя", max_length=150)
    description = models.TextField("Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Автор статьи"
        verbose_name_plural = "Авторы статьи"


class New(models.Model):
    """Article"""
    title = models.CharField("Заголовок", max_length=100)
    tagline = models.CharField("Подзоголовок", max_length=100, default='')
    description = models.TextField("Текст статьи")
    poster = models.ImageField("Главная фотография", upload_to="news/")
    country = models.CharField("Страна", max_length=30)
    author = models.ManyToManyField(Author, verbose_name="Автор статьи", related_name="new_author")
    article_date = models.DateField("Дата выхода статьи", default = date.today)
    category = models.ManyToManyField(Category, verbose_name="Категория", related_name="new_category")
    url = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("new_detail", kwargs={"slug": self.url})


    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


class AdditionalImg(models.Model):
    """Дополнительные фото к статье"""
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="article_shots/")
    movie = models.ForeignKey(New, verbose_name="Статья", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фото к статье"
        verbose_name_plural = "Фото к статье"
