from flask import Flask, render_template,request,redirect,redirect
from urllib.parse import urlparse, urlunparse, parse_qs,urlencode
app = Flask(__name__)
app.secret_key = "super secret key"
def amazonify(url):
    new_url = urlparse(url)
    if not new_url.netloc:
        return None
    query_dict = parse_qs(new_url[4])
    query_dict['tag'] = "krishnaventur-21"
    new_url = new_url[:4] + (urlencode(query_dict, True), ) + new_url[5:]
    return urlunparse(new_url)

@app.route('/')
def home():
        return render_template('login.html')

@app.route('/login/', methods = ['POST'])
def login():
    # if request.method == 'GET':
    #     return render_template('login.html')
    if request.method == 'POST':
        url = request.form['url']
        try:
            ind=url.find("http")
            if(ind==-1):
                return render_template('login.html',error_message="Please Try again and Check the link")
            url=amazonify(url)
            return redirect(url, code=302)
        except ValueError:
            return render_template('login.html',error_message="Please Try again and check the link")
if __name__ == '__main__':
    app.run(debug=True)