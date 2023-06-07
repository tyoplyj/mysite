from django.db.models import Count
from django.contrib.auth.models import User
from django.core.cache import cache


from .models import *

menu = [{'title': "Главная", 'url_name': 'home'},
        {'title': "О нас", 'url_name': 'about'},
        {'title': "Добавить товар", 'url_name': 'addproduct'},
        {'title': "Контакты", 'url_name': 'contact'},
        ]


class DataMixin:
    paginate_by = 12
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.annotate(Count('perimetrshop'))

        user_menu = menu.copy()
        if not self.request.user.is_superuser:
            user_menu.pop(2)

        context['menu'] = user_menu

        # Получение списка уникальных категорий и фотографий категорий
        category_photos = Category.objects.annotate(num_products=Count('perimetrshop')).filter(num_products__gt=0)
        context['category_photos'] = category_photos

        context['cats'] = cats
#        if 'cat_selected' not in context:
#            context['cat_selected'] = 0
        return context
