# Entre nós ♡

Site com liberação em **22/10/2026 às 19h, horário de Brasília**, seguida de um quiz de dez perguntas e duas fases de plataforma. Requer Python 3.9 ou superior, sem pacotes externos.

```sh
cd /workspace/22102026
python server.py
```

O servidor usa a porta 3000, configurável por `PORT`. Para mudar a data, use `UNLOCK_AT` com fuso explícito, por exemplo `UNLOCK_AT='2026-10-23T19:00:00-03:00' python server.py`.

Edite `MESSAGE` em `server.py` para trocar o texto final. As respostas e a mensagem ficam no servidor; o relógio do servidor controla a liberação. Depois do horário, o site continua disponível. Não há senha ou identificação: qualquer pessoa com acesso ao site pode responder ao quiz.

Para disponibilizar na internet, hospede o servidor Python em um serviço com suporte a processos persistentes. Esta implementação mantém o progresso em memória; reiniciar o processo reinicia os quizzes em andamento.

## Visualização estática

Ao abrir somente `public/index.html`, o site detecta a ausência da API e executa o quiz no navegador. Nesse modo, usa o relógio do dispositivo, e as respostas e a mensagem estão no HTML; não oferece bloqueio seguro. Para manter a verificação do horário no servidor, execute `python server.py` e acesse a aplicação por esse servidor. Ao alterar o texto ou horário, atualize também `localApi` e `localUnlockAt` no HTML para o modo estático.

Após as duas respostas certas, uma fase de plataforma aparece. Use ←/→ ou A/D para andar e espaço para pular; no celular, use os botões. Cair reinicia a fase, preservando o quiz. Alcançar a carta solicita a mensagem final. A fase é validada no navegador; não funciona como autenticação contra manipulação técnica.
