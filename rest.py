from flask import Flask, request, jsonify

app = Flask(__name__)

data = {
        1: "Hello World"
    }

users = {
        1: {
            "name": "Alex",
            "age": 25
        },
        
        2: {
            "name": "Max",
            "age": 28
        },

        3: {
            "name": "Egor",
            "age": 15
        }
    }

@app.route('/hello_world', methods=['GET'])
def say_hello():
    return jsonify(data)

@app.route('/users/', methods=['GET'])
def user_info():
    try:
        id = int(request.args.get("id"))
        return jsonify(users[id])
    except:
        return "sorry broski"

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    if not name or not email or not message:
        return "All fields are required", 400

    print(f"New contact request from {name} ({email}): {message}")

    return "Successful sended!"

if __name__ == "__main__":
    app.run(debug=True)