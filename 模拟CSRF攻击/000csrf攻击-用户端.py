from flask import Flask, render_template,request,redirect,url_for

app=Flask(__name__,static_folder="static",template_folder="templates")

@app.route("/",methods=["POST","GET"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == "hrt" and password == "21009100253":
            response = redirect(url_for("transfer"))
            response.set_cookie("username","password")
            return response
        else:
            print("用户名或密码错误")
    return render_template("000正规途径的登录界面.html")

@app.route("/transfer",methods=["POST","GET"])
def transfer():
    username = request.cookies.get("username")
    if not username:
        return redirect(url_for("login"))
    if request.method == "POST":
        towho = request.form.get("towho")
        money = request.form.get("money")
        return "转账给%s 转账的金额%s 成功！"%(towho,money)
    return render_template("000正规途径的转账界面.html")

if __name__ == '__main__':
    app.run(debug=True)

