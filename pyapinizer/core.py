# -*- coding: utf-8 -*-

import json

import dill


class Caller(object):
    def __init__(self, pkl):
        super(Caller, self).__init__()
        if hasattr(pkl, 'read') and callable(pkl.read):
            self.__callee = dill.load(pkl)
        else:
            self.__callee = dill.loads(pkl)

    def __call__(self, *args, **kwargs):
        return self.__callee(*args, **kwargs)


def GenerateHandler(pkl):
    class Handler(BaseHTTPRequestHandler):

        def eval(self, *args, **kwargs):
            ret = Caller(pkl)(*args, **kwargs)
            if isinstance(ret, bytes):
                return ret
            if isinstance(ret, str):
                return ret.encode('utf-8')
            return json.dumps(ret, ensure_ascii=False)

        def do_GET(self):
            p = self.path.split("?")
            path = p[0][1:].split("/")
            params = {}
            if len(p) > 1:
                params = parse_qs(p[1], True, True)
            print(params)
            body = self.eval(**params)

            self.send_response(200)
            self.send_header('Content-type', 'application/json; charset=utf-8')
            self.send_header('Content-length', len(body))
            self.end_headers()
            self.wfile.write(body)

    return Handler


if __name__ == '__main__':
    import http.server

    def testfunc(**kwargs):
        return dict({'abc': 123, 'ddd': True, 'n': None}, **kwargs)

    pkl = dill.dumps(testfunc)

    server_address = ("", 8000)
    handler_class = GenerateHandler(pkl)
    simple_server = http.server.HTTPServer(server_address, handler_class)
    simple_server.serve_forever()
