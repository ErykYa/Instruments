from django.views.generic import ListView, DetailView, CreateView, TemplateView
from .models import Catalog
from django.db.models import Q
from django.shortcuts import render
from cart.forms import CartAddProductForm


class Home(TemplateView):
    template_name = 'catalog/Home.html'


class Category(ListView):
    model = Catalog
    context_object_name = 'catalog'
    template_name = 'catalog/Catalog.html'
    paginate_by = 50

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_product_form'] = CartAddProductForm()
        return context

    def get_queryset(self):
        return Catalog.objects.filter(category_id=self.kwargs['category_id'])

# def get_brand(request, brand_title):
#     catalog = Catalog.objects.filter(brand=brand_title).filter(price__gt=0)
#     context = {
#         'catalog': catalog,
#     }
#     return render(request, 'catalog/Catalog.html', context)


class Brand(ListView):
    model = Catalog
    context_object_name = 'catalog'
    template_name = 'catalog/Catalog.html'
    paginate_by = 50

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_product_form'] = CartAddProductForm()
        return context

    def get_queryset(self):
        return Catalog.objects.filter(brand=self.kwargs['brand_title'])


class HomeCatalog(ListView):
    model = Catalog
    context_object_name = 'catalog'
    template_name = 'catalog/Catalog.html'
    paginate_by = 50

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_product_form'] = CartAddProductForm()
        return context

    def get_queryset(self):
        return Catalog.objects.all()


class NavSearch(ListView):
    model = Catalog
    context_object_name = 'catalog'
    template_name = 'catalog/Catalog.html'
    paginate_by = 50

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_product_form'] = CartAddProductForm()
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Catalog.objects.filter(
                Q(title__icontains=query)
            )
        return Catalog.objects.all()


class CatalogResults(ListView):
    model = Catalog
    context_object_name = 'catalog'
    template_name = 'catalog/Catalog.html'
    paginate_by = 50

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_product_form'] = CartAddProductForm()
        return context

    def get_queryset(self):
        title = self.request.GET.get('q')
        brand = self.request.GET.get('q1')
        base_queryset = Catalog.objects.all()
        if not title:
            title = ''

        if not brand:
            brand = ''

        if title or brand != '':
            filtering_query = self._build_filtering_query_(title, brand)
            return base_queryset.filter(filtering_query)

        return base_queryset

    @staticmethod
    def _build_filtering_query_(query_title, query_brand):
        if query_brand != '':
            return (
                Q(title__icontains=query_title, brand=query_brand)
            )
        elif query_title is '':
            return (
                Q(brand=query_brand)
            )
        return (
            Q(title__icontains=query_title)
        )


class Tovar(DetailView):
    model = Catalog
    context_object_name = 'tovar'
    template_name = 'catalog/Tovar.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_product_form'] = CartAddProductForm()
        return context



