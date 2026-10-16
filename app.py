from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    profile = None

    if request.method == "POST":
        profile = {
            "name": request.form.get("name"),
            "bio": request.form.get("bio"),
            "image": request.form.get("image")
        }

    return render_template("index.html", profile=profile)

if __name__ == "__main__":
    app.run(debug=True)