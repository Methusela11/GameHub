
from django import forms
from .models import Game, Category

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['title','slug','category','description','price','cover_image','file','external_link','version']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name','slug']
