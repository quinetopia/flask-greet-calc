# Put your app in here.

from flask import Flask, request
import operations

app = Flask(__name__)


@app.route('/math/<maths>')
def doing_math(maths):
    """comment here"""
    a = request.args["a"]
    b = request.args["b"]
    
    result = 0

    if maths == "add":
        result = operations.add(int(a), int(b))
    elif maths == "sub":
        result = operations.sub(int(a), int(b))
    elif maths == "mult":
        result = operations.mult(int(a), int(b))
    elif maths == "div":
        result = operations.div(int(a), int(b))

    html = f"<html><body><h1>{result}</h1><body></html>"
    return html
