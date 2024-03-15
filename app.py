from flask import Flask, render_template

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('home.html', active_page='home')

@app.route('/services')
def services():
    return render_template('services.html', active_page='services')

@app.route('/clients')
def clients():
    return render_template('clients.html', active_page='clients')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html', active_page='gallery')

@app.route('/contact')
def contact():
    return render_template('contact.html', active_page='contact')


if __name__ == '__main__':
    app.run(debug=True)