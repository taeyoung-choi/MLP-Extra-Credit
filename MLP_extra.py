from tornado.web import Application
from tornado.web import RequestHandler
from tornado.ioloop import IOLoop


class RankHandler(RequestHandler):
    def get(self):
        # take professor + course_number input
        # e.g.: 'COMS w4111 w4995 w4170'
        input = self.get_argument('user', 'none')
        print(input)
        self.write('Hello, {}'.format(input))
        # self.write(input)


if __name__ == "__main__":
    handler_mapping = [
        (r'/', RankHandler),
    ]
    application = Application(handler_mapping)
    application.listen(7777)
    IOLoop.current().start()
