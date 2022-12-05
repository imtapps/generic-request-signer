#!/usr/bin/env python

from example.middleware import AuthMiddleware
from flask import Flask, Response

app = Flask(__name__)
app.config.from_object('example.settings')
app.wsgi_app = AuthMiddleware(app)


@app.route('/')
def index():
    return Response('hello world')


@app.route('/verify')
def verify():
    return Response('verified')


if __name__ == '__main__':
    app.run(threaded=True)
