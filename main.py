from flask import Flask,render_template,request,redirect,url_for,session
import database

app=Flask(__name__)
app.secret_key="384htoeirgn"




@app.route("/register",methods=["POST","GET"])
def register():
    if request.method=="GET":
        return render_template("register.html")
    elif request.method=="POST":
        login=request.form["login"]
        pass1=request.form["pass1"]
        pass2=request.form["pass2"]
        errors=[]

        #Проверка существования пользователя
        if database.is_user_exists(login):
            errors.append("Такой пользователь уже существует")

        #Проверка на одинаковость паролей
        if pass1 !=pass2:
            errors.append("Пароли не совпадают")

        #Проверка качества пароля
        if len(pass1)<4:
            errors.append("Пароль должен быть минимум 4 символа")

        #Если нет ошибок - регистрация
        if len(errors)==0:
            database.add_user(login,pass1)
            return render_template("success_register.html")
        else:
            return render_template("register.html",errors=errors )