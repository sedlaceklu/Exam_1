from flask import Flask, request
from psycopg2 import connect

DB_USER = "postgres"
DB_PASSWORD = "coderslab"
DB_HOST = "127.0.0.1"
DB_NAME = "exam"


app = Flask(__name__)


def get_connection():
    return connect(
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        dbname=DB_NAME
    )
@app.route("/", methods=["GET", "POST"])
def readers():
    if request.method == "GET":
        return """
        <form method="POST">
          <input type="text" name="name" placeholder="Name">
          <input type="text" name="email" placeholder="Email">
          <input type="submit">Send</button>
        </form>
        """

    name = request.form.get("name")
    email = request.form.get("email")

    if name == "" or email == "" or "@" not in email:
        return "Invalid data!"


    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO Readers (name, email) VALUES (%s, %s)",
        (name, email)
    )

    connection.commit()

    cursor.close()
    connection.close()

    return "Reader added"

if __name__ == "__main__":
    app.run(debug=True)

