from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("000暗藏csrf攻击的网页.html")

if __name__ == '__main__':
    app.run(port=8888,debug=True)