import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#import sys


# instantiate the app
app = Flask(__name__)

# to view the log
#print(app.config, file=sys.stderr)

# set config
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

# instantiate the db
db = SQLAlchemy(app)

def create_app(script_info=None):

	# instantiate the app
	app = Flask(__name__)

	# set config
	app_settings = os.getenv('APP_SETTINGS')
	app.config.from_object(app_settings)

	# set up extensions
	db.init_app(app)

	# register blueprints
	from project.api.users import users_blueprint
	app.register_blueprint(users_blueprint)

	# This is used to register the app and db to the
	# shell. Now we can work with the application context and the database without having to import them
	# directly into the shell.
	# shell context for flask cli
	@app.shell_context_processor
	def ctx():
		return {'app': app, 'db': db}
	return app