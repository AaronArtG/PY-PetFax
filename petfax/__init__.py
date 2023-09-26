from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return 'Hello, PetFax!'
    
    # Register pet blueprint
    from . import pet  # Adjust the import path to match your directory structure
    app.register_blueprint(pet.bp)

    # Register fact blueprint
    from . import fact
    app.register_blueprint(fact.bp)

    return app
