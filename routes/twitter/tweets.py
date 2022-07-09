from flask import jsonify

# GET /twitter/tweets
# GET /twitter/tweets/<id>
# POST /twitter/tweets
# PUT /twitter/tweets/<id>
# DELETE /twitter/tweets/<id>

def register(app):
    
    @app.route('/twitter/tweets', methods=['GET'])
    def get_all_tweets():
        return jsonify([
            {"id": 1},
            {"id": 2}
        ])
