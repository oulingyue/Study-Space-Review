from website import create_app
from flask import request, jsonify

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)