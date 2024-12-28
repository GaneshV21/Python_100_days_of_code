from flask import Flask , render_template
import datetime,requests
app = Flask(__name__)

api1="https://api.agify.io/"
api2="https://api.genderize.io/"

api3="https://api.npoint.io/c790b4d5cab58020d391"


@app.route('/')
def home():
    current_year = datetime.datetime.now().year
    return render_template('index.html',year=current_year)



#Task:
@app.route('/guess/<name>')
def guess(name):
    response1 = requests.get(api1,params={
        "name":name
    }).json()
    response2 = requests.get(api2,params={
        "name":name
    }).json()

    print(response1)
    print(response2)
    return render_template("index2.html",name=name,age=response1['age'],gender=response2['gender'])


#blog task
@app.route('/blog')
def blog():
    response3 = requests.get(api3)
    all_posts = response3.json()
    return render_template("blog.html",data=all_posts)

if __name__ == '__main__':
    app.run(debug=True)