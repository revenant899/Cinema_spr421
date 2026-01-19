from django import forms
from films.models import Film

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = '__all__'
        # ['name', 'image_url', 'description', 'price', 'stock', 'category', 'show_time']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Film name'}),
            'image_url': forms.URLInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Film description'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Price in USD'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of tickets available'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'show_time': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control', 'placeholder': 'Show time'}),
        }