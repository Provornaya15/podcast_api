from flask import Flask, render_template, request
app = Flask("MyApp")

@app.route("/")
def main():
     return render_template("index.html")

@app.route("/signup", methods=["POST"])
def sign_up():
    form_data = request.form
    print form_data["email"]
    return render_template("index2.html")

@app.route("/<name>")
def hello_someone(name):
    return render_template("index.html",name=name.title())

@app.route("/start")
def start_searching():
    return render_template("index3.html")




app.run(debug=True)
