from flask import *

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('home.html')


@app.route('/categories')
def go_categories():
    return render_template('categories.html', categories = {'Classic': [], 'Fiction': [],
                                                            'Thriller': [], 'History': [],
                                                            'Others': []})


@app.route('/profile')
def go_profile():
    return render_template('profile.html')


@app.route('/registration')
def go_registration():
    return render_template('register.html')


@app.route('/shops')
def go_shops():
    return render_template('shop.html', shops=['BookStore', 'Websites', 'Buy PDF'])


@app.route('/about_us')
def go_about_us():
    return render_template('about_us.html')


@app.route('/reviews')
def go_reviews():
    return render_template('reviews.html')


@app.route('/authors')
def go_authors():
    return render_template('authors.html')


@app.route('/read_in')
def go_read_in():
    return render_template('read_in.html')

@app.route('/login')
def go_login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
