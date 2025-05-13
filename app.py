from flask import Flask, send_from_directory, jsonify

app = Flask(__name__)

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('src/static', filename, mimetype='text/css')

@app.route('/activities')
def get_activities():
    # Exemplo de dados de atividades
    activities = {
        "Soccer": {
            "description": "Join the soccer team and compete in tournaments.",
            "schedule": "Mondays and Wednesdays, 4-6 PM",
            "max_participants": 20,
            "participants": ["Alice", "Bob"]
        },
        "Chess Club": {
            "description": "Learn and play chess with others.",
            "schedule": "Fridays, 3-5 PM",
            "max_participants": 15,
            "participants": ["Charlie"]
        }
    }
    return jsonify(activities)

if __name__ == '__main__':
    app.run(debug=True)