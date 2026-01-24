from flask import Flask, render_template, request, redirect,url_for

app = Flask(__name__)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        branch = request.form['branch']

        return render_template(
            'success.html',
            name=name,
            email=email,
            branch=branch
        )

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']

        if email == "":
            return "Email is required"

        return render_template('success.html', email=email)

    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
