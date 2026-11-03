from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/galeria')
def galeria():
    return render_template('galeria.html')

@app.route('/video')
def video():
    return render_template('video.html')

@app.route('/musica')
def musica():
    return render_template('musica.html')

@app.route('/galaxia')
def galaxia():
    return render_template('galaxia.html')

if __name__ == '__main__':
    app.run(debug=True)