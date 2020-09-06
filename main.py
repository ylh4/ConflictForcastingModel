from flask import Flask, render_template, request 
from datetime import datetime
APP = Flask(__name__ , template_folder='template')


def index():
    return render_template('index.html')
@APP.route('/')
@APP.route("/home")
def home():
    return render_template('home.html')

@APP.route("/Model/")
def methodology():
    return render_template('methodology.html')
@APP.route("/Analysis/")
def expanalysis():
    return render_template('explaratory.html')
    

@APP.route("/Forecast/", methods=['POST', 'GET'])
def forecast():
    if request.method == 'POST':
        result=request.form.to_dict()
        forecastingdate = datetime.strptime(result['conflictmonth'], '%Y-%m')
        months = datetime.fromtimestamp(int(forecastingdate.timestamp())).strftime('%Y-%m')
        file_path = '/static/dashboard_forecast_' + months + '.json'
        forecastingdate = datetime.fromtimestamp(int(forecastingdate.timestamp())).strftime('%b, %Y')
        return render_template('forecasting.html', result= forecastingdate, path = file_path)
    else:
        return render_template('forecasting.html', result= " Result will be displayed here " )
@APP.route("/Predictors/")
def predictors():
    return render_template('predictors.html')
@APP.route("/Evaluation/")
def evaluation():
    return render_template('model_evaluation.html')

@APP.route("/Mselection/")
def mselection():
    return render_template('model_selection.html')
 
@APP.route("/contact_us/") 
def hello_world():
    return render_template ('contact_us.html')
if __name__ == "__main__":
    APP.run(debug=True)

