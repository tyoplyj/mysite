from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from .forms import *
from .utils import *
from .models import *
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin




class ShopHome(DataMixin, ListView):
    model = PerimetrShop
    template_name = 'shop/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная')

        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return PerimetrShop.objects.filter(is_published=True).select_related('cat')


def about(request):
    return render(request,'shop/about.html', {'menu': menu, 'title': 'О нас'})


class AddProduct(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddProductForm
    template_name = 'shop/addproduct.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавить продукт')
        return dict(list(context.items()) + list(c_def.items()))

def pageNotFound(request, exception):                   # Функия странцы 404
    return HttpResponseNotFound('<h1>Иди на хуй, такого адреса нету!!!</h1>')


class ShowPost(DataMixin, DetailView):
    model = PerimetrShop
    template_name = 'shop/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])

        current_product = context['post']
        current_category = current_product.cat

        next_product = PerimetrShop.objects.filter(cat=current_category, id__gt=current_product.id).order_by(
            'id').first()
        context['next_product'] = next_product

        previous_product = PerimetrShop.objects.filter(cat=current_category, id__lt=current_product.id).order_by(
            '-id').first()
        context['previous_product'] = previous_product
        return dict(list(context.items()) + list(c_def.items()))




class ShopCategory(DataMixin, ListView):
    model = PerimetrShop
    template_name = 'shop/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return PerimetrShop.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(title=str(c.name), cat_selected=c.pk)

        return dict(list(context.items()) + list(c_def.items()))


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'shop/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'shop/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('login')


class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'shop/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Контакты")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')













