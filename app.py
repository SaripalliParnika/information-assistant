from flask import Flask, render_template, request, jsonify
from assistant import process_command

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json.get("message", "")
    if user_input:
        response = process_command(user_input)
        return jsonify({"response": response})
    return jsonify({"response": "I didn't receive anything."})

if __name__ == "__main__":
    app.run(debug=True)
