from django.shortcuts import render, redirect
from .models import Produtos
from django.http import HttpResponse
def Home(request):
    return render(request, 'front/home.html')

def ProdutosCad(request):
    try:
        newProduct = Produtos()
        newProduct.nome = request.POST.get('nome')
        newProduct.tipo = request.POST.get('tipo')
        newProduct.valor = request.POST.get('valor')
        newProduct.stq = request.POST.get('estoque')
        newProduct.save()
        produtos = {
            'produtos': Produtos.objects.all()
        }
        return render(request, 'front/produtos.html', produtos)
    except Exception as e:
        print(f"ocorreu um erro: {e}")
        mensagem_erro = "Ocorreu um erro durante o processamento. Por favor, tente novamente."
        return render(request, 'home.html', {'mensagem de erro': mensagem_erro})

def Listaprodutos(request):
    try:
        produtos = {
            'produtos': Produtos.objects.all()
        }
        return render(request, 'front/listaprodutos.html', produtos)
    except Exception as e:
        print(f"Ocorreu um erro durante a busca de produtos: {e}")
        mensagem_erro = "Ocorreu um erro ao buscar os produtos. Por favor, tente novamente."
        return render(request, 'home.html', {'mensagem_erro': mensagem_erro})
def Editar(request, id):
    produto = {
      'produto': Produtos.objects.get(id=id)
    }
    return render(request, 'front/editar.html', produto)

def Update(request, id):
    try:
        newproduct = Produtos.objects.get(id=id)

        # Armazene os valores atuais antes da atualização
        nome_anterior = newproduct.nome
        tipo_anterior = newproduct.tipo
        valor_anterior = newproduct.valor
        estoque_anterior = newproduct.stq

        if 'nome' in request.POST:
            newproduct.nome = request.POST.get('nome', nome_anterior)
        if 'tipo' in request.POST:
            newproduct.tipo = request.POST.get('tipo', tipo_anterior)
        if 'valor' in request.POST:
            newproduct.valor = request.POST.get('valor', valor_anterior)
        if 'estoque' in request.POST:
            newproduct.stq = request.POST.get('estoque', estoque_anterior)

        newproduct.save()

        # Atualize a lista de produtos após a alteração
        produtos = {
            'produtos': Produtos.objects.all()
        }

        mensagem_sucesso = "Produto atualizado com sucesso."
        return render(request, 'front/listaprodutos.html', {'produtos': produtos, 'mensagem_sucesso': mensagem_sucesso})
    except Exception as e:
        print(f"Ocorreu um erro durante a atualização: {e}")
        mensagem_erro = f"Ocorreu um erro durante a atualização: {e}. Tente novamente."
        return render(request, 'front/editar.html', {'produto': newproduct, 'mensagem_erro': mensagem_erro})

def Delete(request,id):
    produto = Produtos.objects.get(id=id)
    produto.delete()
    produtos = {
        'produtos': Produtos.objects.all()
    }
    return render(request, 'front/listaprodutos.html', produtos)

def Busca(request):
    if request.method == 'POST':
        busca = request.POST.get('busca')
        tipo = request.POST.get('tipo')
        if tipo == 'nome':
            resultados = Produtos.objects.filter(nome__icontains=busca)
        elif tipo == 'tipo':
            resultados = Produtos.objects.filter(tipo__icontains=busca)
        elif tipo == 'id':
            resultados = Produtos.objects.filter(id__icontains=busca)
        else:
            resultados = []

        resultados = {
            'resultados': resultados,
            'tipo': tipo,
        }

        return render(request, 'front/busca.html', resultados)
    else:
        return render(request, 'front/listaprodutos.html')