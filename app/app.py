import pyfiglet
from flask import Flask
from flasgger import Swagger
import logging, os

from config import get_version
from rest.ext_api_end_points import api_blueprint


def create_app():
    try:
        logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
        logging.getLogger('werkzeug').setLevel(logging.ERROR)

        web_app = Flask(__name__)
        web_app.register_blueprint(api_blueprint)

        swagger = Swagger(web_app, config=swagger_config)

        ascii_banner = pyfiglet.figlet_format("Tweesky")
        print(ascii_banner, flush=True)

        logging.info(f'Starting up.. [port:{get_port()}]')

        return web_app

    except Exception as e:
        logging.exception(e)


def get_port():
    """
    Retrieves port
    :return:
    """
    return int(os.environ.get("PORT", 5001))


swagger_config = {
    "headers": [],
    "openapi": "3.0.2",
    "components": {
        "securitySchemes": {
            "bearerAuth": {
                "type": "http",
                "scheme": "bearer"
            }
        },
    },
    "servers": [
        {
            "url": "http://localhost:5001", "description" : "dev"
        }
    ],
    "specs": [
        {
            "endpoint": "swagger",
            "route": "/openapi.json",
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "title": "OpenAPI Sample with Flasgger (Python)",
    "description": "Sample application showing OpenAPI configuration ",
    "version": get_version(),
    "termsOfService": "https://github.com/gcatanese/S3-Simple-Browser/blob/main/README.md",
    "static_url_path": "/characteristics/static",
    "swagger_ui": True,
    #"specs_route": "/apidocs",
}

if __name__ == '__main__':
    web_app = create_app()

    web_app.run(debug=False, port=get_port(), host='0.0.0.0')
