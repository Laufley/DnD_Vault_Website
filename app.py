from flask import Flask, render_template
# from controllers.player_history_controller import players_history_blueprint
from controllers.campaign_controller import campaigns_blueprint
from controllers.player_controller import players_blueprint
from controllers.controller import public_blueprint

app = Flask(__name__)

# app.register_blueprint(players_history_blueprint)
app.register_blueprint(campaigns_blueprint)
app.register_blueprint(players_blueprint)
app.register_blueprint(public_blueprint)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
