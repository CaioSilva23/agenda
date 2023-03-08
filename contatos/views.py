from django.views.generic import ListView, UpdateView, DeleteView, View
from contatos.models import Contato, Categoria
from contatos.forms import FormContato, FormCategoria
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse_lazy


@method_decorator(login_required(login_url='login'), name='dispatch')
class ContatosList(ListView):
    template_name = 'contatos/home.html'
    model = Contato
    context_object_name = 'contatos'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.order_by('nome').filter(user=self.request.user)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = FormContato()
        context['form_categoria'] = FormCategoria()
        return context
    
    def post(self, *args, **kwargs):
        form = FormContato(self.request.POST)
        if form.is_valid():
            novo_contato = form.save(commit=False)
            novo_contato.user = self.request.user
            novo_contato.save()
            messages.success(self.request, 'Novo contato inserido com sucesso!')
            return redirect('/')
        messages.error(self.request, 'Dados inválidos!')
        return redirect('/')

@method_decorator(login_required, name='dispatch')
class FiltroContatosList(ContatosList):
    # FILTRO DO HOME CONTANTOS
    def get_queryset(self):
        qs = super().get_queryset()
        termo = self.request.GET.get('termo')

        campos = Concat('nome', Value(' '), 'sobrenome')
        qs = qs.annotate(
            nome_completo=campos
            ).filter(Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo))
        return qs
    
@method_decorator(login_required(login_url='login'), name='dispatch')
class ContatoDetalhes(UpdateView):
    # ATUALIZANDO UM CONTATO
    template_name = 'contatos/contato.html'
    model = Contato
    form_class = FormContato
    context_object_name = 'contato'

    # def form_valid(self, form):
    #     form.save()
    #     messages.success(self.request, 'Contato editado com sucesso!')
    #     return redirect('contato', self.get_object().id)
   
    def get_success_url(self):
        messages.success(self.request, 'Contato editado com sucesso!')
        return reverse_lazy('contato', kwargs={'pk': self.get_object().id})
    

@method_decorator(login_required(login_url='login'), name='dispatch')
class PostCategoria(View):
    def post(self, *args, **kwargs):
        form = FormCategoria(self.request.POST)
        if form.is_valid():
            form.save()
            messages.success(self.request, 'Novo contato inserido com sucesso!')
            return redirect('/')
        messages.error(self.request, 'Dados inválidos!')
        return redirect('/')

@method_decorator(login_required, name='dispatch')
class ContatoDeleteView(View):
    def get(self, *args, **kwargs):
        contato = Contato.objects.get(id=kwargs['pk'])
        contato.delete()
        messages.success(self.request, 'Contato deletado com sucesso!')
        return redirect('home')
