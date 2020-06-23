import sys
from django.template import RequestContext
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from financeiro.models import Produto
from .forms import PessoaForm, UsuarioForm, TelefoneForm, EnderecoForm, EstadoForm, BairroForm, CidadeForm

sys.path.append("..")

def helloWorld(request):
    return HttpResponse('teste')

def home(request):
    produtos1 = Produto.objects.all()
    produtos2 = Produto.objects.all()
    produtos3 = Produto.objects.all()
    return render(request, 'website/index.html', {'produtos1':produtos1, 'produtos2':produtos2, 'produtos3':produtos3})

def produtoView(request, id):
    produto = get_object_or_404(Produto, pk=id)
    return render(request, 'website/produto_view.html', {'produto':produto})

def carrinho(request):
    return render(request, 'website/cart.html')

def cadastrar_usuario(request):
    
    if request.method == 'POST':
    
        form = PessoaForm(request.POST)
        tel = TelefoneForm(request.POST)
        end = EnderecoForm(request.POST)
        bai = BairroForm(request.POST)
        est = EstadoForm(request.POST)

        if (form.is_valid() and tel.is_valid() and end.is_valid() and bai.is_valid() and est.is_valid()): # and tel.is_valid() and end.is_valid() and end1.is_valid() and end2.is_valid() and end3.is_valid()):
            
            pessoa = form.save(commit=False)
            id_pessoa = pessoa.id
            pessoa.save()
            
            telefone = tel.save(commit=False)
            telefone.save()
            
            endereco = end.save()
            endereco.save()
            
            bairro = bai.save()
            bairro.save()

            estado = est.save()
            estado.save()

            return redirect('/')
    
    else:
        tel = TelefoneForm()
        end = EnderecoForm()
        bai = BairroForm()          
        form = PessoaForm()
        est = EstadoForm()
        
        return render(request, 'website/cadastro.html', {'form':form, 'tel':tel, 'end': end, 'bai':bai, 'est':est}) #, 'tel':tel, 'end':end, 'end1':end1, 'end2':end2, 'end3':end3})
    
    return render(request, 'website/cadastro.html', {'form':form, 'tel':tel, 'end':end, 'bai':bai, 'est':est}) #, 'tel':tel, 'end':end, 'end1':end1, 'end2':end2, 'end3':end3})

def cadastrar_produto(request):
    return render(request, 'website/produto.html')

'''
def usuario(request):
    return render(request, 'website/usuario.html', {'name':self.name})
'''

def contato(request):
    return render(request, 'website/contato.html')

def parceiros(request):
    return render(request, 'website/parceiros.html')

def assinante(request):
    return render(request, 'website/assinante.html')

def localidades_atendidas(request):
    return render(request, 'website/localidades.html')

def login(request):
    return render(request, 'website/login.html')

def cat_alimentos(request):
    return render(request, 'website/cat_alimentos.html')

def cat_bebidas(request):
    return render(request, 'website/cat_bebidas.html')

def cat_hortifruti(request):
    return render(request, 'website/cat_hortifruti.html')

def cat_utilitarios(request):
    return render(request, 'website/cat_utilitarios.html')

def cat_limpeza(request):
    return render(request, 'website/cat_limpeza.html')

def cat_higiene(request):
    return render(request, 'website/cat_higiene.html')

def cat_pet(request):
    return render(request, 'website/cat_pet.html')

def cat_todos(request):
    return render(request, 'website/cat_todos.html')

def produtos_todos(request):
    produtos = Produto.objects.all()
    return render(request, 'website/produtos_todos.html', {'produtos': produtos})

def fornecedores(request):
    return render(request, 'website/fornecedores.html')

# Create your views here.
