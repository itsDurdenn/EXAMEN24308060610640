from flask import Flask, render_template, session, request, redirect, url_for, flash
import requests

app = Flask(__name__)
app.secret_key = 'random_value'

@app.route('/')
def index():
    return render_template('Base.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        user = {
            'nombre': request.form.get('nombre'),
            'email': request.form.get('email'),
            'edad': request.form.get('edad'),
            'sexo': request.form.get('sexo'),
            'peso': request.form.get('peso'),
            'altura': request.form.get('altura'),
            'password': request.form.get('password')
        }
        session['user'] = user
        flash('Registro guardado correctamente.', 'success')
        return redirect(url_for('perfil'))
    return render_template('registro.html')

@app.route('/sesion')
def sesion():
    return render_template('sesion.html')

@app.route('/perfil')
def perfil():
    user = session.get('user')
    return render_template('perfil.html', user=user)

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    user = session.get('user')
    if user and user.get('email') == email and user.get('password') == password:
        flash('Inicio de sesión exitoso.', 'success')
        return redirect(url_for('index'))
    else:
        flash('Usuario o contraseña incorrectos.', 'error')
        return redirect(url_for('sesion'))

if __name__ == '__main__':
    app.run(debug=True)