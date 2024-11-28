from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return "<h1>Hello World :)</h1>"


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}."


@app.route('/c_to_f/<celsius>')
def convert_celsius_to_fahrenheit(celsius):
    """Convert celsius to fahrenheit."""
    return f"""Celsius: {float(celsius):.2f} <br>
Fahrenheit: {float(celsius) * 9 / 5 + 32:.2f}"""


@app.route('/f_to_c/<fahrenheit>')
def convert_fahrenheit_to_celsius(fahrenheit):
    """Convert fahrenheit to celsius."""
    return f"""Fahrenheit: {float(fahrenheit):.2f} <br>
Celsius: {(float(fahrenheit) - 32) * 5 / 9:.2f}"""


if __name__ == '__main__':
    app.run()
