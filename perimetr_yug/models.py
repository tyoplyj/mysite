from django.db import models
from django.urls import reverse


# Create your models here.

class PerimetrShop (models.Model):
    title = models.CharField(max_length=255, verbose_name = 'Заголовок')
    slug = models.SlugField(blank=True, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name='Описание')
    param = models.TextField(blank=True, verbose_name = 'Характеристики')
    contents = models.TextField(blank=True, verbose_name='Обзор товара')
    price = models.IntegerField(verbose_name = 'Цена')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name = 'Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name = 'Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name = 'Последнее обновление')
    is_published = models.BooleanField(default=True, verbose_name = 'Публикация')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name = 'Категория')

    def __str__(self):
        return self.title

    def get_absolute_url(self):          # Функция динамических ссылок для товаров
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:                                  # Класс для отображения названия в ЛК
        verbose_name = 'Магазин'                 # Изменение названия
        verbose_name_plural = 'Магазин'          # Убрать букву s в конце
        ordering = ['-time_create', 'title']      # Сортировка по (вставить атрибут БД)

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name = 'Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    photo = models.ImageField(upload_to="category_photos/%Y/%m/%d", blank=True, null=True, verbose_name='Фото')

    def __str__(self):
        return self.name

    def get_absolute_url(self):          # Функция динамических ссылок в категориях
        return reverse('category', kwargs={'cat_slug': self.slug})


    class Meta:                                  # Класс для отображения названия в ЛК
        verbose_name = 'Категория'                 # Изменение названия
        verbose_name_plural = 'Категории'          # Убрать букву s в конце
        ordering = ['id']      # Сортировка по (вставить атрибут БД)