import disnake
from disnake import Intents
from disnake.ext import commands

import aiosqlite

import os
from dotenv import load_dotenv

from datetime import datetime, timezone, timedelta

import logging as log

'Veja sobre a biblioteca logging para entender como funciona isso aqui e como usar'
log.basicConfig(level=log.INFO, filename='logs.log', format='%(asctime)s - %(levelname)s - %(message)s')

load_dotenv()

TOKEN = os.getenv("TOKEN")


class MyBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.persistent_views_added = False

    async def on_ready(self):
        atividade = disnake.Game(name="no Inhouse Academy")
        await self.change_presence(status=disnake.Status.online, activity=atividade)

        'Aqui é onde torna um botão, selecmenu ou modal em persistente, ou seja, mesmo que reinicie o bot, continuará funcionando'
        if not self.persistent_views_added:
            '''
            Para fazer algo persistente, só escrever self.add_view(Colocar aqui o diretório do arquivo .py onde está localizado a classe que vc quer deixar persistente)'
            colocar o (bot) para habilitar os comandos lá dentro da persistente, pois sem isso o comando não funcionará'''
            # self.add_view(Scrim.ScrimBotao(bot))
            self.persistent_views_added = True


        print(f'Bot {self.user} foi iniciado!!')
        log.info(f'\n=======================================\n\nBot {self.user} foi iniciado!\n\n=======================================')


    '''
    Caso precise do horarío de agora no nosso timezone, chame essa função dessa forma num cog:
    horario_atual = await self.bot.obter_horario_atual
    
    Essa função puxa tanto o horario quanto a data, caso queira só o horario ou a data só alterar abaixo.
    '''
    async def obter_horario_atual(self):
        data_hora_gmt_3 = datetime.now().astimezone(timezone(timedelta(hours=-3)))
        horario = f'{data_hora_gmt_3.strftime("%d/%m/%Y")} às {data_hora_gmt_3.strftime("%H:%M:%S")}'
        return horario


    '''
    Use essa função para executar um comando de INSERT ou UPDATE no database,'
    Dentro de um cog, ou seja, de outro arquivo fora o main.py, você deve usar o comando da seguinte forma:
    await self.bot.execute("INSERT INTO Scrim_times(Coloque aqui todos os valores separados por virgula que serão inseridos no database) VALUES(Insira a quantidade de valores que serão inseridos com ? e separando por virgula) WHERE Scrim_n = ?", insira aqui a variável do scrim_n)
    await self.bot.execute(f"UPDATE Scrim_times SET Time = "{variavel do time aqui}" WHERE Scrim_n = '{variavel scrim_n}' ")'''
    async def execute(self, query, *values):
        async with aiosqlite.connect("database.db") as db:
            async with db.cursor() as cur:
                await cur.execute(query, tuple(values))
            await db.commit()

    '''
    Essa função serve para buscar vários valores no database com um SELECT, retornará os valores em uma tupla onde você pode chamar cada valor indivualmente ou usar a todos de uma vez
    dados =  await self.bot.buscar("SELECT Time, Id, Usuario from Scrim_times WHERE Scrim_n = '{variavel scrim_n}' ")
    
    caso queira usar os valores indivualmente, fazer assim:
    
    time = dados[0]
    id = dados[1]
    usuario = dados[2]
    
    claro que se quiser, não precisa guardar os dados em uma variavel, já pode usar direto dados[posição da variavel] direto a onde vc vai precisar dela
    '''
    async def buscar(self, query, *values):
        async with aiosqlite.connect("database.db") as db:
            async with db.cursor() as cur:
                exe = await cur.execute(query, tuple(values))
                row = await exe.fetchone()
            if len(row) <= 0:
                row = None
            return row

    'buscar_id é igual o buscar, porém pra pegar somente um valor, sua função é identica a de cima com essa unica diferença, use como achar melhor'
    async def buscar_id(self, query, *values):
        async with aiosqlite.connect("database.db") as db:
            async with db.cursor() as cur:
                exe = await cur.execute(query, values)
                row = await exe.fetchmany(size=5)
            if len(row) > 0:
                row = [r for r in row[0]]
            else:
                row = '9'
            return str(row[0])


'Não mexer aqui'
intents = Intents.default()
intents.message_content = True
intents.members = True

'Não mexer aqui'
bot = MyBot(intents=intents, command_prefix='@@')
bot.remove_command('help')


'Esse é o comando que carrega todas as cogs do bot dentro do arquivo /Comandos'
bot.load_extensions('./Comandos')
