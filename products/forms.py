from django import forms
from . import models


class ProductForm(forms.ModelForm):

    class Meta:
        model = models.Product
        fields = ['title', 'category', 'brand', 'serie_number', 'description', 'cost_price', 'selling_price']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'brand': forms.Select(attrs={'class': 'form-control'}),
            'serie_number': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea({'class': 'form-control', 'rows': 3}),
            'cost_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'selling_price': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Título',
            'category': 'Categoria',
            'brand': 'Marca',
            'serie_number': 'Número de série',
            'description': 'Descrição',
            'cost_price': 'Preço de custo',
            'selling_price': 'Preço de venda',
        }
