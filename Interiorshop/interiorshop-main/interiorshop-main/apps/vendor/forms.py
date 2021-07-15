from django.forms import ModelForm
from django import forms
from apps.product.models import Product, ProductImage,Category,Vendor
class ProductForm(ModelForm):
    #category = forms.ModelChoiceField(queryset=Category.objects.all() ,empty_label='choose_category',required=True)
    class Meta:
        model = Product

        #fields = ['category' , 'image', 'title', 'description', 'price']
        fields = ['category']
        # fields = ['category', 'image', 'title', 'description', 'price']

class ProductImageForm(ModelForm):
    class Meta:
        model = ProductImage
        fields = ['image']
# class EditUserProfile(ModelForm):
#     class Meta:
#         model=Vendor
#         fields=['name','email','password']