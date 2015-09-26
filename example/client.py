#!/usr/bin/env python

import asyncio
import websockets


@asyncio.coroutine
def hello():
    websocket = yield from websockets.connect('ws://localhost:8765/')
    sending = input(">> ")
    yield from websocket.send(sending)
    receiving = yield from websocket.recv()
    print("<< {}".format(receiving))
    websocket.close()


def main(coroutine):
    asyncio.get_event_loop().run_until_complete(coroutine())


if __name__ == "__main__":
    main(hello)
