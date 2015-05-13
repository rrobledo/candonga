'''Echo HTTP handler'''
import tornado.gen
import tornado.web


class EchoHandler(tornado.web.RequestHandler):  # pylint: disable=R0904
    '''Handle echo operations'''

    @tornado.gen.coroutine
    @tornado.web.asynchronous
    def post(self):
        '''POST method'''

        message = self.request.body.decode('utf-8')

        self.set_status(200)
        self.write(message)
        self.finish()
