# Atividade de Programação - Pub-Sub com ZeroMQ - Sistema Distribuído

**Nome:** Ian Marcos da Cruz Chaves  
**Matrícula:** 201802684  

Este é um projeto de exemplo que demonstra a implementação de um sistema de mensagens utilizando o padrão Pub-Sub do ZeroMQ. Ele inclui um servidor e um cliente, permitindo a comunicação entre usuários individuais e o envio de mensagens para tópicos.

## Funcionamento

### Servidor (publisher.py)

O servidor é responsável por receber e encaminhar as mensagens de duas maneiras:

1. **Mensagens Individuais (RPC):** O servidor aguarda mensagens JSON que contêm informações sobre o destinatário e o conteúdo da mensagem. Ele responde encaminhando a mensagem de volta com a identificação do remetente.

2. **Mensagens de Tópico (Pub-Sub):** O servidor aceita mensagens no formato "TOPIC conteúdo". Ele envia o conteúdo da mensagem para todos os clientes inscritos no tópico.

### Cliente (subscriber.py)

O cliente é um programa interativo que permite que os usuários enviem mensagens individuais ou mensagens para um tópico. Ele possui três threads:

1. **Thread de Envio Individual:** Permite ao usuário enviar mensagens individuais para outros usuários. O usuário deve inserir o nome do destinatário e o conteúdo da mensagem.

2. **Thread de Envio de Tópico:** Permite ao usuário enviar mensagens para um tópico. O usuário deve inserir o conteúdo da mensagem.

3. **Thread de Recepção de Tópico:** Recebe mensagens enviadas para o tópico e exibe o conteúdo no console.

## Exemplo de Uso

1. Inicie o servidor executando o arquivo `subscriber.py`.

2. Inicie um ou mais clientes executando o arquivo `publisher.py`.

3. No cliente, use as opções disponíveis para enviar mensagens individuais ou para tópicos.

4. Observe como as mensagens individuais são roteadas para os destinatários corretos, e as mensagens de tópico são exibidas para os inscritos.

Certifique-se de substituir os endereços IP e portas no código pelos valores apropriados para a sua configuração.

## Requisitos

- Python 3.x
