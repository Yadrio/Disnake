Comentei em todos os arquivos pra explicar o basico de como usar tudo, só ir paginando tudo, qualquer coisa pergunta


Para todo comando que criar(botoes, modais etc), colocar dentro da pasta Comandos

Para toda função que criar, colocar dentro da pasta Funções como um novo arquivo explicando que tipo de funções estão ali


Onde estiver 'pass' é onde voce configurara seu comando, pass serve só para não der erro na hora de iniciar o bot

Biblioteca Disnake no GitHub, contém exemplos de como fazer as coisas básicas, comandos, botoes, menus etc
https://github.com/DisnakeDev/disnake


Formatações de texto e embeds no discord
https://c.r74n.com/discord/formatting



A seguir, exemplos de como fazer o básico na biblioteca
obs: praticamente todos os comandos na biblioteca disnake são assíncronos, então não esqueça de colocar await antes dos comandos



## Comando simples usando preffix
    @bot.command()
    async def nome_do_comando(ctx):
        pass


## Slash command
    @bot.slash_command(name='', description='')     
    async def scrim(self, inter: disnake.ApplicationCommandInteraction):

Voce pode colocar só "inter" na declaração da interaction, ela puxa todos os metodos que existe porem, não exibirá as opções, ai tem q consultar a documentação ou saber de cabeça

## Descrição em comandos, importar isso:
    from disnake.ext.commands import Param

## Exemplo de uso:
    @bot.slash_command(name='', description='')     
    async def scrim(self, inter: disnake.ApplicationCommandInteraction,
                    texto: str = Param(description='Insira a descrição da opções aqui')):





## Cog
Você usará cogs quando precisar criar outro arquivo com comandos dentro, seja comando com preffix ou slash


    class Comandos(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='', description='')
    async def comando_nome(self, inter):
        'Codigo do comando aqui'

    def setup(bot):
    bot.add_cog(Comandos(bot))


Para declarar a cog e colocar o comando dentro, precisa criar uma classe necessariamente, e nas ultimas linhas do arquivo deve estar a função setup, que servirá como "bootar" a cog e puxar a variavel bot da classe principal da main

#### Note, para declarar comandos dentro da classe da cog, a sintaxe do decorator muda, conforme os exemplos:
    @commands.slash_command - Para slash commands
    async def slash(self):

    @commands.command() - Para comando com preffix
        from disnake.ext import commands













# Botão
#### Há 2 formas de criar botões, a primeira é criar um classe disnake.ui.View e colocar os botoes com decorators, a segunda forma é criar uma classe View e uma classe disnake.ui.Button, então usar a classe view para chamar a classe Button, isso é útil quando os dados do botão não forem determinados e quando tiver varios botoes então usar um loop for. 
    
    Botão com decorator

    class Exemplo_botão(disnake.ui.View):
        def __init__(self, bot):
            self.bot = bot
            super().__init__(timeout=None)

    @disnake.ui.button(style=ButtonStyle.green, custom_id='sim', emoji='✔️')
    async def sim(self, button: disnake.ui.Button, inter):
        'response do botão aqui'

    @disnake.ui.button(style=ButtonStyle.green, custom_id='não', emoji='✔️')
    async def nao(self, button: disnake.ui.Button, inter):
        'response do botão aqui'


    Botão sem decorator

    class Horario(ui.View):
        def __init__(self, bot):
            super().__init__(timeout=None)
    
        self.add_item(self.Horario_botao(bot=bot, 
                                         label='Nome botão', 
                                         style=ButtonStyle.green, 
                                         custom_id='id custom', 
                                         emoji='🔥'))


    class Horario_botao(ui.Button):
        def __init__(self, bot, label, style, custom_id, emoji):
    
            super().__init__(label=label, style=style, custom_id=custom_id, emoji=emoji)

        async def callback(self, inter: MessageInteraction):
            'response do botão aqui'




# Select menu
Menus selecionaveis, aquela caixa preto que contem opções, é assim que faz, só seguir o exemplo
    class Confirmação_finalizar_menu(disnake.ui.StringSelect):
        def __init__(self, bot):
            self.bot = bot
        
        # aqui em options, recebe a lista de todas as opções que serão exibidas ao clicar, só seguir o exemplo
        options = [
            disnake.SelectOption(
                label="Titulo da opção 1 aqui", description=f"Descrição da opção aqui", emoji="1️⃣"
            ),
            disnake.SelectOption(
                label="Titulo da opção 2 aqui", description=f"Descrição da opção aqui", emoji="2️⃣"
            ),
        ]

        super().__init__(
            placeholder="Coloque aqui que será exibido antes de clicar na caixa de seleção",
            min_values=1, # minimo de valores que o usuario pode escolher
            max_values=1, # maximo de valores que o usuario pode escolher
            options=options,
        )

    async def callback(self, inter: disnake.MessageInteraction):
        'response do select option'
         
Você pode fazer um match case com "self.values[0]" para filtrar qual opção do select o usuario selecionou




# Modal

    class SelectModal(disnake.ui.Modal):
        def __init__(self, bot):
            self.bot = bot


        nome = ui.TextInput(label='Titulo do modal',
                            placeholder="Texto que será exibido na caixa de escrita, antes do usuario digitar algo, como um exemplo de como fazer",
                            style=TextInputStyle.short, # tamanho da caixa de opção, veja a documentação pra ver detalhes
                            max_length=20, # maximo de caracteres que o usuario pode inserir
                            custom_id="id_custom_do_modal") 

        super().__init__(title=f"{title}", custom_id="criar_scrim", components=nome)

    async def callback(self, inter: disnake.ModalInteraction) -> None:

        for custom_id, texto_digitado in inter.text_values.items():
