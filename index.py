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

class BusinessDataHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def post(self):
        try:
            requested_amount = float(self.get_argument('requested_amount', ''))
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

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/businessdata", BusinessDataHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    port = int(os.environ.get("PORT", 8888))
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()
