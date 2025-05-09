from flask import Flask
from .endpoints.student_endpoints import student_bp
from .endpoints.teacher_endpoints import teacher_bp

def create_app():
    app = Flask(__name__)

    # Register blueprints for student and teacher endpoints
    app.register_blueprint(student_bp, url_prefix='/students')
    app.register_blueprint(teacher_bp, url_prefix='/teachers')

    return app
