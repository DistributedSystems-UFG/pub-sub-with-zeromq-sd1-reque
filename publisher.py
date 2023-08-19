import zmq
import threading

contexto = zmq.Context()

# Mensagens individuais (RPC)
socket_rpc = contexto.socket(zmq.REQ)
socket_rpc.connect("tcp://localhost:5555")

# Mensagens baseadas em tópicos (Pub-Sub)
socket_sub = contexto.socket(zmq.SUB)
socket_sub.connect("tcp://localhost:5556")
socket_sub.setsockopt_string(zmq.SUBSCRIBE, "")

def enviar_individual():
    while True:
        destinatario = input("Digite o nome do destinatário: ")
        conteudo = input("Digite a mensagem: ")
        mensagem = {"destinatario": destinatario, "conteudo": conteudo}
        socket_rpc.send_json(mensagem)
        resposta = socket_rpc.recv_string()
        print(resposta)

def enviar_topico():
    while True:
        conteudo = input("Digite a mensagem para o tópico: ")
        mensagem = f"TÓPICO {conteudo}"
        socket_sub.send_string(mensagem)

def receber_topico():
    while True:
        mensagem = socket_sub.recv_string()
        print(f"Mensagem do tópico recebida: {mensagem}")

thread_individual = threading.Thread(target=enviar_individual)
thread_enviar_topico = threading.Thread(target=enviar_topico)
thread_receber_topico = threading.Thread(target=receber_topico)

thread_individual.start()
thread_enviar_topico.start()
thread_receber_topico.start()
