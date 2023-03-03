
from django.views.generic import View, TemplateView, ListView
from django.shortcuts import redirect, get_object_or_404,render
from contatos.forms import FormContato
from django.contrib import messages
from contatos.models import Contato
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import Http404
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat






@method_decorator(
    login_required(login_url='login', redirect_field_name='next'),
    name='dispatch'
)
class DashboardContatos(View):

    def get_contato(self, id):
        contato = None
        if id:
            contato = get_object_or_404(Contato, id=id)
        return contato
    
    def get(self, request, id):
        return redirect(f'/contato/{id}')

    def post(self, request, id=None):

        if not id:
            form = FormContato(request.POST, request.FILES)
            if form.is_valid():
                user = form.save(commit=False)
                user.user = request.user
                user.save()
                messages.success(request, 'Contato cadastrado com sucesso!')      
                return redirect('home')
            else:
                messages.info(request, 'Dados inválidos, tente novamente!')      
                return redirect('home')    


        contato = self.get_contato(id=id)
        form = FormContato(request.POST or None, 
                           request.FILES or None, 
                           instance=contato)
        if form.is_valid():
            user = form.save(commit=False)
            user.user = request.user
            user.save()
            messages.success(request, 'Contato editado com sucesso!')
            return redirect(f'/contato/{id}')
        else:
            messages.success(request, 'Dados incorretos!!')
            return redirect(f'/contato/{id}')
        

class ContatoDelete(DashboardContatos):
    def get(self, request, id=None):
        contato = self.get_contato(id)
        contato.delete()
        messages.success(request, 'Contato deletado com sucesso!')
        return redirect('home')
    


class ContatoDetail(TemplateView):
    template_name = 'contatos/contato.html'


    def get_context_data(self, id,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        contato = get_object_or_404(Contato, id=id)
        form = FormContato(instance=contato)


        if self.request.user != contato.user:
            raise Http404
        
        context.update({'contato': contato, 'form': form})
        return context
    

class HomeDetail(TemplateView):
    template_name = 'contatos/home.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        contatos = Contato.objects.order_by('nome').filter(user=self.request.user)
        pesquisa = self.request.POST.get('pesquisa')
        
        campos = Concat('nome', Value(' '), 'sobrenome')

        if pesquisa:
            contatos = contatos.annotate(nome_completo=campos).filter(Q(nome_completo__icontains=pesquisa) | Q(telefone__icontains=pesquisa))

        form = FormContato
        # PAGINAÇÃO 
        paginator = Paginator(contatos, 6)
        page = self.request.GET.get('p')
        contatos = paginator.get_page(page)

        context.update({'contatos': contatos, 'form': form})
        return context
    
