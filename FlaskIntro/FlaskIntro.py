from flask import *
from datetime import *

app = Flask(__name__)

images_on_sever = [
    {
        "src": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSPWZNJkKcjT8zEPVwcWC78wAAysC6jlDr3cA2zgtHlOiQYtpZ_Kg",
        "title": "loading screen 1",
        "tags": "tag 1"
        },
    {
        "src": "https://www.wired.com/wp-content/uploads/2016/03/GW20160134040.jpg",
        "title": "loading screen 2",
        "tags": "tag 2"
    },
    {
        "src": "https://s-media-cache-ak0.pinimg.com/736x/f4/5e/9d/f45e9dbac8cac965a7aa5085a8ed6c3e.jpg",
        "title": "loading screen 3",
        "tags": "tag 3"
    }
]

@app.route('/')
def hello_world():
    return redirect(url_for("dota"))


current_time = str(datetime.now())
number_of_visitor = 0


@app.route('/login')
def login():
    global number_of_visitor
    number_of_visitor += 1
    current_time = str(datetime.now())
    return render_template("login.html", current_time=current_time, number_of_visitor=number_of_visitor)


@app.route('/dota')
def dota():
    return render_template("dota.html", images=images_on_sever)


@app.route('/contact')
def information():
    return render_template("contact.html")


if __name__ == '__main__':
    app.run()
