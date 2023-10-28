import websocket
import time

depth = 0
oxygen = 100
fuel = 100


def submarine(move):
    global depth
    global oxygen  # в %
    global fuel  # в %
    while oxygen & fuel:
        if move:
            depth = depth - move
        if depth != 0:
            oxygen = oxygen - 5
        else:
            oxygen = 100
        fuel = fuel - 1
        yield ({'depth': depth, 'oxygen': oxygen, 'fuel': fuel})
        time.sleep(2)


def on_open(ws):
    print("Connection opened")
    ws.send(submarine)


def on_message(ws, message):
    print(f"Recived message: {message}")


def on_close(ws):
    print("Connection closed")


ws = websocket.WebSocketApp("ws://127.0.0.1/ws/socket-server",
                            on_open=on_open,
                            on_message=on_message,
                            on_close=on_close)

ws.run_forever()
