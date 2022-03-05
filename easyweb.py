# Stine Web Frame 1.0

import asyncio
from aiohttp import web


__all__ = ["path", "WebApplication", "run",
           "Request", "Response", "WebSocketResponse",
           "FileResponse", "StreamResponse",
           "Http404", "Http403"]


def path(method, url, view):
    return method, url, view


class WebApplication:
    urlpatterns = []

    @staticmethod
    @asyncio.coroutine
    def main(loop, address, port, run_class):
        _app = web.Application(loop=loop)

        for request_type, url, view in getattr(run_class, "urlpatterns"):
            _app.router.add_route(request_type, url, view)
        handler = _app.make_handler()
        server = yield from loop.create_server(handler,
                                               address, port)
        return server.sockets[0].getsockname()


def run(main_class, address, port):
    loop = asyncio.get_event_loop()
    host = loop.run_until_complete(main_class.main(loop, address, port, main_class))
    print("Serving on {}:{}. Hit Ctrl-C to stop.".format(host[0], host[1]))
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    print("Server shutting down.")


Request = web.Request
Response = web.Response
FileResponse = web.FileResponse
StreamResponse = web.StreamResponse
WebSocketResponse = web.WebSocketResponse
Http403 = web.HTTPForbidden
Http404 = web.HTTPNotFound


if __name__ == '__main__':
    def index(request: Request):
        global index_started
        print("index called")
        raise Http403


    class Test(WebApplication):
        urlpatterns = [
            path("GET", "/", index)
        ]


    run(Test, "127.0.0.1", 8000)
