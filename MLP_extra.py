from tornado.web import Application
from tornado.web import RequestHandler
from tornado.ioloop import IOLoop


class RankHandler(RequestHandler):
    def get(self):
        input = self.get_argument('user', 'none')
        self.write('Hello, {}'.format(input))


if __name__ == "__main__":
    handler_mapping = [
        (r'/', RankHandler),
    ]
    application = Application(handler_mapping)
    application.listen(7777)
    IOLoop.current().start()
