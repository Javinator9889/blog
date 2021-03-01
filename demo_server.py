import flask



app = flask.Flask(__name__,
                  static_url_path='/',
                  static_folder='public/')

@app.route('/')
def root():
    return app.send_static_file('index.html')


app.run(port=8080)
