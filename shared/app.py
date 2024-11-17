import sys
import os

# Add the root of your project to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Continue with your imports
# Continue with your imports
from flask import Flask
from flask_migrate import Migrate
from shared.utils.db_utils import db, migrate
from shared.models import user_model, post_model, comment_model
from shared.models.user_model import User  # Import the User model first
from shared.models.post_model import Post  # Import the Post model
from shared.models.comment_model import Comment 

# from flask import Flask
# from shared.utils.db_utils import db, migrate
# from shared.utils.db_utils import db
# from shared.models import comment_model



# Initialize the Flask App
app = Flask(__name__)

# Initialization configuration
# (later move this configuration to config/config.py)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:iop890890@localhost/vishu_model_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate.init_app(app, db)

from shared.models import user_model
from shared.models import post_model
from shared.models import comment_model