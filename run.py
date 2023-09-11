import asyncio
from hypercorn.asyncio import serve
from hypercorn.config import Config
from api import asgi_app as app

# ASGI RUN
if __name__ == "__main__":
    config = Config()
    config.bind = ["0.0.0.0:5000"]  # The IP and port to bind to
    config.loglevel = "info"  # Set the log level to info or debug
    asyncio.run(serve(app, config))

# WSGI RUN
# from api import app

# @app.shell_context_processor
# def make_shell_context():
#     return { "app": app }

# if __name__ == '__main__':
#     app.run(debug=True, host="0.0.0.0", port=5000)