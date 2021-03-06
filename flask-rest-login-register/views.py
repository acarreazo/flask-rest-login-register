from models import Base, User
from flask import Flask, jsonify, request, url_for, abort, g
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

from flask.ext.httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()


engine = create_engine('sqlite:///users.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
app = Flask(__name__)


@auth.verify_password
def verify_password(username_or_token, password):

    user_id = User.verify_auth_token(username_or_token)
    if user_id:
        user = session.query(User).filter_by(id = user_id).one()
    else:
        user = session.query(User).filter_by(username = username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True


@app.route('/rest/login',methods = ['POST'])
def get_login():
    username = request.json.get('username')
    password = request.json.get('password')

    user = session.query(User).filter_by(username=username).first()
    g.user = user
    if not user or not user.verify_password(password):
        return False

    token = user.generate_auth_token()
    return jsonify({'token': token.decode('ascii')})


@app.route('/rest/user', methods = ['POST'])
def crear_usuario():
    username = request.json.get('username')
    password = request.json.get('password')
    nombres = request.json.get('nombres')
    hobbie = request.json.get('hobbie')
    if username is None or password is None:
        print "Faltan parametros"
        abort(400) 
        
    if session.query(User).filter_by(username = username).first() is not None:
        print "El usuario ya existe"
        user = session.query(User).filter_by(username=username).first()
        return jsonify({'message':'El usuario ya existe'}), 200#, {'Location': url_for('get_user', id = user.id, _external = True)}
        
    user = User(username = username,nombres = nombres, hobbie = hobbie)
    user.hash_password(password)
    session.add(user)
    session.commit()
    return jsonify({ 'resultado': 'ok' }), 201#, {'Location': url_for('get_user', id = user.id, _external = True)}


@app.route('/rest/user')
@auth.login_required
def obtener_usuario():
    return jsonify({ 'hobbie': '%s!' % g.user.hobbie })



if __name__ == '__main__':
    app.debug = True
    #app.config['SECRET_KEY'] = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))
    app.run(host='0.0.0.0', port=5000)
