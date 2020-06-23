from django.db import models
from django.core.files.storage import FileSystemStorage
from django.utils.html import mark_safe

fs = FileSystemStorage(location='/home/felipe/dev/VirtualShop/mymarket/website/static/images')

class Image(object):

    def image_tag(self, image):
        self.image = image
        return mark_safe('<img src="/home/felipe/dev/VirtualShop/mymarket/financeiro/images/users/%s" />' %(self.image))

    image_tag.short_description = 'Image'

class Estado(models.Model):
    
    ESTADO = [
        ('al','Alagoas'),
        ('am','Amazonas'),
        ('ap','Amapá'),
        ('ba','Bahia'),
        ('ce','Ceará'),
        ('df','Distrito Federal'),
        ('es','Espírito Santo'),
        ('go','Goiás'),
        ('ma','Maranhão'),
        ('mt','Mato Grosso'),
        ('ms','Mato Grosso do Sul'),
        ('mg','Minas Gerais'),
        ('pa','Pará'),
        ('pb','Paraíba'),
        ('pr','Paraná'),
        ('pe','Pernambuco'),
        ('pi','Piauí'),
        ('rj','Rio de Janeiro'),
        ('rn','Rio Grande do Norte'),
        ('ro','Rondônia'),
        ('rs','Rio Grande do Sul'),
        ('rr','Roraima'),
        ('sc','Santa Catarina'),
        ('se','Sergipe'),
        ('sp','São Paulo'),
        ('to','Tocantins'),
        ]

    sigla = models.CharField(max_length=2, null=False, choices=ESTADO)

class Cidade(models.Model):

    nome_cidade = models.CharField(max_length=20, null=False)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

class Bairro(models.Model):

    nome_bairro = models.CharField(max_length=40, null=False)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

class Endereco(models.Model):

    bairro = models.ForeignKey(Bairro, on_delete=models.CASCADE)
    logradouro = models.CharField(max_length=120, null=False)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=120, null=True)
    cep = models.CharField(max_length=8)

class Telefone(models.Model):

    numero = models.CharField(max_length=11, null=False, unique=True)
    numero2 = models.CharField(max_length=11, null=True, blank=True)

class Pessoa(models.Model):

    TITLE_CHOICES = [
        ('M','Masculino'),
        ('F','Feminino'),
            ]

    cpf = models.CharField(max_length=11, unique=True)
    nome = models.CharField(max_length=40, null=False)
    data_nasc = models.DateField(null=False)
    sexo = models.CharField(max_length=1, null=False, choices=TITLE_CHOICES)
    email = models.EmailField(max_length=100, null=False)
    est_cad = models.CharField(max_length=1)
    senha = models.CharField(max_length=150, null=False)
    telefone = models.ForeignKey(Telefone, on_delete=models.CASCADE)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Usuario(models.Model):

    foto = models.ImageField(storage=fs, null=True)
    obs = models.TextField()
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

class Funcionario(models.Model):

    funcao = models.CharField(max_length=20, null=False)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

class Fornecedor(models.Model):

    razao_social = models.CharField(max_length=120, null=False)
    cnpj = models.CharField(max_length=14, null=False)
    nome_fantasia = models.CharField(max_length=120, null=False)
    obs = models.TextField()
    telefone = models.ForeignKey(Telefone, on_delete=models.CASCADE)

class Endereco_fornecedor(models.Model):

    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)

class Categoria(models.Model):

    categoria = models.CharField(max_length=120, null=False)

    def __str__(self):
            return self.categoria
    
class Oferta(models.Model):

    nome_desconto = models.CharField(max_length=20, null=False)
    preco_desc = models.IntegerField(null=False)
    imagem_oferta = models.ImageField(storage=fs, blank=True, null=True)
    data_desc = models.DateField(null=False)

    def __str__(self):
        return self.nome_desconto

class Produto(models.Model):

    nome = models.CharField(max_length=100, null=False)
    preco = models.DecimalField(null=False, decimal_places=2, max_digits=10)
    imagem = models.ImageField(storage=fs, null=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    oferta = models.ForeignKey(Oferta, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome

class Fornecedor_categoria(models.Model):

    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)

class Fornecedor_produto(models.Model):

    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)

class Cesta(models.Model):

    nome_cesta = models.CharField(max_length=100, null=False)
    preco_cesta = models.DecimalField(null=False, decimal_places=2, max_digits=10)
    imagem = models.ImageField(storage=fs, null=False)
    obs = models.TextField()
    
    def __str__(self):
        return self.nome_cesta

class Cesta_produtos(models.Model):

    cesta = models.ForeignKey(Cesta, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)


    
    
