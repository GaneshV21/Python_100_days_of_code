from flask import Flask, render_template,request
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,ValidationError
from flask_bootstrap import Bootstrap5
# documentation link = https://wtforms.readthedocs.io/en/3.0.x/fields/#basic-fields

app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.secret_key = "some secret string"

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = MyForm()
    if request.method == "POST":
        if form.validate_on_submit():
            if form.email.data == "ganesh@gmail.com" and form.password.data == "123":
                return render_template('success.html')
            else:
                return render_template('denied.html')
        else:
            return render_template('login.html', form=form)
    else:
        return render_template('login.html',form=form)


class MyForm(FlaskForm):
    email = StringField('email',validators=[Email(message="Invalid email address")])
    password = PasswordField('password',validators=[DataRequired(message="Field must be at least 8 characters long")])
    login = SubmitField("login")

if __name__ == '__main__':
    app.run(debug=True)
