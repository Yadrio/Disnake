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



# Comando simples de texto
    @bot.command()
    async def nome_do_comando(ctx):
        pass


# Slash command
    @bot.slash_command(name='', description='')     
    async def scrim(self, inter: disnake.ApplicationCommandInteraction):

# Voce pode colocar só inter nos comandos se quiser, mas ele não exibirá os metodos dessa variavel
# Para colocar descrição nas opções do comando, importe isso:
    from disnake.ext.commands import Param

# Exemplo de como usa:
    @bot.slash_command(name='', description='')     
    async def scrim(self, inter: disnake.ApplicationCommandInteraction,
                    texto: str = Param(description='Insira a descrição da opções aqui')):





# Como fazer um cog, isso seria usar outro arquivo pra executar comandos dentro

    class Classe_principal_do_cog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='', description='')
    async def comando_nome(self, inter):
        pass

# Note, para declarar slash commands dentro de uma cog, se usa essa sintaxe @commands.slash_command e pra isso precisa importar isso 
    from disnake.ext import commands


# Essa função tem que ter na ultima linha de todo cog pra funcionar
    def setup(bot: commands.Bot):
        bot.add_cog(Classe_principal_do_cog(bot))











# Botão
# É assim que faz um botão, dentro de uma classe, esse exemplo possui 2 botões, todo botão precisa ter um custom_id, emoji é opcional, qualquer emoji que der pra colocar ali e exibir, da certo, seja do discord ou de fora. Quando for chamar um botão, sempre defina a variavel bot, que será recebida da classe My_bot() no main.pý
    class Exemplo_botão(disnake.ui.View):
        def __init__(self, bot):
            self.bot = bot
            super().__init__(timeout=None)

    @disnake.ui.button(style=ButtonStyle.green, custom_id='sim', emoji='✔️')
    async def sim(self, button: disnake.ui.Button, inter):
        pass

    @disnake.ui.button(style=ButtonStyle.green, custom_id='não', emoji='✔️')
    async def nao(self, button: disnake.ui.Button, inter):
        pass



# Select menu
# Menus selecionaveis, aquela caixa preto que contem opções, é assim que faz, só seguir o exemplo
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
        pass

# No callback você coloca o que quer que aconteça quando uma opção é escolhida, para exibir todos as opções use o comando self.values[0] vc tbm pode usar isso na descrição ou titulo da opção, pra aparecer pro usuario
# Voce pode filtrar cada opção selecioda usando o match case no python, em outras linguagens se chama switch case





# Modal
# O modal é quando aparece uma caixa de escrita no meio da tela, sobrepondo tudo que havia antes
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
# Para exibir ou tratar as respostas, esse esse for, ele exibe o custom id e o texto digito pelo usuario