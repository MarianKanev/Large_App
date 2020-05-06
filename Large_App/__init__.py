from flask import Flask
app = Flask(__name__)

# Import here all py files with route functions
# This way you can split Flask routes in different py files 

import Large_App.views
import Large_App.views2
import Large_App.views3