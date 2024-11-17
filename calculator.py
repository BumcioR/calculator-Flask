from flask import Flask, request

# http://127.0.0.1:5000/calculate?op=sum&arg1=2&arg2=5

# Initialize a flask application
app = Flask(__name__)

# Define the route to homepage
@app.route('/calculate')
def calculate():

    # Get the operand
    op = request.args.get('op', type=str)
    # Get arguments
    arg1 = request.args.get('arg1', type=int)
    arg2 = request.args.get('arg2', type=int)

    # Perform requested operation:
    if op == 'sum':
        return str(arg1 + arg2)
    elif op == 'subtract':
        return str(arg1 - arg2)
    elif op == 'multiply':
        return str(arg1 * arg2)
    elif op == 'divide':
        return str(arg1 / arg2)

    else:
        "Error: missing some data"

if __name__ == '__main__':
    app.run()
