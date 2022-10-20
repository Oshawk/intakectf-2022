import datetime
import sqlite3
import traceback
from pathlib import Path

from flask import Flask, render_template, request

app = Flask(__name__)
connection = None
last_reset = None
quotes = [(quote.strip(),) for quote in (Path(__file__).parent / "quotes.txt").open().read().split("\n")]


def maybe_reset_db():
    global connection
    global last_reset

    if last_reset is None or (datetime.datetime.now() - last_reset).total_seconds() > 60:
        if connection is not None:
            connection.close()

        connection = sqlite3.connect(":memory:", check_same_thread=False)
        cursor = connection.cursor()

        cursor.execute("CREATE TABLE flag(flag STRING);")
        cursor.execute("INSERT INTO flag VALUES (?);", ("flag{a2c6f7a781d923c7}",))

        cursor.execute("CREATE table quote(quote STRING);")
        cursor.executemany("INSERT INTO quote VALUES (?);", quotes)

        cursor.close()


@app.route("/")
def home():
    maybe_reset_db()
    return render_template("home.html")


@app.route("/search")
def search():
    maybe_reset_db()
    query = request.args.get("query", "")

    cursor = connection.cursor()
    try:
        assert not any(blocked in query.lower() for blocked in ("-", "/", "*", ";", "\\", "union"))
        cursor.execute(f"SELECT quote FROM quote WHERE quote LIKE '%{query}%';")
        result = render_template("search.html", quotes=[i[0] for i in cursor.fetchall()])
    except Exception as e:
        error = "".join(traceback.format_exception(e))
        result = render_template("error.html", error=error)
    finally:
        cursor.close()

    return result


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=42008, debug=False)
