'''Web server's run script'''
import argparse
import tornado.ioloop
import tornado.web

import backend.service.applications as applications


def main():
    '''Web server main function'''

    parser = argparse.ArgumentParser(description='Echo web service')
    parser.add_argument(
        '-p', '--port', type=int, required=True, dest="port",
        help='Service port')
    args = parser.parse_args()

    applications.BACKEND.listen(args.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()
