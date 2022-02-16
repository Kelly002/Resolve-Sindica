#########################################################
# Este bot foi desenvolvido para o atendimento de um
# sindico em  um condominio em Campinas.
# Desenvolvido por Kelly M. O. Lopes
# Campinas, 14 de janeiro de 2022
#########################################################


#########################################################
# Importando as bibliotecas necessaárias para a construção do bot
#########################################################
# Importando bilbliocas
import requests
import json
#import time


# Variaveis auxiliares
aux = []
aux2 = []




#########################################################
# Informações iniciais para a construção do bot
#########################################################
# Classe que instância o Bot com a API do Telegram
class TelegramBot:
    def __init__(self):
        token = '5074202239:AAHCwCgpd38-o3rOBCdQBmDXuvJePTTRckk'
        self.url_base = f'https://api.telegram.org/bot{token}/'

    def Iniciar(self):
        update_id = None
        while True:
            atualizacao = self.obter_novas_mensagens(update_id)
            dados = atualizacao["result"]
            if dados:
                for dado in dados:
                    update_id = dado['update_id']
                    mensagem = str(dado["message"]["text"])
                    chat_id = dado["message"]["from"]["id"]
                    eh_primeira_mensagem = int(dado["message"]["message_id"]) == 1
                    resposta = self.criar_resposta(mensagem, eh_primeira_mensagem)
                    self.responder(resposta, chat_id)
#########################################################
# Função que inicializa as apresentações dos botões com o comando "/ok"
#########################################################
# Função que pega as mensagens
    def obter_novas_mensagens(self, update_id):
        link_requisicao = f'{self.url_base}getUpdates?timeout=100'
        if update_id: link_requisicao = f'{link_requisicao}&offset={update_id + 1}'
        resultado = requests.get(link_requisicao)
        return json.loads(resultado.content)

    # Função que capta as perguntas que são inputadas pelo usuário


    def criar_resposta(self, mensagem, eh_primeira_mensagem):
        print('mensagem do cliente:' + str(mensagem))  # visualizar as respostas do usuário


#########################################################
# Construindo o fluxo de conversa do bot
#########################################################

        # Mensagem inicial do Bot
        if eh_primeira_mensagem == True or mensagem.lower() in ('Na','na','nathy','nathaly','Nathy','Nathaly', 'oi', 'olá', 'o', 'bom dia', 'boa tarde', 'boa noite'):
            return f'''Oi tudo  bem 😃 ?
                    Por favor,  para agilizar digite uma das opções:
                    1-Finaceiro 🤑
                    2-Reformas 🛠
                    3-Mudanças 🚚
                    4-Salão de Festas 🎂
                    '''

        # Condição que trata da primeira lista de opções oferecida pelo Bot
        if mensagem == '1':
            return f'''Boleto vencido até  30 dias?:
                    5-Sim 
                    6-Não 
                    Digite um dos valores.'''

        # Condição que trata do primeiro iten oferecido pelo lista de opções do Bot
        if mensagem == '5':
            return f''' Peça a segunda via pelo app.'''

        # Condição que trata do segundo iten oferecido pelo lista de opções do Bot
        if mensagem == '6':
            return f'''Favor entrar em contato com o jurídico.'''

        # Condição que trata do terceiro iten oferecido pelo lista de opções do Bot
        if mensagem == '2':
            return f'''Vai trocar o piso, azulejo, ou colocar geso?
                   7-Sim
                   8-Não'''
        # Condição que trata do primeiro iten oferecido pelo lista de opções do Bot
        if mensagem == '8':
            return f''' Entre no app e agende a data da reforma. Após reservar, basta dar um print na tela e enviar para mim'''
        # Condição que trata do primeiro iten oferecido pelo lista de opções do Bot
        if mensagem == '7':
            return f''' Entre em contato com o Engenheiro Miqueias, pois você irá precisar de um ART.'''

        # Condição que trata do terceiro iten oferecido pelo lista de opções do Bot
        if mensagem == '3':
            return f'''
            9-Entrada no condomínio\n
            10-Saída do condomínio'''

        # Condição que trata do terceiro iten oferecido pelo lista de opções do Bot
        if mensagem == '9':
            return f''' Já enviou o contrato para o adm?
              11- Sim
              12-Não'''

        # Condição que trata do terceiro iten oferecido pelo lista de opções do Bot
        if mensagem == '11':
            return f''' Basta esperar que eles entrem em contato. O prazo é de 72hs uteis.'''

        # Condição que trata do terceiro iten oferecido pelo lista de opções do Bot
        if mensagem == '12':
            return f''' Basta enviar um email para grasieli.gomes@brcondos.com'''

        # Condição que trata do terceiro iten oferecido pelo lista de opções do Bot
        if mensagem == '10':
            return f''' Basta reservar a data no app.'''

        # Condição que trata do terceiro iten oferecido pelo lista de opções do Bot
        if mensagem == '4':
                return f''' Quer agendar uma data para sua festa?
                        13-Sim
                        14- Mais informações sobre o salão'''

        # Condição que trata do terceiro iten oferecido pelo lista de opções do Bot
        if mensagem == '13':
            return f''' Entre no app e agende a data. '''

        # Condição que trata do terceiro iten oferecido pelo lista de opções do Bot
        if mensagem == '14':
            return f''' * Lotação máxima é de 60 pessoas.
                        * Temos 40 cadeiras e 10 mesas.
                        * Não pode colar nada nas paredes e nem fumar em qualquer área do condomínio.
                        * Me envie a reserva mais os dados completo dos seus convidados com o número do RG ou CPF.'''


    # Bot responde as perguntas do usuário
    def responder(self, resposta, chat_id):
        link_requisicao = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(link_requisicao)
        print('Bot:' + str(resposta)) # visualizar as respostas do Bot



# Inicializando o Bot
bot = TelegramBot()
bot.Iniciar()


