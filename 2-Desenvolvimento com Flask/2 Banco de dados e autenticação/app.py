from flask import Flask, request, jsonify
from database import db
from models.user import User
from flask_login import LoginManager, login_user, current_user,logout_user, login_required

app = Flask(__name__)
app.config["SECRET_KEY"] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

login_manager = LoginManager()
db.init_app(app)
login_manager.init_app(app)

login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username and password:

        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            print(current_user.is_authenticated)
            return jsonify({'message':'Usuário Logado!'})

    return jsonify({'message':'Credenciais Inválidas!'}), 400

@app.route("/logout", methods=["GET"])
@login_required
def logout():
    logout_user()
    return jsonify({'message':'Usuário Deslogado!'})

@app.route("/user", methods=["POST"])
def create_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username and password:
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return jsonify({'message':'Usuário Cadastrado!'})
    
    return jsonify({'message':'Credenciais inválidas!'})

@app.route("/user/<int:user_id>", methods=['GET'])
@login_required
def read_user(user_id):
    user = User.query.get(user_id)

    if user:
        return {"username": user.username}
    
    return jsonify({'message':'Usuário não encontrado'}), 404

@app.route("/user/<int:user_id>", methods=['PUT'])
@login_required
def update_user(user_id):
    data = request.get_json()
    user =  User.query.get(user_id)
    password = data.get("password")

    if user and password:
        user.password = password
        db.session.commit()
        return jsonify({"message":"senha atualizada com sucesso"})
    
    return jsonify({'message':'Usuário não encontrado'}), 404

@app.route("/user/<int:user_id>", methods=['DELETE'])
@login_required
def delete_user(user_id):
    user =  User.query.get(user_id)

    if user_id == current_user.id:
        return jsonify({"message":"Deleção não permitida!"}), 403

    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": f"Usuário {user_id} atualizada com sucesso"})
    
    return jsonify({'message':'Usuário não encontrado'}), 404

if __name__ == '__main__': 
    app.run(debug=True)