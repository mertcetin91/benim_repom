from flask import Flask, render_template, request, url_for

app = Flask(__name__)



def convert(entry):  
    a = entry // 3600000  #saat
    b = (entry - 3600000 * (entry // 3600000)) // 60000   #dakika
    c = (entry - 3600000 * (entry // 3600000))   
    d = (c - 60000 * (c // 60000)) // 1000      #saniye
    x = entry 
        
    if entry < 1000:
        return f" just {x} millisecond/s"
    elif 1000 <= entry < 60000:
        return f"{d} second/s"
    elif 60000 <= entry < 3600000:
        return f"{b} minute/s {d} second/s" if b and d > 0 else f"{b} minute/s"
    elif entry >= 3600000:
        return f"{a} hour/s {b} minute/s {d} second/s" if a and b and d > 0 else f"{a} hour/s"

@app.route("/")
def home():
    return render_template("index.html", developer_name = "E2079-MERT", not_valid = False)
    
@app.route("/", methods=["POST"])
def result():
    if request.method == "POST":
        num = request.form.get("number") #num=girilecek olan sayı
        if not num.isdigit() or int(num) <= 0 :
            return render_template("index.html",  developer_name = "E2079-MERT", not_valid = True)
        return render_template("result.html", developer_name = "E2079-MERT", milliseconds = int(num), result = convert(int(num)))
    



if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=80)
    
    
    
    
    


    


       