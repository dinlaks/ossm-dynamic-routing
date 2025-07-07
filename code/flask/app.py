from flask import Flask, render_template, request, Response
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/call-api")
def call_api():
    env = request.args.get("env", "dev")
    if env not in ["dev", "prod", "qa"]:
        return Response("Invalid environment", status=400, mimetype="text/plain")

    headers = {"x-env-target": env}

    try:
        response = requests.get("http://product-api.internal/hello", headers=headers)
        return Response(response.content, status=response.status_code, mimetype="text/plain")
    except requests.RequestException as e:
        return Response(str(e), status=500, mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
