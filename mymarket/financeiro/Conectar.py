import MySQLdb
import re

class Connector(object):
    pass

    ''' Connector of the database for the class.'''
    def __init__(self):
        try:
            self.con = MySQLdb.connect(host="localhost", user="root")
            self.con.select_db('db_mymarket')

            self.cursor = self.con.cursor()
        except ValueError:
            print("Não foi possível se conectar ao banco de dados!")

    ''' Write data to the database '''
    def Executar(self, script):

        self.script = script

        try:
            print(self.script)

            self.cursor.execute('%s' %self.script)
            dec = input("Deseja realmente salvar os dados?")
            if (dec == 'sim' or dec == 'Sim'):
                self.con.commit()
            else:
                print('você decidiu não salvar os dados!')

        except ValueError:
            print("Não foi possível se conectar ao banco de dados!")

    ''' Consult data of the database. Specifically ddd. '''
    def Consultar(self, script):

        self.script = script

        try:
            print(script)

            self.cursor.execute('%s' %self.script)
            result = self.cursor.fetchone()
            return result
        except ValueError:
            print("Não foi possível se conectar ao banco de dados!")

    def Validar_Dados(self, email, cpf, cnpj, telefone):

        validar = ''

        self.Consultar()












'''
valor = 11
Teste = Connector()
result = Teste.Consultar('call localizar_ddd(%s)' %(valor))
regex = re.compile('[(,)]')
subs = regex.sub('', str(result))
print(subs)
'''


""" 
    List of created procedures
    
        
        
"""
