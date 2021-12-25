from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def home():
    PPB = ''
    COGs = ''
    PPC = ''
    if request.method == "POST":
            
        req = request.form
            
        selling_price = float(req["selling_price"])  # another option is--->   bottle_cost = request.form["bottle_cost"] the name attribute is inside brackets
        case_cost = float(req["case_cost"])
        case_size = float(req["case_size"])
            
        PPB = round(case_cost/case_size, 2)
            # COGs = bottle_cost/PPB
            # PPC =(PPB-bottle_cost)*24
        print(PPB)

        # return redirect(request.url)
    return render_template("home.html", PPB=PPB)

@app.route('/about/')
def about():
    return render_template("about.html")






if __name__ == "__main__":
    app.run(debug=True)
    
    