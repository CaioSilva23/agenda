from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Contato
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def home(request):
    contatos = Contato.objects.order_by('nome')
    pesquisa = request.POST.get('pesquisa')
    
    campos = Concat('nome', Value(' '), 'sobrenome')

    if pesquisa:
        contatos = contatos.annotate(nome_completo=campos).filter(Q(nome_completo__icontains=pesquisa) | Q(telefone__icontains=pesquisa))

    # PAGINAÇÃO 
    paginator = Paginator(contatos, 6)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/home.html', {'contatos': contatos})


def contato(request, id):
    contato = get_object_or_404(Contato, id=id)
    return render(request, 'contatos/contato.html', {'contato': contato})
