
from django.views.generic import View, TemplateView, ListView, DetailView
from django.shortcuts import redirect, get_object_or_404,render
from contatos.forms import FormContato
from django.contrib import messages
from contatos.models import Contato
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import Http404, HttpResponse
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat


@method_decorator(
    login_required(login_url='login', redirect_field_name='next'),
    name='dispatch'
)



class ContatosDetail(DetailView):
    model = Contato
    context_object_name = 'contato'
    template_name = 'contatos/contato.html'
    
    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        form = FormContato(instance=self.get_object())
        ctx.update({'form': form})
        return ctx
    
    def post(self, *args, **kwargs):
        form = FormContato(self.request.POST or None, 
                            self.request.FILES or None, 
                            instance=self.get_object())
        if form.is_valid():
            user = form.save(commit=False)
            user.user = self.request.user
            user.save()
            messages.success(self.request, 'Contato editado com sucesso!')      
            return redirect(f'/contato/{self.get_object().id}/')
        else:
            messages.info(self.request, 'Dados inválidos, tente novamente!')  
            return redirect(f'/contato/{self.get_object().id}/')


class ContatosList(ListView, Paginator):
    model = Contato
    template_name = 'contatos/home.html'
    context_object_name = 'contatos'
    ordering = 'nome'
    
    def paginater(self, contatos):
        paginator = Paginator(contatos, 6)
        page = self.request.GET.get('p')
        contatos = paginator.get_page(page)
        return contatos

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        form = FormContato()
     
        contatos = self.paginater(self.get_queryset())
        ctx['contatos'] = contatos
        ctx.update({'form': form})
        print(ctx)
        return ctx
    
    def post(self, *args, **kwargs):
        form = FormContato(self.request.POST or None, 
                            self.request.FILES or None, 
                            )
        if form.is_valid():
            user = form.save(commit=False)
            user.user = self.request.user
            user.save()
            messages.success(self.request, 'Contato salvo com sucesso!')  
            return redirect('home')
        else:
            messages.error(self.request, 'Error ao salvar o contato, tente novamente!')  
            return redirect('home')


class ContatoDelete(ContatosDetail):
    def get(self, *args, **kwargs):
        contato = Contato.objects.get(id=kwargs['pk'])
        contato.delete()
        messages.success(self.request, 'Contato deletado com sucesso!')
        return redirect('home')
