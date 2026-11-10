
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory user storage
users = {
    1: {"id": 1, "name": "Supriya", "email": "supriya@example.com"},
    2: {"id": 2, "name": "Rahul", "email": "rahul@example.com"}
}

next_id = 3


# GET: Retrieve all users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(list(users.values())), 200


# GET: Retrieve one user
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = users.get(user_id)

    if user is None:
        return jsonify({"error": "User not found"}), 404

    return jsonify(user), 200


# POST: Add a new user
@app.route("/users", methods=["POST"])
def add_user():
    global next_id

    data = request.get_json(silent=True)

    if not data or not data.get("name") or not data.get("email"):
        return jsonify({"error": "Name and email are required"}), 400

    new_user = {
        "id": next_id,
        "name": data["name"],
        "email": data["email"]
    }

    users[next_id] = new_user
    next_id += 1

    return jsonify({
        "message": "User created successfully",
        "user": new_user
    }), 201


# PUT: Update an existing user
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    user = users.get(user_id)

    if user is None:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json(silent=True)

    if not data:
        return jsonify({"error": "JSON data is required"}), 400

    if "name" in data:
        user["name"] = data["name"]

    if "email" in data:
        user["email"] = data["email"]

    return jsonify({
        "message": "User updated successfully",
        "user": user
    }), 200


# DELETE: Remove a user
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    deleted_user = users.pop(user_id)

    return jsonify({
        "message": "User deleted successfully",
        "user": deleted_user
    }), 200


if __name__ == "__main__":
    app.run(debug=True)
