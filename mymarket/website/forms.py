from django import forms

from financeiro.models import Pessoa, Usuario, Telefone, Endereco, Bairro, Cidade, Estado

class PessoaForm(forms.ModelForm):

    class Meta:
        model = Pessoa
        fields = ('nome', 'sexo', 'cpf', 'data_nasc', 'email', 'est_cad', 'senha')

class EstadoForm(forms.ModelForm):

    class Meta:
        model = Estado
        fields = ('sigla',)

class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ('foto', 'obs')

class BairroForm(forms.ModelForm):

    class Meta:
        model = Bairro
        fields = ('nome_bairro',)

class TelefoneForm(forms.ModelForm):

    class Meta:
        model = Telefone
        fields = ('numero', 'numero2')

class EnderecoForm(forms.ModelForm):

    class Meta:       
        model = Endereco
        fields = ('cep', 'logradouro', 'complemento', 'numero')

class CidadeForm(forms.ModelForm):
    
    class meta:
        model = Cidade
        fields = ('nome_cidade',)


