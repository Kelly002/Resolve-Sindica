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
import requests
from telebot import types

#from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                         # RegexHandler, ConversationHandler, CallbackQueryHandler)
#from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup





#########################################################
# Informações iniciais para a construção do bot
#########################################################
CHAVE_API = '5074202239:AAHCwCgpd38-o3rOBCdQBmDXuvJePTTRckk'
bot = telebot.TeleBot(CHAVE_API)

# Traz as informações pessoais do usuário que está interagindo com o bot  #id=5060316690
#print(bot.get_me())

#########################################################
# Função que inicializa as apresentações dos botões com o comando "/ok"
#########################################################
def main():
    @bot.message_handler(commands=['aqui'])
    def handle_command_adminwindow(message):
        msg = message.text


#########################################################
# Construindo o fluxo de conversa do bot
#########################################################

# Função que trata da primeira Opção apresentada no menu do bot
    @bot.message_handler(commands=["financeiro"])
    def financeiro(mensagem):
        texto = """
        Boleto vencido acima de 30 dias, favor entrar em contato com o jurídico no telefone: +55 19 98388-4942
        """
        bot.send_message(mensagem.chat.id, texto)


# Função que trata do segundo na primeira Opção apresentada pelo bot
    @bot.message_handler(commands=["reformas"])
    def reformas(mensagem):
        texto = """
        Se a sua reforma precisa de Art, favor entrar em contato com o Engenheiro Miquéias, no telefone: +55 19 98840-7845.\n
        Agora, se for algo mais simples, basta agendar o horário no app BRCondos, e enviar o print do serviço e dos dados para mim.
        """
        bot.send_message(mensagem.chat.id, texto)


# Função que trata do terceiro item que está Opção apresentada pelo bot
    @bot.message_handler(commands=["adm"])
    def adm(mensagem):
        texto = """
        Favor entrar em contato com a BrCondos no telefone: +55 19 3234-3420.
        """
        bot.send_message(mensagem.chat.id, texto)


# Função que trata do quarto item que está dentro da primeira Opção apresentada pelo bot
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
        texto = """Olá, condômino 😃 tudo bem?
        Qual é a sua dúvida 🤔🤔 ? \n
        /financeiro Financeiro
        /reformas Reformas
        /adm Administrativo
        /mudancas Mudanças
        Clique em uma das opções acima!!!
        """
        bot.send_message(mensagem.chat.id, text=texto)


    bot.polling()

if __name__ == "__main__":
    main()


