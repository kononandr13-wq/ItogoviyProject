from flask import Flask,render_template,request,redirect,url_for,session
import database

app=Flask(__name__)
app.secret_key="384htoeirgn"

@app.route('/')
def index():
    return render_template('register.html')

@app.route('/city')
def city():
    return render_template('baza_graz.html')
@app.route('/rozusk')
def rozusk():
    return render_template('vudat_rozusk.html')
@app.route('/shtraf')
def shtraf():
    return render_template('vipisat_shtraf.html')
@app.route('/baza_oper')
def baza_oper():
    return render_template('baza_oper_y_fcb.html')


@app.route("/admin")
def admin_page():
    Dostyp=database.get_Dostyp()
    gos_persona=database.get_gos_persona()
    file=database.get_file()
    Citizens=database.get_Citizens()

    return render_template("admin.html",Dostyp=Dostyp,gos_persona=gos_persona,file=file,Citizens=Citizens)



@app.route("/register",methods=["POST","GET"])
def register():
    if request.method=="GET":
        return render_template("register.html")
    elif request.method=="POST":
        login=request.form["login"]
        pass1=request.form["pass1"]
        pass2=request.form["pass2"]
        errors=[]


        if database.is_user_exists(login):
            errors.append("Такой пользователь уже существует")


        if pass1 !=pass2:
            errors.append("Пароли не совпадают")

        if len(pass1)<4:
            errors.append("Пароль должен быть минимум 4 символа")

        if len(errors)==0:
            database.add_user(login,pass1)
            return render_template("success_register.html")
        else:
            return render_template("register.html",errors=errors )
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        login = request.form["login"]
        password = request.form["password"]

        auth_user = database.auth_user(login, password)
        if auth_user == None:
            return render_template(
                "login.html",
                errors=["Неверный пароль"]
            )
        else:
            print("Успешная авторизация")
            session["user_id"] = auth_user["user_id"]
            session["login"] = auth_user["user_login"]
            return redirect(url_for('index'))
if __name__ == '__main__':
    app.run(debug=True)