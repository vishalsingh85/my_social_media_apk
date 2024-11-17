import sys, os
sys.path.append(os.getcwd())
from flask import Flask
from comment_app.routes.comment_routes import comment_bp
from shared.utils.db_utils import db
from shared.models.user_model import User


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:iop890890@localhost/vishu_model_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)

app.register_blueprint(comment_bp)

if __name__ == '__main__':
    app.run(debug=True, port=5003)
    
    
    