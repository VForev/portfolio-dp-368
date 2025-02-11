from flask import Flask
import your_module # this will be your file name; minus the `.py`

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='192.168.1.83', port='8080', debug=True)