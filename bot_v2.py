#########################################################
# Este bot foi desenvolvido para o atendimento de um
# sindico em  um condominio em Campinas.
# Desenvolvido por Kelly M. O. Lopes
# Campinas, 14 de janeiro de 2022
#########################################################


#########################################################
# Importando as bibliotecas necessaárias para a construção do bot
#########################################################
# !pip install pytelegrambotapi   instala a biblioteca do Telegram via terminal
import telebot
import ast

from telebot import types

#########################################################
# Informações iniciais para a construção do bot
#########################################################
# import InlineKeyboardButton, InlineKeyboardMarkup, Update
# from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

CHAVE_API = '5074202239:AAHCwCgpd38-o3rOBCdQBmDXuvJePTTRckk'
bot = telebot.TeleBot(CHAVE_API)

# Traz as informações pessoais do usuário que está interagindo com o bot  #id=5060316690
print(bot.get_me())

#########################################################
# Criação dos botões do Bot
#########################################################
# Função que trata das chaves e dos valores que vão para os botões do bot
def makeKeyboard(perguntas_1):
    markup = types.InlineKeyboardMarkup()
    # print("Passou - " + perguntas_1)

    for key, value in stringList.items():
        if value != "":
            markup.add(
                types.InlineKeyboardButton(text=value, callback_data="['value', '" + value + "', '" + key + "']"))
    return markup


# Função que inicializa as apresentações dos botões com o comando "/ok"
@bot.message_handler(commands=['aqui'])
def handle_command_adminwindow(message):
    msg = message.text


#########################################################
# Construindo o fluxo de conversa do bot
#########################################################

# Função que trata da primeira Opção apresentada no menu do bot
@bot.message_handler(commands=["financiamento"])
def financiamento(mensagem):
    texto = """
    Boleto vencido acima de 30 dias, favor entrar em contato com o jurídico no telefone: +55 19 98388-4942
    """
    bot.send_message(mensagem.chat.id, texto)


# Função que trata do primeiro item que está dentro da primeira Opção apresentada pelo bot
@bot.message_handler(commands=["reformas"])
def reformas(mensagem):
    texto = """
    Se a sua reforma irá ter: Gesso, Troca de Azuleijo, Troca de Piso ou Blindx, favor chamar o Teia.
    """
    bot.send_message(mensagem.chat.id, texto)


# Função que trata do segundo item que está dentro da primeira Opção apresentada pelo bot
@bot.message_handler(commands=["adm"])
def adm(mensagem):
    texto = """
    Entre em contato com a BrCondos no telefone: +55 19 3234-3420.
    """
    bot.send_message(mensagem.chat.id, texto)


# Função que trata do terceiro item que está dentro da primeira Opção apresentada pelo bot
@bot.message_handler(commands=["mudancas"])
def mudancas(mensagem):
    texto = """
    Grite pela Nathaly 😂.
    """
    bot.send_message(mensagem.chat.id, texto)

    bot.send_message(mensagem.chat.id, "Espero ter ajudado 😉")


#########################################################
# Verifica se existem novas mensagens no bot
#########################################################
def verificar(mensagem):
    return True

#########################################################
# Mensagem de saudação
#########################################################
@bot.message_handler(func=verificar)
def responder(mensagem):
    #firstName = bot.messagem.from_user.first_name
    texto = """Oi,+  firstName + 😃 tudo bem?\n
       Qual é a sua dúvida 🤔🤔 ? \n
       /financiamento Financiamento
       /reformas reformas
       /adm Administrativo
       /mudancas Mudanças
       Escolha uma das opções acima!!!
        """
    bot.send_message(mensagem.chat.id, text=texto)


bot.polling()



