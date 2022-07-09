from flask import jsonify

def register(app):
    
    @app.route('/twitter/profiles', methods=['POST'])
    def profiles():
        return jsonify({
            "prueba": "prueba"
        })