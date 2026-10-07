from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
app = Flask(__name__, static_folder="static", static_url_path="/static")



app.secret_key = "online-examination-system-secret-key"



def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="naughtyqueen",
        database="online_examination_system"
    )



@app.route("/")
def home():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():

    student_id = request.form["student_id"]
    password = request.form["password"]

    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    query = """
        SELECT * FROM students
        WHERE student_id = %s AND password = %s
    """

    cursor.execute(query, (student_id, password))

    student = cursor.fetchone()

    cursor.close()
    db.close()

    if student:
        session["student_id"] = student["student_id"]
        return redirect(url_for("dashboard"))

    return render_template(
        "login.html",
        error="Invalid Student ID or Password"
    )



@app.route("/dashboard")
def dashboard():

    if "student_id" not in session:
        return redirect(url_for("home"))

    student_id = session["student_id"]

    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    query = """
        SELECT *
        FROM students
        WHERE student_id = %s
    """

    cursor.execute(query, (student_id,))

    student = cursor.fetchone()

    cursor.close()
    db.close()

    return render_template(
        "dashboard.html",
        student=student
    )


@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("home"))



if __name__ == "__main__":
    app.run(debug=True)