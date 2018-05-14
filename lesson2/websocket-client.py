#! python2
# coding=utf-8  

import websocket
try:
    import thread
except ImportError:
    import _thread as thread
import time

def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

# def on_open(ws):
#     def run(*args):
#         for i in range(3):
#             time.sleep(1)
#             ws.send("Hello %d" % i)
#         time.sleep(1)
#         ws.close()
#         print("thread terminating...")
#     thread.start_new_thread(run, ())

def on_open(ws):
    def run(*args):
    	ws.send("trade")
        # for i in range(3):
        #     time.sleep(1)
        #     ws.send("Hello %d" % i)
        # time.sleep(1)
        # ws.close()
        print("thread terminating...")
    thread.start_new_thread(run, ())

if __name__ == "__main__":
    websocket.enableTrace(True)
    # ws = websocket.WebSocketApp("ws://echo.websocket.org/",
    #                           on_message = on_message,
    #                           on_error = on_error,
    #                           on_close = on_close)

    # k线图 https://www.btc123.com/market/kline
    ws = websocket.WebSocketApp("wss://api.btc123.com/websocket",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)

    ws.on_open = on_open
    ws.run_forever()