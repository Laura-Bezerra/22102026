import json
import os
import secrets
import time
from datetime import datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).parent
UNLOCK_AT = datetime.fromisoformat(os.environ.get('UNLOCK_AT', '2026-10-22T19:30:00-03:00'))
MESSAGE = 'São quase 200 milhões de segundos dividindo a vida com você. Quase 200 milhões de segundos descobrindo, dia após dia, que a vida faz muito mais sentido ao seu lado. Que, na verdade, eu já nem sei se consigo imaginar uma vida sem você nela.\n\nSe lá atrás alguém me contasse que um dia eu sentiria tanto amor, que alguém seria capaz de despertar tanta coisa em mim, eu duvidaria até o último segundo. Eu não acreditaria que fosse possível amar alguém dessa forma, com tanta intensidade, tanta certeza e, ao mesmo tempo, com a sensação de que ainda existe um amor inteiro dentro de mim esperando para ser descoberto.\n\nMas hoje eu sei.\n\nE eu viveria mais cinquenta vezes se soubesse que, em cada uma dessas vidas, eu encontraria você. Mesmo que demorasse, mesmo que nossos caminhos fossem diferentes, mesmo que eu precisasse atravessar o mundo inteiro sem saber o que estava procurando. Se no final fosse você, eu iria.\n\nEu repetiria todas as decisões da minha vida, inclusive as erradas, enfrentaria todos os dias difíceis e percorreria cada caminho novamente, se tivesse a certeza de que todos eles, de alguma forma, me levariam até você.\n\nPorque, de todas as coisas que poderiam ter acontecido comigo, encontrar você foi a minha favorita.\n\nVocê torna tudo mais bonito (e, convenhamos, é só você ficar na minha frente pra eu achar isso, rs). Você me faz querer ser melhor, me faz enxergar beleza até nas coisas feias. E talvez você nem tenha ideia disso, mas o mundo é um lugar melhor porque você existe nele.\n\nE quando eu acho que nada mais vale a pena, quando o mundo parece pesado demais e eu esqueço as coisas boas que ele tem, você me lembra. Não porque seja sua responsabilidade fazer tudo ficar bem, mas porque existe algo extraordinário em saber que, mesmo nos dias mais difíceis, existe você. Com esse seu sorriso lindo, esse olhar brilhoso, esse jeitinho que é só seu e que eu reconheceria em qualquer lugar do mundo.\n\nEu amo quem você é. Amo quem eu sou quando estou com você. Amo as nossas conversas, as nossas besteiras, as nossas diferenças e até os momentos em que você me irrita.\n\nE amo, principalmente, saber que depois de tantos dias, tantas mudanças e tantas versões de nós mesmas, eu continuo olhando para você e pensando que é você. Que sempre foi você. E que, se a vida me permitir escolher, vai continuar sendo você.\n\nÀs vezes penso em como é curioso que, entre tantas pessoas, tantos lugares e tantas possibilidades, duas vidas tenham se encontrado e decidido caminhar juntas.\n\nSeis anos e quatro meses depois, eu ainda tenho vontade de te conhecer mais, de descobrir seus novos sonhos, de acompanhar todas as mulheres que você ainda vai se tornar e de amar cada uma delas.\n\nPorque eu não quero apenas o amor bonito dos dias fáceis. Quero a vida de verdade com você. Os dias comuns, as manhãs sonolentas, as risadas sem motivo, as conquistas, os planos que dão certo e aqueles que precisamos refazer. Quero ter histórias para contar e, quando a memória falhar, ter você ao meu lado para me lembrar de como foi.\n\nE se um dia me perguntarem o que eu faria diferente na minha vida, acho que minha resposta seria: teria procurado você um pouquinho antes.\n\nFeliz mais um dia 22, meu amor.\n\nDe todos os segundos que já vivi, os meus favoritos são aqueles em que a vida me deu você. E de todos os que ainda estão por vir, espero que a maioria seja ao seu lado.\n\nEu te amo. Muito mais do que esses quase 200 milhões de segundos seriam capazes de explicar.'
QUESTIONS = [{'text': 'Em que dia da semana começamos a namorar?', 'options': ['Sexta-feira', 'Domingo', 'Segunda-feira', 'Sábado'], 'answer': 'Segunda-feira'}, {'text': 'Onde tomamos o melhor mojito da nossa vida?', 'options': ['Paraty – RJ', 'Porto Seguro – BA', 'Ilhabela – SP', 'Florianópolis – SC'], 'answer': 'Porto Seguro – BA'}, {'text': 'Qual é a minha princesa favorita?', 'options': ['Rapunzel', 'Merida', 'Bela', 'Elsa'], 'answer': 'Bela'}, {'text': 'Por que o emoji que me representa é um robô?', 'options': ['Porque eu gosto muito de tecnologia', 'Porque meu celular era Android', 'Porque eu cursei Mecatrônica', 'Porque eu danço igual um robô'], 'answer': 'Porque meu celular era Android'}, {'text': 'Qual filme eu estava assistindo quando voltamos da viagem de Gramado?', 'options': ['Shrek', 'Bob Esponja', 'Procurando Nemo', 'A Era do Gelo'], 'answer': 'Bob Esponja'}, {'text': 'Qual música estava tocando quando eu olhei pra você e pensei: "Eu quero essa garota"?', 'options': ['Dona de Mim — IZA', 'Talismã — IZA', 'Meu Abrigo — Melim', 'Brisa — IZA'], 'answer': 'Talismã — IZA'}, {'text': 'Quando eu percebi que te amava de verdade?', 'options': ['Quando senti saudade de você pela primeira vez', 'Quando percebi que queria passar a vida ao seu lado', 'Quando você ficou doente e minha vontade foi cuidar de você, em vez de fugir', 'Quando tivemos nossa primeira conversa sobre o futuro juntas'], 'answer': 'Quando você ficou doente e minha vontade foi cuidar de você, em vez de fugir'}, {'text': 'O que eu sempre quis ganhar, mas nunca ganhei nem comprei?', 'options': ['Um telescópio', 'Um kit de mágica', 'Um banco imobiliário', 'Um videogame'], 'answer': 'Um kit de mágica'}, {'text': 'O que eu odeio que aconteça?', 'options': ['Quando alguém começa a gostar de algo só porque eu recomendei', 'Quando algo que eu gosto há muito tempo vira hype e todo mundo começa a gostar também', 'Quando alguém critica uma coisa de que eu gosto muito', 'Quando uma série tem muitas temporadas'], 'answer': 'Quando algo que eu gosto há muito tempo vira hype e todo mundo começa a gostar também'}, {'text': 'Qual alimento eu parei de comer quando era pequena porque disse que não gostava, mesmo gostando, e minha vó levou isso para a vida?', 'options': ['Queijo', 'Ovo', 'Banana', 'Tomate'], 'answer': 'Ovo'}]
SESSIONS = {}


class Handler(BaseHTTPRequestHandler):
    def reply(self, data, status=200):
        body = json.dumps(data, ensure_ascii=False).encode()
        self.send_response(status)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Cache-Control', 'no-store')
        self.end_headers()
        self.wfile.write(body)

    def unlocked(self):
        return time.time() >= UNLOCK_AT.timestamp()

    def do_GET(self):
        if self.path == '/api/status':
            return self.reply({'unlocked': self.unlocked(), 'unlockAt': UNLOCK_AT.isoformat(), 'serverTime': time.time() * 1000})
        if self.path != '/':
            return self.send_error(404)
        body = (ROOT / 'public/index.html').read_bytes()
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.send_header('Cache-Control', 'no-store')
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self):
        if self.path not in ('/api/start', '/api/answer', '/api/finish'):
            return self.send_error(404)
        if not self.unlocked():
            return self.reply({'error': 'Ainda não chegou a hora.'}, 403)
        if self.path == '/api/start':
            token = secrets.token_urlsafe(32)
            SESSIONS[token] = 0
            return self.reply({'token': token, 'question': self.question(0)})
        try:
            size = int(self.headers.get('Content-Length', '0'))
            if size > 4096:
                return self.reply({'error': 'Pedido muito grande.'}, 413)
            data = json.loads(self.rfile.read(size))
            token = data.get('token')
            index = SESSIONS.get(token)
            if self.path == '/api/finish':
                if index == len(QUESTIONS) and data.get('phase') == 1:
                    SESSIONS[token] = len(QUESTIONS) + 1
                    return self.reply({'nextPhase': 2})
                if index != len(QUESTIONS) + 1 or data.get('phase') != 2:
                    return self.reply({'error': 'Responda às perguntas primeiro.'}, 403)
                del SESSIONS[token]
                return self.reply({'message': MESSAGE})
            if index is None or index >= len(QUESTIONS):
                return self.reply({'error': 'Comece novamente.'}, 400)
            if data.get('answer') != QUESTIONS[index]['answer']:
                return self.reply({'correct': False, 'feedback': 'tenta de novo linda não é essa não'})
            index += 1
            SESSIONS[token] = index
            if index == len(QUESTIONS):
                return self.reply({'correct': True, 'game': True})
            return self.reply({'correct': True, 'question': self.question(index)})
        except (ValueError, TypeError, AttributeError):
            return self.reply({'error': 'Pedido inválido.'}, 400)

    def question(self, index):
        return {'number': index + 1, 'total': len(QUESTIONS), 'text': QUESTIONS[index]['text'], 'options': QUESTIONS[index]['options']}


if __name__ == '__main__':
    if UNLOCK_AT.tzinfo is None:
        raise ValueError('UNLOCK_AT precisa incluir o fuso horário.')
    port = int(os.environ.get('PORT', '3000'))
    print(f'Servidor na porta {port}. Liberação: {UNLOCK_AT.astimezone(ZoneInfo("America/Sao_Paulo"))}', flush=True)
    ThreadingHTTPServer(('0.0.0.0', port), Handler).serve_forever()
