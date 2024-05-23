from flask import Flask, render_template, request

app = Flask(__name__)

# Define the color code dictionary
color_codes = {
    'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green': 5,
    'blue': 6,
    'violet': 7,
    'gray': 8,
    'white': 9
}

# Define tolerance codes
tolerance_codes = {
    'brown': 1,
    'red': 2,
    'green': 0.5,
    'blue': 0.25,
    'violet': 0.1,
    'gray': 0.05,
    'gold': 5,
    'silver': 10
}

# Function to calculate resistance
def calculate_resistance(band1, band2, band3, multiplier, tolerance):
    try:
        digit1 = color_codes[band1]
        digit2 = color_codes[band2]
        digit3 = color_codes[band3]
        multiplier_value = 10 ** color_codes[multiplier]
        tolerance_value = tolerance_codes.get(tolerance, None)
        resistance = (digit1 * 100 + digit2 * 10 + digit3) * multiplier_value
        return resistance, tolerance_value
    except KeyError:
        return None, None

@app.route('/', methods=['GET', 'POST'])
def index():
    resistance = None
    tolerance_value = None
    band1 = band2 = band3 = multiplier = tolerance = None
    if request.method == 'POST':
        band1 = request.form.get('band1')
        band2 = request.form.get('band2')
        band3 = request.form.get('band3')
        multiplier = request.form.get('multiplier')
        tolerance = request.form.get('tolerance')
        resistance, tolerance_value = calculate_resistance(band1, band2, band3, multiplier, tolerance)
    return render_template('index.html', resistance=resistance, tolerance_value=tolerance_value,
                           band1=band1, band2=band2, band3=band3, multiplier=multiplier, tolerance=tolerance,
                           color_codes=color_codes, tolerance_codes=tolerance_codes)

if __name__ == '__main__':
    app.run(debug=True)
