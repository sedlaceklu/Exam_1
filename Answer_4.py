from flask import Flask, request
from psycopg2 import connect, OperationalError

app = Flask(__name__)

FORM = """
<form action="" method="POST">
    <input type="text" name="name" placeholder="Name">
    <input type="text" name="email" placeholder="Email">
    <input type="submit" value="Submit">
</form>
"""


def save_reader(cursor, name, email):
    sql = "INSERT INTO Readers(name, email) VALUES(%s, %s)"
    values = (name, email)
    cursor.execute(sql, values)


@app.route("/", methods=["GET", "POST"])
def readers():
    if request.method == "GET":
        return FORM

    name = request.form.get("name")
    email = request.form.get("email")

    if not name or not email or "@" not in email:
        return "Invalid data!"

    try:
        connection = connect(
            database="exam",
            user="postgres",
            password="coderslab",
            host="127.0.0.1"
        )
        cursor = connection.cursor()
        save_reader(cursor, name, email)
        connection.commit()
        connection.close()

        return "Reader added"

    except OperationalError as err:
        return str(err)


if __name__ == "__main__":
    app.run()
