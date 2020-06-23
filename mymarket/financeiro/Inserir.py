from Conectar import Connector
import MySQLdb
import re

class Insert(object):

    def __init__(self):
        self.Inserir = Connector()

    def Insert_user(self, cpf, nome, data_nasc, sexo, email, est_cad, senha, foto, obs, telefone):

        pessoa = 'insert into Pessoa(cpf, nome, data_nasc, sexo, email, est_cad, senha) values (%s, "%s", "%s", "%s", "%s", "%s", "%s")' %(cpf, nome, data_nasc, sexo, email, est_cad, senha)
        user = 'insert into Usuario(foto, obs) values ("%s", "%s")' %(foto, obs)
        Tel = 'insert into Telefone(numero) value ("%s")' %(telefone)

        try:
            fail = self.Inserir.Executar(pessoa)
            print(fail)
            fail = self.Inserir.Executar(user)
            print(fail)
            fail = self.Inserir.Executar(Tel)
            print(fail)

            id_user = self.Inserir.Consultar('call localizar_id_usuario("%s")' %(email))
            print(id_user)

            formatar = re.compile('[(,)]')
            id_user = formatar.sub('', str(id_user))
            print(id_user)

            rela_tel = 'call relacionar_telefone(%s, "%s")' %(id_user, telefone)
            print(rela_tel)
            rela_user = 'call relacionar_usuario("%s", %s)' %(email, id_user)
            print(rela_user)
            rela_user_tel = 'call relacionar_telefone_usuario(%s, "%s")' %(id_user, telefone)
            print(rela_user_tel)

            self.Inserir.Executar(rela_tel)
            self.Inserir.Executar(rela_user)
            self.Inserir.Executar(rela_user_tel)

        except MySQLdb._exceptions.IntegrityError:
            print("Dados já cadastrados, por gentileza, verificar e-mail, cpf ou número de telefone!")
            fail = 1
            return fail
        except:
            print("Não foi possível conectar-se ao banco de dados, por gentileza contate o administrador do sistema!")

    def Insert_provider(self, cnpj, razao_social, nome_fantasia, obs,):

        id_pessoa
        cpf
        nome
        data_nasc
        sexo
        email
        est_cad
        id_telefone
        senha
        not null


    def Insert_product(self):
        pass

Inserir = Insert()
Inserir.Insert_user('38446353825', 'Felipe Maeda', '2000-4-28', 'M', 'MAEDAXd@gmail.com', 'A', 'Maeda555', 'foto.png', 'Obs', '14975857066')