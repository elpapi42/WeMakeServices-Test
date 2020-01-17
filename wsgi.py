# This Python file uses the following encoding: utf-8

"""Instance and run the application server."""

from application.app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='127.0.0.1')
