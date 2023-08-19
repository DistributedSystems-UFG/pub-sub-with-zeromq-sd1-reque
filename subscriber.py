import zmq
import threading

context = zmq.Context()

# Individual messaging (RPC)
rpc_socket = context.socket(zmq.REP)
rpc_socket.bind("tcp://*:5555")

# Topic-based messaging (Pub-Sub)
pub_socket = context.socket(zmq.PUB)
pub_socket.bind("tcp://*:5556")

def handle_rpc():
    while True:
        message = rpc_socket.recv_json()
        recipient = message["recipient"]
        content = message["content"]
        response = f"Message from {recipient}: {content}"
        rpc_socket.send_string(response)

def handle_pub():
    while True:
        message = pub_socket.recv_string()
        topic, content = message.split(" ", 1)
        pub_socket.send_string(content)

rpc_thread = threading.Thread(target=handle_rpc)
rpc_thread.start()

pub_thread = threading.Thread(target=handle_pub)
pub_thread.start()
