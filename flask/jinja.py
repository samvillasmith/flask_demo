from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to Flask! This is a test of basic functions.'

@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/submit", methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        return f'Hey {name}! Your email is {email}'
    return render_template('form.html')

@app.route('/success/<int:score>')
def success(score):
    res = ''
    if score > 50:
        res = "PASS"
    else:
        res = "FAIL"
    
    exp = {'score': score, 'res': res}
    return render_template('result1.html', results=exp)

@app.route('/successif/<int:score>')
def successif(score):
    return render_template('result2.html', results=score)

@app.route('/fail/<int:score>')
def fail(score):
    return render_template('result2.html', results=score)

@app.route('/get_results', methods=['POST', 'GET'])
def get_results():
    if request.method == 'POST':
        science = int(request.form['science'])
        math = int(request.form['math'])
        english = int(request.form['english'])
        total_score = science + math + english
        return redirect(url_for('successif', score=total_score))
    
    # Show the form for GET requests
    return render_template('getresults.html')

if __name__ == '__main__':
    app.run(debug=True)