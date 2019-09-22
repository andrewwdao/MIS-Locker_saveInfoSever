'''
---------------------------------------------------------------
  Main Python file.
  Server created for the purpose of saving user information
  Raspberry Pi B3+
  (c) Minh-An Dao - 2019
  version 1.00 - 22/09/2019
---------------------------------------------------------------
'''
from flask import Flask, render_template
#import datetime
app = Flask(__name__)
@app.route("/")
def hello():
#   now = datetime.datetime.now()
#   timeString = now.strftime("%Y-%m-%d %H:%M")
   templateData = {
      'server_title' : 'MIS Locker System',
      'server_func' : 'Add Guest ID'
#      'time': timeString
      }
   return render_template('index.html', **templateData)
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=7497, debug=True)