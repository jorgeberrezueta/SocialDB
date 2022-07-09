from flask import jsonify

def register(app):
    
    @app.route('/auth/login', methods=['POST'])
    def login():
        return jsonify({
            "prueba": "prueba"
        })