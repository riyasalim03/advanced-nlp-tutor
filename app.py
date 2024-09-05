import correction_api
from flask import Flask,render_template,redirect
from flask import request
from flask import jsonify

app= Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

tutor = correction_api.Tutor(); 
int_corrections = 0

@app.route("/")
@app.route("/home")
def index():

    print(tutor.get_suggestion_list())  
    return render_template("index.html",sugg=tutor.get_suggestion_list())


@app.route('/sendto', methods=['POST'])
def sendto():

    res_str=""

    output = request.get_json()

    for i in output["ops"]:
        res_str+=i["insert"]

    api_result = tutor.send(res_str)
    tutor.make_correction_list(api_result)

    print(api_result)
    
    return render_template("correction_template.html",sugg=tutor.get_suggestion_list())

@app.route('/result',methods=['GET'])

def temm():
    return render_template("correction_template.html",sugg=tutor.get_suggestion_list())

@app.route('/update',methods=['POST'])
def updattt():
    
    return jsonify(tutor.sugg_list)


if __name__ == "__main__":
    app.run(debug=True)
