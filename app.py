from flask import Flask
import logging
from controlers.data_controler import date_bp
from controlers.area_controler import area_bp


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

if __name__ == '__main__':
    app.register_blueprint(area_bp, url_prefix="/api/area")
    app.register_blueprint(date_bp, url_prefix="/api/date")
    app.run(debug=True)
