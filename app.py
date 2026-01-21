from flask import Flask, render_template, request

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

if __name__ == '__main__':
    app.run(debug=True)
