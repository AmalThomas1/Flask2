from flask import Flask,request,render_template



app=Flask(__name__)


@app.route('/')
def welcome():
    return 'welcome'


@app.route('/cal', methods=['GET'])
def math_operator():
    operation=request.json['operation']
    num1=request.json['num1']
    num2=request.json['num2']

    if operation=='add':
        return num1+num2
    elif operation=='division':
        return num1/num2
    elif operation=='multiplication':
        return num1*num2
    else:
        return num1-num2


if __name__=='__main__':
    app.run(debug=True)




    
