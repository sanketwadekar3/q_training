from flask import Flask

app = Flask(__name__)

@app.route('/')
def cal_fun(var_1=6, var_2=3, operation = "Addition" ):
    if(operation == 'Addition'):
        result = var_1 + var_2
    elif(operation == 'Subtraction'):
        result = var_1 - var_2
    elif(operation == 'Multiplication'):
        result = var_1 * var_2
    elif(operation == 'Division'):
        result = var_1 / var_2
    else:
        result = 'INVALID CHOICE'
    return result

if __name__ == '__main__':
    app.run()