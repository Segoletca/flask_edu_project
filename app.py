from flask import Flask

from csrf_protection import csrf
from rest.index import index_app
from rest.examples import examples_app
from rest.clicker import clicker_app
from rest.products import products_app


def create_app():
    app = Flask(__name__)
    app.config.update(
        # python -c 'import secrets; print(secrets.token_hex())'
        SECRET_KEY='ebebb939c6beaa9ea23c1fb581a35b80318dd0328647b73b091a66dd652aa335',
    )
    csrf.init_app(app)
    app.register_blueprint(index_app)
    app.register_blueprint(examples_app, url_prefix="/examples", )
    app.register_blueprint(clicker_app, url_prefix="/clicker", )
    app.register_blueprint(products_app, url_prefix="/products")
    return app


def main():
    app = create_app()
    app.run(debug=True)


if __name__ == "__main__":
    main()
