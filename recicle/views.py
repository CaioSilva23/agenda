# from django.shortcuts import render, get_object_or_404, redirect
# from .models import Contato
# from django.core.paginator import Paginator
# from django.db.models import Q, Value
# from django.db.models.functions import Concat
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from .forms import FormContato

# @login_required(login_url='login')
# def home(request):
#     form = FormContato()
#     contatos = Contato.objects.order_by('nome').filter(user=request.user)
#     pesquisa = request.POST.get('pesquisa')
    
#     campos = Concat('nome', Value(' '), 'sobrenome')

#     if pesquisa:
#         contatos = contatos.annotate(nome_completo=campos).filter(Q(nome_completo__icontains=pesquisa) | Q(telefone__icontains=pesquisa))

#     # PAGINAÇÃO 
#     paginator = Paginator(contatos, 6)
#     page = request.GET.get('p')
#     contatos = paginator.get_page(page)

#     return render(request, 'contatos/home.html', {'contatos': contatos, 'form':form})


# def contato(request, id):
#     contato = get_object_or_404(Contato, id=id)
#     form = FormContato(instance=contato)
#     if request.user != contato.user:
#         messages.info(request, 'Esse contato não é seu!')
#         return redirect('home')
#     return render(request, 'contatos/contato.html', {'contato': contato,'form': form})


# def novo_contato(request):
#     if request.method == 'GET':
#         return redirect('home')
#     elif request.method == 'POST':
#         form = FormContato(request.POST, request.FILES)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.user = request.user
#             user.save()
#             messages.success(request, 'Contato cadastrado com sucesso!')
#             return redirect('home')
#         else:
#             return redirect('home')


# def editar_contato_id(request, id):
#     contato = get_object_or_404(Contato, id=id)

#     if request.method == 'GET':
#         return redirect('home')
    
#     elif request.method == 'POST':
#         form = FormContato(request.POST, request.FILES, instance=contato)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.user = request.user
#             user.save()
#             messages.success(request, 'Contato editado com sucesso!')
#             return redirect(f'/contatos/contato/{id}')
#         else:
#             return redirect('home')


# def deletar(request, id):
#     contato = get_object_or_404(Contato, id=id)
#     contato.delete()
#     messages.success(request, 'Contato deletado com sucesso!')
#     return redirect('home')