from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/')  # Menambahkan rute untuk halaman utama
def home():
    return render_template('login.html')  # Mengembalikan halaman login saat mengakses rute utama

@app.route('/success/<name>')
def success(name):
    return 'Welcome %s' % name

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        return render_template('login.html')  # Menampilkan kembali halaman login jika bukan POST

if __name__ == '__main__':
    app.run(debug=True)
