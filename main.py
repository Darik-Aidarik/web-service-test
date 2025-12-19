from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
    name = request.args.get("name")
    message = request.args.get("message")

    if not name or not message:
        return "Необходимых параметром нет. Это печально :(", 400

    return f"Hello {name}! {message}!"

if __name__ == '__main__':
    app.run(debug=True)