from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

def convert_roman(decimal_num):
    # set the dictionary for roman numerals
    roman = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',
             50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    # initialize the result variable
    num_to_roman = '' 
    # loop the roman numerals, calculate for each symbol and add to the result
    for i in roman.keys():
        num_to_roman += roman[i] * (decimal_num // i)
        decimal_num %= i      
    return num_to_roman 

@app.route("/", methods = ["GET"]) 
def head():
    return render_template("index.html", developer_name="E2079-Mert", not_valid=False)

@app.route("/", methods = ["POST"]) 
def result():
    if request.method == "POST":
        num = request.form.get("number")
        if (not num.isdecimal()) or (not (0 < int(num) < 4000)):
            return render_template("index.html", not_valid = True, developer_name = "E2079-Mert")
        return render_template("result.html", developer_name = "E2079-Mert", number_decimal = num, number_roman = convert_roman(int(num)))
    else:
        return redirect(url_for("index"))



if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=80)
    