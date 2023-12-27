from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Product
from .tacks import all_bucket_objects_task, delete_object_task
from django.contrib import messages


# Create your views here.


class HomeView(View):
    def get(self, request):
        products = Product.objects.filter(available=True)
        return render(request, 'home/home.html', {'products': products})


class ProductDetailView(View):
    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        return render(request, 'home/product_detail.html', {'product': product})


class BucketHome(View):
    template_name = 'home/bucket.html'

    def get(self, request):
        objects = all_bucket_objects_task()
        return render(request, self.template_name, {'objects': objects})


class DeleteBucketObject(View):
    def get(self, request, key):
        delete_object_task(key)
        messages.success(request, 'object is delete', 'success')
        return redirect('home:bucket')
