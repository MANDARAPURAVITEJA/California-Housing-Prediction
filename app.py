from flask import Flask
from housing.logger import logging
from housing.exception import HousingException
import sys

app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    try:
        raise Exception("This is a custom exception using for testing")
    except Exception as e:
        housing=HousingException(e,sys)
        logging.info(housing.error_message)
    logging.info("Testing the logging package")
    return "Starting Machine Learning Project"

if __name__=="__main__":
    app.run(debug=True)