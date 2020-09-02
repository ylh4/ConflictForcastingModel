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

        forecastingdate = datetime.fromtimestamp(int(forecastingdate.timestamp())).strftime('%d %b, %Y')
        return render_template('forecasting.html', result= months, path = file_path)
    else:
        return render_template('forecasting.html', result= " Result will be displayed here " )
@APP.route("/Predictors/")
def predictors():
    return render_template('predictors.html')
@APP.route("/Evaluation")
def evaluation():
    return render_template('model_evaluation.html')
 
embed = """
<div id="observablehq-ccd29192"></div>
<script type="module">
import {Runtime, Inspector} from "https://cdn.jsdelivr.net/npm/@observablehq/runtime@4/dist/runtime.js";
import define from "https://api.observablehq.com/d/eceaa744227c4fea.js?v=3";
const inspect = Inspector.into("#observablehq-ccd29192");
(new Runtime).module(define, name => (name === "vegaPetals") && inspect());
</script>
"""  
@APP.route("/contact_us/") 
def hello_world():
    return f"""<html>
  <h1>This is web page served with Flask</h1>
  {embed}
</html>"""
if __name__ == "__main__":
    APP.run(debug=True)

