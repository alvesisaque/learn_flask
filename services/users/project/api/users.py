from flask import Blueprint, jsonify

users_blueprint = Blueprint('users', __name__)

# created a new instance of the Blueprint
@users_blueprint.route('/users/ping', methods=['GET'])
def ping_pong():
	return jsonify({
		'status': 'success',
		'message': 'pong!'
	})