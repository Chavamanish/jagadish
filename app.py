# importing required librarires 
#from curses import flash
#from random import sample
#from select import select
#from ssl import ALERT_DESCRIPTION_USER_CANCELLED
#from tkinter import EXCEPTION, Y
#from tkinter.font import NORMAL
from jkongara_3 import model
from flask import Flask, render_template , request
import pandas as pd



app=Flask(__name__)

# defining the url route for the home page
@app.route('/Home')
def home():
    return render_template('main_page.html')

@app.route('/Home/get_quote')
def quote():
    return render_template('get_quaote.html')   
    


# Fetching the user input data from the web page
@app.route('/',methods=['POST']) 
def get_value():
    t1=request.form['t1']
    t2=request.form['t2']
    t3=request.form['t3']
    t4=request.form['t4']
    t5=request.form['t5']
    t6=request.form['t6']
    t7=request.form['t7']
    t8=request.form['t8']
    t9=request.form['t9']
    t10=request.form['t10']

    # making the prediction for the user generated values
    testcase=pd.DataFrame([[t2,t3,t4,t5,t6,t7,t8,t9,t10]])
    print(t6)
    prediction = model.predict(testcase)


    return render_template('predictions_display.html',v1=t1,v2=t2,v3=t3,v4=t4,v5=t5,v6=t6,v7=t7,v8=t8,v9=t9,v10=t10,pred=prediction)
    #return render_template('index.html',pred=prediction)

    



# Main function for running the app.py file
# The program execution starts from here
if __name__ == '__main__':
    app.run(debug=True)