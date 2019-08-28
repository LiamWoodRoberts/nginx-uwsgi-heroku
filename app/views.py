from app import app

@app.route("/")
def index():
    return "FLASK-NGINX-UWSGI_HEROKU"
