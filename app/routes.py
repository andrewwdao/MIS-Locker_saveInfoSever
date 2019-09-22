from app import app

@app.route('/')
@app.route('/index')
def index():
    templateData = {
        'server_title' : 'MIS Locker System',
        'server_func' : 'Add Guest ID'
        #'time': timeString
    }
    return render_template('index.html', **templateData)
