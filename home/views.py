from django.shortcuts import render
from django.views.generic import View
from .models import *
# Create your views here.
class BaseView(View):
	views = {}


class HomeView(BaseView):
	def get(self,request):
		self.views['sliders'] = Slider.objects.all()
		self.views['categories'] = Category.objects.all()
		self.views['subcategories'] = SubCategory.objects.all()
		self.views['items'] = Product.objects.filter(status = 'active')
		return render(request,'index.html',self.views)

class SubCategoryViews(BaseView):
	def get(self,request,slug):
		id = SubCategory.objects.get(slug = slug).id
		self.views['subcategories_product'] = Product.objects.filter(subcategory_id = id)
		return render(request,'subcategory.html',self.views)


class BrandViews(BaseView):
	def get(self,request,slug):
		id = Brand.objects.get(slug = slug).id
		self.views['brand_product'] = Product.objects.filter(brand_id = id)
		return render(request,'brand.html',self.views)