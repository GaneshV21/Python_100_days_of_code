from flask import Flask, render_template,request,redirect,url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,SelectField
from wtforms.validators import DataRequired,URL
import csv,pandas

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = 'GANESH21'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location_url = StringField('Location',validators=[URL(),DataRequired()])
    open_time = StringField('Open', validators=[DataRequired()])
    closing_time = StringField('Close', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee', choices=['☕️','☕️☕️','☕️☕️☕️','☕️☕️☕️☕️','☕️☕️☕️☕️☕️'])
    wifi_rating = SelectField('Wifi', choices=['✘','💪','💪💪','💪💪💪','💪💪💪💪','💪💪💪💪💪'])
    power_outlet_rating = SelectField('Power', choices=['✘','🔌','🔌🔌','🔌🔌🔌','🔌🔌🔌🔌','🔌🔌🔌🔌🔌'])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add',methods=['GET','POST'])
def add_cafe():
    form = CafeForm()
    if request.method == 'GET':
        return render_template('add.html', form=form)
    else:
        if form.validate_on_submit():
            with open('cafe-data.csv', mode='a',encoding='utf-8', newline='') as file:
                file.write(f"\n{form.cafe.data},{form.location_url.data},{form.open_time.data},{form.closing_time.data},{form.coffee_rating.data},{form.wifi_rating.data},{form.power_outlet_rating.data}")
            return redirect(url_for('cafes'))
        else:
            return render_template('add.html',form=form)




    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)