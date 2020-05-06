from Large_App import app

@app.route('/2')
def index2():
    return 'Hello World 2!'