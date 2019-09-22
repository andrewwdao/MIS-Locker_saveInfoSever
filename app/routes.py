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

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=7497, debug=True)