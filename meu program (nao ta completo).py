from instabot import Bot
from time import sleep
import os
import glob

cookie_del = glob.glob("config/*cookie.json")
os.remove(cookie_del[0])


thiisp = Bot()


print('Olá, seja bem vindo :)')
print('''
Não execute esse programa 2 vezes ou mais ao mesmo tempo! (caso ignore isso, você poderá ter o insta bloqueado.)
''')

nome = str(input('Digite o seu usuário: '))
senha = str(input('Digite a sua senha: '))

thiisp.login(username=nome, password=senha)

print(f'''

Seja bem vindo, {nome}!

''')
escolha = int(input('''O que você deseja fazer?

( 1 ) Visualizar storys automaticamente.
( 2 ) Parar de seguir quem não me segue de volta.
( 3 ) Curtir storys de alguma pessoa.

Escolha uma alternativa: '''))

if escolha == 2:
    thiisp.unfollow_non_followers()

elif escolha == 3:
    usuario01 = str(
        input('Digite o @ do Usuário que você deseja curtir as fotos: '))
    quantidade01 = int(
        input('Digite a quantidade de fotos que você deseja curtir: '))
    thiisp.like_user(usuario01, amount=quantidade01)

thiisp.unfollow_non_followers()
