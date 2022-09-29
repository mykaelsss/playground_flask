from flask import Flask, render_template


app = Flask(__name__)
@app.route('/')
def hello():
    return "Hello"


@app.route('/play')
@app.route('/play/<int:x>')
@app.route('/play/<int:x>/<color>')
def play_num(x=3, color ="#9FC5F8"):
    return render_template("index.html", x=x, color=color)



if __name__=="__main__":
    app.run(debug=True, port = 5001)
