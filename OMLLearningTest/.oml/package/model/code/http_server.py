#####################
#### DO NOT EDIT ####
#####################
"""
Owner: isst
This file will start an HTTP server
Run following command
curl http://localhost:8888 --data <the post content>
"""
import os
import platform
import tornado.ioloop
import tornado.web
from model import ModelImp
model = ModelImp()


class MainHandler(tornado.web.RequestHandler):

    def is_binary_content(self):
        content_type = self.request.headers.get("Content-Type", "text/plain")
        return (content_type == "application/binary")

    def post(self):
        if (not self.request.body):
            self.set_status(500)
            self.write("empty request")
            self.finish()
            return
        try:
            if self.is_binary_content():
                response = model.EvalBinary(self.request.body)
                self.set_header("Content-Type", "application/binary")
                self.write(response)
            else:
                response = model.Eval(self.request.body.decode("utf-8"))
                self.set_header("Content-Type", "text/plain")
                self.write(response)
            self.finish()
            return
        except Exception as e:
            self.set_status(500)
            self.write("internal server error: %s" % e)
            self.finish()


def make_app():
    return tornado.web.Application([(r"/", MainHandler)])


if __name__ == "__main__":
    app = make_app()
    listeningPort = 8888
    if platform.system() == 'Windows':
        stringPort = os.getenv('_ListeningPort_')
        if (stringPort is None) or (stringPort == ''):
            print('_ListeningPort_ is required, not set.')
            exit()
        listeningPort = int(stringPort)

    app.listen(listeningPort)
    print("running \n")
    tornado.ioloop.IOLoop.current().start()
