from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Smart Student Placement Management System</h1>"
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        branch = request.form['branch']

        return f"""
        <h2>Registration Successful</h2>
        <p>Name: {name}</p>
        <p>Email: {email}</p>
        <p>Branch: {branch}</p>
        """

    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
