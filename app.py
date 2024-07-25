from flask import Flask, render_template
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/creativedesign')
def creativedesign():
    return render_template('creativedesign.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/pricing')
def pricing():
    return render_template('pricing.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/seo')
def seo():
    return render_template('seo.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/webdevelopment')
def webdevelopment():
    return render_template('webdevelopment.html')

app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == '__main__':
    app.run()