'''
---------------------------------------------------------------
  Main Python file.
  Server created for the purpose of saving user information
  Raspberry Pi B3+
  (c) Minh-An Dao - 2019
  version 1.00 - 22/09/2019
---------------------------------------------------------------
'''
from app import app

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=7497, debug=True)