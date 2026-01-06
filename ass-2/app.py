from flask import Flask, request, jsonify

app = Flask(__name__)

users = []
auto_id = 1


# Register user
@app.route('/register', methods=['POST'])
def register():
    global auto_id
    data = request.get_json()

    # validation
    if not data:
        return jsonify({"error": "JSON data required"}), 400

    if not all(k in data for k in ("name", "email", "password")):
        return jsonify({"error": "name, email, password are required"}), 400

    # check if email already exists
    for user in users:
        if user["email"] == data["email"]:
            return jsonify({"error": "Email already registered"}), 409

    user = {
        "id": auto_id,
        "name": data["name"],
        "email": data["email"],
        "password": data["password"]  # plain for now
    }

    users.append(user)
    auto_id += 1

    return jsonify({
        "message": "User registered successfully",
        "user_id": user["id"]
    }), 201


# Login user
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON data required"}), 400

    if not all(k in data for k in ("email", "password")):
        return jsonify({"error": "email and password required"}), 400

    for user in users:
        if user["email"] == data["email"] and user["password"] == data["password"]:
            return jsonify({
                "message": "Login successful",
                "user": {
                    "id": user["id"],
                    "name": user["name"],
                    "email": user["email"]
                }
            }), 200

    return jsonify({"error": "Invalid email or password"}), 401


# Get all users (optional, admin type)
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200


if __name__ == '__main__':
    app.run(debug=True)

