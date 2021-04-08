from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    rnd_num = random.randint(1, 10)
    cp_year = datetime.date.today().year
    return render_template('index.html',
                           num=rnd_num,
                           year=cp_year)


@app.route('/guess/<name>')
def guess(name):
    # Genderize.io
    gender_response = requests.get(f'https://api.genderize.io?name={name}')
    gender_data = gender_response.json()["gender"]

    # Agify.io
    age_response = requests.get(f'https://api.agify.io?name={name}')
    age_data = age_response.json()["age"]

    return render_template('guess.html',
                           name=name,
                           gender=gender_data,
                           age=age_data)
@app.route('/blog')
def blog():
    blog_url = 'https://api.npoint.io/5abcca6f4e39b4955965'
    blog_response = requests.get(url=blog_url)
    blog_data = blog_response.json()

    return render_template('blog.html',
                           posts=blog_data)

if __name__ == "__main__":
    app.run(debug=True)
