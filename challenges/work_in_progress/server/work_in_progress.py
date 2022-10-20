import pickle

from flask import Flask, make_response, redirect, render_template, request

KEY = b"repeating_xor_key"

app = Flask(__name__)
users = {}


class User:
    def __init__(self, username):
        self.username = username


def clear_cookie(text):
    response = make_response(text)
    response.set_cookie("user", "", expires=0)
    return response


def set_cookie(text, value):
    response = make_response(text)
    response.set_cookie("user", value)
    return response


def xor(data, key):
    result = bytearray()
    for i in range(len(data)):
        result.append(data[i] ^ key[i % len(key)])

    return bytes(result)


def get_cookie(user_):
    return xor(pickle.dumps(user_), KEY).hex()


def get_user(cookie):
    return pickle.loads(xor(bytes.fromhex(cookie), KEY))


@app.route("/", methods=["GET"])
def home_get():
    return clear_cookie(render_template("home.html"))


@app.route("/", methods=["POST"])
def home_post():
    username = request.form.get("username", "")
    password = request.form.get("password", "")
    submit = request.form.get("submit", "")

    if (
        username == "" or
        password == "" or
        submit not in ("login", "register")
    ):
        return clear_cookie(render_template("home.html", message="All fields must be filled."))

    if submit == "login":
        if users.get(username, "") == password:
            user_ = User(username)
            return set_cookie(redirect("/user"), get_cookie(user_))
        else:
            return clear_cookie(render_template("home.html", message="Invalid username or password."))
    else:
        if username in users:
            return clear_cookie(render_template("home.html", message="Username already exists."))
        else:
            users[username] = password
            user_ = User(username)
            return set_cookie(redirect("/user"), get_cookie(user_))


@app.route("/user", methods=["GET"])
def user():
    try:
        user_ = get_user(request.cookies.get("user", ""))
    except Exception:
        return clear_cookie(redirect("/"))

    return render_template("user.html", username=user_.username)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=42005, debug=False)
