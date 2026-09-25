import os
from flask import Flask
from werkzeug.security import generate_password_hash
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from celery_config import init_celery
from cache import cache
from mail_config import mail

from config import Config
from models.models import db, User


def create_app():

    app = Flask(__name__)

    os.makedirs(os.path.join(app.root_path, "instance"), exist_ok=True)

    app.config.from_object(Config)

    CORS(app)

    db.init_app(app)
    cache.init_app(app)
    mail.init_app(app)
    JWTManager(app)

    from routes.auth import auth_bp
    from routes.admin import admin_bp
    from routes.recruiter import recruiter_bp
    from routes.student import student_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(recruiter_bp)
    app.register_blueprint(student_bp)

    init_celery(app)

    return app


app = create_app()



if __name__ == "__main__":

    with app.app_context():

        db.create_all()

        admin = User.query.filter_by(role="Admin").first()

        if not admin:

            admin = User(
                email="admin@placement.com",
                password=generate_password_hash("admin@PPA_V2"),
                role="Admin"
            )

            db.session.add(admin)
            db.session.commit()

            print("Admin just joined the portal!!")

    app.run(debug=True)