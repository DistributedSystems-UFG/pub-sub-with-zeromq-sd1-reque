import zmq
import threading

context = zmq.Context()

# Individual messaging (RPC)
rpc_socket = context.socket(zmq.REQ)
rpc_socket.connect("tcp://localhost:5555")

# Topic-based messaging (Pub-Sub)
sub_socket = context.socket(zmq.SUB)
sub_socket.connect("tcp://localhost:5556")
sub_socket.setsockopt_string(zmq.SUBSCRIBE, "")

def individual_sender():
    while True:
        recipient = input("Enter recipient username: ")
        content = input("Enter message: ")
        message = {"recipient": recipient, "content": content}
        rpc_socket.send_json(message)
        response = rpc_socket.recv_string()
        print(response)

def topic_sender():
    while True:
        content = input("Enter message for topic: ")
        message = f"TOPIC {content}"
        sub_socket.send_string(message)

def topic_receiver():
    while True:
        message = sub_socket.recv_string()
        print(f"Topic message received: {message}")

individual_thread = threading.Thread(target=individual_sender)
topic_sender_thread = threading.Thread(target=topic_sender)
topic_receiver_thread = threading.Thread(target=topic_receiver)

individual_thread.start()
topic_sender_thread.start()
topic_receiver_thread.start()
