# from flask import Flask, render_template, request, redirect, url_for, flash, session
# from flask_sqlalchemy import SQLAlchemy
# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField, FloatField
# from wtforms.validators import DataRequired, Length
# from werkzeug.security import generate_password_hash, check_password_hash

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///services.db'
# app.config['SECRET_KEY'] = 'your_secret_key'
# db = SQLAlchemy(app)

# # Models
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(50), unique=True, nullable=False)
#     password_hash = db.Column(db.String(128), nullable=False)
#     role = db.Column(db.String(20), nullable=False)  # 'admin', 'professional', 'customer'

#     def set_password(self, password):
#         self.password_hash = generate_password_hash(password)

#     def check_password(self, password):
#         return check_password_hash(self.password_hash, password)

# class Service(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     price = db.Column(db.Float, nullable=False)
#     description = db.Column(db.Text, nullable=False)

# class ServiceRequest(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     customer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     service_id = db.Column(db.Integer, db.ForeignKey('service.id'))
#     professional_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
#     status = db.Column(db.String(20), default='requested')

#     customer = db.relationship('User', foreign_keys=[customer_id])
#     professional = db.relationship('User', foreign_keys=[professional_id], backref='assigned_requests')
#     service = db.relationship('Service', backref='requests')

# # Forms
# class LoginForm(FlaskForm):
#     username = StringField('Username', validators=[DataRequired(), Length(min=3, max=50)])
#     password = PasswordField('Password', validators=[DataRequired()])
#     submit = SubmitField('Login')

# class RegisterForm(FlaskForm):
#     username = StringField('Username', validators=[DataRequired(), Length(min=3, max=50)])
#     password = PasswordField('Password', validators=[DataRequired()])
#     role = SelectField('Role', choices=[('admin', 'Admin'), ('customer', 'Customer'), ('professional', 'Service Professional')])
#     submit = SubmitField('Register')

# class ServiceForm(FlaskForm):
#     name = StringField('Service Name', validators=[DataRequired()])
#     price = FloatField('Price', validators=[DataRequired()])
#     description = TextAreaField('Description', validators=[DataRequired()])
#     submit = SubmitField('Add Service')

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     form = RegisterForm()
#     if form.validate_on_submit():
#         user = User(username=form.username.data, role=form.role.data)
#         user.set_password(form.password.data)
#         db.session.add(user)
#         db.session.commit()
#         flash('Registration successful!')
#         return redirect(url_for('login'))
#     return render_template('register.html', form=form)

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(username=form.username.data).first()
#         if user and user.check_password(form.password.data):
#             session['user_id'] = user.id
#             session['role'] = user.role
#             flash('Login successful!')
#             return redirect(url_for('dashboard'))
#         else:
#             flash('Invalid credentials')
#     return render_template('login.html', form=form)

# @app.route('/logout')
# def logout():
#     session.clear()
#     return redirect(url_for('home'))

# @app.route('/dashboard')
# def dashboard():
#     if 'user_id' not in session:
#         return redirect(url_for('login'))
#     role = session.get('role')
#     return render_template('dashboard.html', role=role)

# @app.route('/services')
# def services():
#     services = Service.query.all()
#     return render_template('services.html', services=services)

# @app.route('/request_service/<int:service_id>')
# def request_service(service_id):
#     if 'user_id' not in session or session['role'] != 'customer':
#         return redirect(url_for('login'))
#     new_request = ServiceRequest(customer_id=session['user_id'], service_id=service_id, status='requested')
#     db.session.add(new_request)
#     db.session.commit()
#     flash('Service request created!')
#     return redirect(url_for('services'))

# @app.route('/service_requests')
# def service_requests():
#     requests = ServiceRequest.query.all()
#     return render_template('service_requests.html', service_requests=requests)

# @app.route('/admin_dashboard')
# def admin_dashboard():
#     return render_template('admin_dashboard.html')

# @app.route('/add_service', methods=['GET', 'POST'])
# def add_service():
#     form = ServiceForm()
#     if form.validate_on_submit():
#         new_service = Service(name=form.name.data, price=form.price.data, description=form.description.data)
#         db.session.add(new_service)
#         db.session.commit()
#         flash('Service added successfully!')
#         return redirect(url_for('services'))
#     return render_template('add_service.html', form=form)

# if __name__ == '__main__':
    
#     app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField, FloatField
from wtforms.validators import DataRequired, Length
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///services.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # 'admin', 'professional', 'customer'
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    description = db.Column(db.Text, nullable=True)
    service_type = db.Column(db.String(100), nullable=True)
    experience = db.Column(db.Integer, nullable=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=False)
    time_required = db.Column(db.Integer, nullable=False)

class ServiceRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'))
    professional_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    date_of_request = db.Column(db.DateTime, default=datetime.utcnow)
    date_of_completion = db.Column(db.DateTime, nullable=True)
    service_status = db.Column(db.String(20), default='requested')
    remarks = db.Column(db.Text, nullable=True)

    customer = db.relationship('User', foreign_keys=[customer_id])
    professional = db.relationship('User', foreign_keys=[professional_id], backref='assigned_requests')
    service = db.relationship('Service', backref='requests')

# Forms
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    role = SelectField('Role', choices=[('admin', 'Admin'), ('customer', 'Customer'), ('professional', 'Service Professional')])
    submit = SubmitField('Register')

class ServiceForm(FlaskForm):
    name = StringField('Service Name', validators=[DataRequired()])
    price = FloatField('Price', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    time_required = FloatField('Time Required (in minutes)', validators=[DataRequired()])
    submit = SubmitField('Add Service')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, role=form.role.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful!')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            session['user_id'] = user.id
            session['role'] = user.role
            flash('Login successful!')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials')
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('/'))

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    role = session.get('role')
    return render_template('dashboard.html', role=role)

@app.route('/services')
def services():
    services = Service.query.all()
    return render_template('services.html', services=services)

@app.route('/request_service/<int:service_id>')
def request_service(service_id):
    if 'user_id' not in session or session['role'] != 'customer':
        flash("You need to be logged in as a customer to request a service.", "danger")
        return redirect(url_for('login'))

    service = Service.query.get(service_id)
    if not service:
        flash("Invalid service ID.", "danger")
        return redirect(url_for('services'))

    new_request = ServiceRequest(
        customer_id=session['user_id'], 
        service_id=service_id, 
        professional_id=None,  # No professional assigned yet
        date_of_request=datetime.utcnow(),
        service_status='requested',
        remarks=None
    )

    db.session.add(new_request)
    db.session.commit()
    flash('Service request created successfully!', "success")
    return redirect(url_for('services'))


@app.route('/service_requests')
def service_requests():
    requests = ServiceRequest.query.all()
    return render_template('service_requests.html', service_requests=requests)

@app.route('/admin_dashboard')
def admin_dashboard():
    return render_template('admin_dashboard.html')

@app.route('/add_service', methods=['GET', 'POST'])
def add_service():
    form = ServiceForm()
    if form.validate_on_submit():
        new_service = Service(name=form.name.data, price=form.price.data, description=form.description.data, time_required=form.time_required.data)
        db.session.add(new_service)
        db.session.commit()
        flash('Service added successfully!')
        return redirect(url_for('services'))
    return render_template('add_service.html', form=form)



@app.route('/accept_request/<int:request_id>')
def accept_request(request_id):
    service_request = ServiceRequest.query.get(request_id)
    if service_request:
        service_request.service_status = 'accepted'
        db.session.commit()
        flash('Service request accepted!', 'success')
    else:
        flash('Invalid service request!', 'danger')
    return redirect(url_for('service_requests'))

@app.route('/reject_request/<int:request_id>')
def reject_request(request_id):
    service_request = ServiceRequest.query.get(request_id)
    if service_request:
        service_request.service_status = 'rejected'
        db.session.commit()
        flash('Service request rejected!', 'warning')
    else:
        flash('Invalid service request!', 'danger')
    return redirect(url_for('service_requests'))

@app.route('/complete_request/<int:request_id>')
def complete_request(request_id):
    service_request = ServiceRequest.query.get(request_id)
    if service_request:
        service_request.service_status = 'completed'
        service_request.date_of_completion = datetime.utcnow()
        db.session.commit()
        flash('Service marked as completed!', 'success')
    else:
        flash('Invalid service request!', 'danger')
    return redirect(url_for('service_requests'))


if __name__ == '__main__':
    app.run(debug=True)
