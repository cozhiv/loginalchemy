import os
from flask import Flask


def create_app(test_config=None):
    #create and configure
    app = Flask(__name__, instance_relative_config = True)
    #api = Api(app)
    app.config.from_mapping(
        SECRET_KEY = "dev",
        #DATABASE= os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    
    #print(test_config)
    if test_config is None:
        #load instance config, if it exists, when not in test mode
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    #check if the instance file exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    

    # just hello world!
    @app.route('/hello')
    def hello():
        return "Hello Boza!"

    from . import db
    @app.teardown_request
    def teardown_request(response_or_exc):
        db.db_session.remove()
    db.init_db()


    #from . import db
    #db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import rest
    app.register_blueprint(rest.bp)
    #from . import blog
    #app.register_blueprint(blog.bp)
    #app.add_url_rule('/','index')

    return app