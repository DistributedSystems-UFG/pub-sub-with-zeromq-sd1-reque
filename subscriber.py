import zmq
import threading

contexto = zmq.Context()

# Mensagens individuais (RPC)
socket_rpc = contexto.socket(zmq.REP)
socket_rpc.bind("tcp://*:5555")

# Mensagens baseadas em tópicos (Pub-Sub)
socket_pub = contexto.socket(zmq.PUB)
socket_pub.bind("tcp://*:5556")

def tratar_rpc():
    while True:
        mensagem = socket_rpc.recv_json()
        destinatario = mensagem["destinatario"]
        conteudo = mensagem["conteudo"]
        resposta = f"Mensagem de {destinatario}: {conteudo}"
        socket_rpc.send_string(resposta)

def tratar_pub():
    while True:
        mensagem = socket_pub.recv_string()
        topico, conteudo = mensagem.split(" ", 1)
        socket_pub.send_string(conteudo)

thread_rpc = threading.Thread(target=tratar_rpc)
thread_rpc.start()

thread_pub = threading.Thread(target=tratar_pub)
thread_pub.start()
