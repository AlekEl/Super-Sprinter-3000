from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)


@app.route('/')
def index():
    note_text = None
    if "note" in session:
        note_text = session["note"]
    return render_template("index.html", note=note_text)


@app.route("/story")
def test():
    note_text = None
    if "note" in session:
        note_text = session["note"]
    return render_template("story.html", note=note_text)


@app.route("/story", methods=["POST"])
def route_save():
    print("POST RECEIVED")
    session["note"] = request.form["note"]
    return redirect("/")


if __name__ == '__main__':
    app.secret_key = "1234567"
    app.run(
        debug=True,
        port=5000
    )
