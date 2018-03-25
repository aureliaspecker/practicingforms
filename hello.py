
from flask import Flask, render_template, request

app = Flask("MyApp")

@app.route("/")
def hello():
    return "Welcome to my website"

@app.route("/aurelia")
def aurelia():
    return "Hello Aurelia, nice to meet you!"

@app.route("/<name>") #this says "whatever anybody enters in the URL, it will take that entry and store it as a variable called name and then pass that variable into the hello function and render the HTML template"
def hello_someone(name):
    return render_template("hello.html", name=name.title())

@app.route("/signup")
def signup():
    return render_template("signup.html")
@app.route("/signup_submit", methods=["POST"])
def sign_up_submit():
    form_data = request.form
    print form_data["email"]
    print form_data["phone"]
    return "All OK"

@app.route("/aboutyou")
def aboutyou():
    return render_template("aboutyou.html")
@app.route("/aboutyou_submit", methods=["POST"])
def about_you():
    form_data = request.form
    print form_data["yourname"]
    print form_data["birthdate"]
    print form_data["tellmemore"]
    return "All OK"

app.run(debug=True)
