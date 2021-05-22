from django.forms import ModelForm
from product.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'image', 'title', 'description', 'price']


# class ProductImageForm(ModelForm):
#     class Meta:
#         model = ProductImage
#         fields = ['image']
