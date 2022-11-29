from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    """Greet input name."""
    return f"Hello {name}"


@app.route('/f/<celsius>')
def convert_celsius_to_fahrenheit(celsius):
    """Convert temperature from celsius to fahrenheit."""
    fahrenheit = float(celsius) * 9.0 / 5 + 32
    return f"Temperature of {celsius} C is equivalent to {fahrenheit} F."


if __name__ == '__main__':
    app.run()
