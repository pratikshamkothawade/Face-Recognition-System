from flask import Flask, render_template,request
server = Flask(__name__)

@server.route("/")
@server.route("/verify")
def verify():
    return render_template('Page.html')

@server.route("/result", methods = ['POST',"GET"])
def result():
    output = request.form.to_dict()
    name = output["name"]

    return render_template("Page.html",name = name)

if __name__ == '__main__':
    server.run(debug=True,port=5001)