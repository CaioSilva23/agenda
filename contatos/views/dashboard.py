from django.views import View
from django.shortcuts import redirect, get_object_or_404,render
from contatos.forms import FormContato
from django.contrib import messages
from contatos.models import Contato

class DashboardContatos(View):

    def get_recipe(self, id):
        contato = None
        if id:
            contato = get_object_or_404(Contato, id=id)
        return contato
    
    def get(self, request, id):
        return redirect(f'/contato/{id}')

    def post(self, request, id):
        contato = self.get_recipe(id=id)
        form = FormContato(request.POST or None, 
                           request.FILES or None, 
                           instance=contato)
        if form.is_valid():
            user = form.save(commit=False)
            user.user = request.user
            user.save()
            messages.success(request, 'Contato editado com sucesso!')
            return redirect(f'/contatos/contato/{id}')
        else:
            messages.success(request, 'Dados incorretos!!')
            return redirect(f'/contatos/contato/{id}')