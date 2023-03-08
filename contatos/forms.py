from django import forms
from .models import Contato, Categoria


class FormContato(forms.ModelForm):
    class Meta:
        model = Contato
        #fields = '__all__'
        exclude = ('user', 'date_created', 'descricao')

        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome', 'class': 'form-control'}),
            'sobrenome': forms.TextInput(attrs={'placeholder': 'Sobrenome', 'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'placeholder': 'Telefone', 'class': 'form-control'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            
        }
class FormCategoria(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'
        
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Categoria...', 'class': 'form-control'}),
 
        }
