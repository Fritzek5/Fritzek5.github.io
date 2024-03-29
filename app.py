from flask import Flask, render_template, url_for
import plotly.graph_objs as go

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
    app.run(debug = True)
