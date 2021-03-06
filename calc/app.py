# Put your app in here.

from flask import Flask, request
import operations

app = Flask(__name__)


@app.route('/math/<maths>')
def doing_math(maths):
    """
    Implementing basic math functions. Function required passed as last 
    element of the resource, arguments passed in query string 
    """
    _math_func_ = {"add": operations.add , "sub" : operations.sub , "mult" : operations.mult , "div" : operations.div}
    a = request.args["a"]
    b = request.args["b"]

    
    result = 0

    result = _math_func_[maths](int(a), int(b))

    # if maths == "add":
    #     result = operations.add(int(a), int(b))
    # elif maths == "sub":
    #     result = operations.sub(int(a), int(b))
    # elif maths == "mult":
    #     result = operations.mult(int(a), int(b))
    # elif maths == "div":
    #     result = operations.div(int(a), int(b))

    html = f"<html><body><h1>{result}</h1><body></html>"
    return html
