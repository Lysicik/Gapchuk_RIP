from django.db import models
from datetime import date

from django.urls import reverse


class Author(models.Model):
    """Авторы"""
    name = models.CharField("Имя", max_length=100)
    age = models.PositiveSmallIntegerField("Возраст", default=0)
    description = models.TextField("Описание")


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Авторы"
        verbose_name_plural = "Авторы"


class Book(models.Model):
    """Книга"""
    title = models.CharField("Название", max_length=100)
    tagline = models.CharField("Слоган", max_length=100, default='')
    description = models.TextField("Описание")
    authors = models.ManyToManyField(Author, verbose_name="автор", related_name="author_book")

    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"