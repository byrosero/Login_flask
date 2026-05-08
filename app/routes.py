from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from .models import db, User

api = Blueprint('api', __name__)

@api.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    email = data.get("email")

    if not username or not password or not email:
        return jsonify({"error": "Faltan campos"}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"error": "Usuario ya existe"}), 409

    hashed_pass = generate_password_hash(password)
    new_user = User(username=username, password=hashed_pass, email=email)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": f"Usuario {username} creado"}), 201


@api.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password, password):
        return jsonify({"error": "Credenciales inválidas"}), 401

    # Convertimos el ID a cadena
    token = create_access_token(identity=str(user.id))

    return jsonify({
        "message": "Inicio de sesión exitoso",
        "token": token
    }), 200


# Perfil protegido (requiere token)
@api.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)

    if not user:
        return jsonify({"message": "Usuario no encontrado"}), 404

    return jsonify({
        "message": "Perfil de usuario obtenido con éxito",
        "user": {
            "id": user.id,
            "username": user.username,
            "email": user.email
        }
    }), 200


# Listar usuarios
@api.route('/users', methods=['GET'])
@jwt_required()
def get_users():
    users = User.query.all()
    return jsonify([
        {"id": u.id, "username": u.username, "email": u.email}
        for u in users
    ])


# Editar usuario
@api.route('/users/<int:user_id>', methods=['PUT'])
@jwt_required()
def update_user(user_id):
    data = request.get_json()
    user = User.query.get(user_id)

    if not user:
        return jsonify({"message": "Usuario no encontrado"}), 404

    # Actualizar campos si se proporcionan
    if "username" in data:
        # Verificar si el nuevo username ya existe (y no es el del usuario actual)
        existing_user = User.query.filter_by(username=data["username"]).first()
        if existing_user and existing_user.id != user_id:
            return jsonify({"error": "Nombre de usuario ya en uso"}), 409
        user.username = data["username"]

    if "email" in data:
        existing_email = User.query.filter_by(email=data["email"]).first()
        if existing_email and existing_email.id != user_id:
            return jsonify({"error": "Email ya en uso"}), 409
        user.email = data["email"]

    if "password" in data:
        user.password = generate_password_hash(data["password"])

    db.session.commit()

    return jsonify({
        "message": f"Usuario {user_id} actualizado con éxito",
        "user": {"id": user.id, "username": user.username, "email": user.email}
    }), 200


# Eliminar usuario
@api.route('/users/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    user = User.query.get(user_id)

    if not user:
        return jsonify({"message": "Usuario no encontrado"}), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({"message": f"Usuario {user_id} eliminado con éxito"}), 200