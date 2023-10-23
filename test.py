from flask import Flask, request


app= Flask(__name__) # acts as a wrapper class, we are creating a flask application

@app.route('/add')
def addition():
    return f"this is my test func"

@app.route('/navya')
def print_name():
    return f"navya nair"

@app.route("/user")
def print_user():
    data=request.args.get("name") # geting a value for the function
    return f"{data}"

if __name__=="__main__":
    app.run(host="0.0.0.0")
