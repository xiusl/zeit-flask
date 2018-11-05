from app import app

@app.route('/')
def index():
    return "Hello, Python World!"


@app.route('/hi')
def xiu():
    return "Hello, shilin!"

