from django.db import models
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='/images')

class Pessoa(models.Model):

    cpf = models.CharField(max_length=11, unique=True)
    nome = models.CharField(max_length=40, null=False)
    data_nasc = models.DateField(null=False)
    sexo = models.CharField(max_length=1, null=False)
    email = models.EmailField(max_length=100, null=False)
    est_cad = models.CharField(max_length=1)
    senha = models.CharField(max_length=150, null=False)

class Usuario(models.Model):

    foto = models.ImageField(storage=fs, null=True)
    obs = models.TextField()
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE())

class Endereco(models.Model):

    bairro = models.ForeignKey(Bairro, on_delete=models.CASCADE())
    logradouro = models.CharField(max_length=120, null=False)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=120, null=True)

class Endereco_usuario(models.Model):

    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE())
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE())

class Bairro(models.Model):

    nome_bairro = models.CharField(max_length=40, null=False)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE())

class Cidade(models.Model):

    nome_cidade = models.CharField(max_length=20, null=False)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE())

class Estado(models.Model):

    sigla = models.CharField(max_length=2, null=False)

class Telefone(models.Model):

    numero = models.CharField(max_length=11, null=False, unique=True)

class Telefone_usuario(models.Model):

    telefone = models.ForeignKey(Telefone, on_delete=models.CASCADE())
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE())

class Funcionario(models.Model):

    funcao = models.CharField(max_length=20, null=False)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE())

class Fornecedor(models.Model):

    razao_social = models.CharField(max_length=120, null=False)
    cnpj = models.CharField(max_length=14, null=False)
    nome_fantasia = models.CharField(max_length=120, null=False)
    obs = models.TextField()

class Endereco_fornecedor(models.Model):

    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE())
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE())

class Telefone_fornecedor(models.Model):

    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE())
    telefone = models.ForeignKey(Telefone, on_delete=models.CASCADE())

class Categoria(models.Model):

    categoria = models.CharField(max_length=120, null=False)

class Produto(models.Model):

    nome = models.CharField(max_length=100, null=False)
    preco = models.DecimalField(null=False)
    imagem = models.ImageField(storage=fs, null=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE())
    oferta = models.ForeignKey(Oferta, on_delete=models.CASCADE())

class Oferta(models.Model):

    preco_desc = models.DecimalField(null=False)
    imagem_oferta = models.ImageField(storage=fs)
    data_desc = models.DateField(null=False)

class Fornecedor_categoria(models.Model):

    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE())
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE())

class Fornecedor_produto(models.Model):

    produto = models.ForeignKey(Produto, on_delete=models.CASCADE())
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE())






    
    
    
