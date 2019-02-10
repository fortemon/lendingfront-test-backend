import os

import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def get(self):
        self.write("<p>Server started</p>")

class LoanHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with, content-type")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def post(self):
        data = tornado.escape.json_decode(self.request.body);

        try:
            requested_amount = float(data['requested_amount'])
        except ValueError:
            self.set_status(400)
            self.finish({'message': '`requested_amount` not valid.'})
            return

        if requested_amount < 50000:
            self.write({'message': 'Approved'})
        elif requested_amount > 50000:
            self.write({'message': 'Declined'})
        else:
            self.write({'message': 'Undecided'})

    def options(self):
        return

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/loan", LoanHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    port = int(os.environ.get("PORT", 8888))
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()
