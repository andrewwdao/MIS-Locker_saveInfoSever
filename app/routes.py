from flask import render_template
from app import app
from app.forms import InfoForm

@app.route('/')
@app.route('/index')
def index():
    form = InfoForm()
    templateData = {
        'server_title' : 'MIS Locker System',
        'server_func' : 'Add Guest ID',
        'form' : form
        #'time': timeString
    }
    return render_template('index.html', **templateData)

#if __name__ == "__main__":
  #app.run(host='0.0.0.0', port=7497, debug=True)