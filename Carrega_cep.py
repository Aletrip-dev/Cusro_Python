import requests
import json
from C_Endereco import Endereco #chama a classe endereço
cep = input('Informe um CEP') #solicita a informação do CEP
r = requests.get("http://www.viacep.com.br/ws/%s/json/"%cep)
 
if r.status_code == requests.codes.ok:
    j = json.loads(r.text)
    Endereco = Endereco()
    Endereco.cep = j['cep']
    Endereco.logradouro = j['logradouro']
    Endereco.complemento = j['complemento']
    Endereco.bairro = j['bairro']
    Endereco.localidade = j['localidade']
    Endereco.uf = j['uf']
    Endereco.unidade = j['unidade']
    Endereco.ibge = j['ibge']
    Endereco.gia = j['gia']

    Endereco.salvar()
else:
    print("cep não encontrado")

