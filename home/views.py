from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from bucket import bucket
from .models import Product
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from utils import IsAdminUserMixin


# Create your views here.


class HomeView(View):
    def get(self, request):
        products = Product.objects.filter(available=True)
        return render(request, 'home/home.html', {'products': products})


class ProductDetailView(LoginRequiredMixin, View):
    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        return render(request, 'home/product_detail.html', {'product': product})


class BucketHome(IsAdminUserMixin, View):
    template_name = 'home/bucket.html'

    def get(self, request):
        objects = bucket.get_objects()
        return render(request, self.template_name, {'objects': objects})


class DeleteBucketObject(IsAdminUserMixin, View):
    def get(self, request, key):
        bucket.delete_object(key)
        messages.success(request, 'object is delete', 'success')
        return redirect('home:bucket')


class DownloadBucketObject(IsAdminUserMixin, View):
    def get(self, request, key):
        bucket.download_object(key)
        messages.success(request, 'object is download', 'success')
        return redirect('home:bucket')
