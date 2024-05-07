from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return """
    <html>
        <head>
            <title>Welcome to the Birding App!</title>
        </head>
        <body>
            <h1>Welcome to the Birding App!</h1>
            <p><a href="/sighting">Record a new bird sighting</a></p>
            <p><a href="/about">About This App</a></p>
        </body>
    </html>
    """

@app.route('/sighting', methods=['GET'])
def sighting_form():
    return render_template('SightingForm.html')

@app.route('/submit_sighting', methods=['POST'])
def submit_sighting():
    try:
        # Retrieve data from form
        species = request.form['species']
        location = request.form['location']
        date = request.form['date']
        time = request.form['time']

        # Add data saving microservice here
        print(f"Received sighting: {species}, {location}, {date} at {time}")

        return redirect(url_for('index'))
    except KeyError as e:
        return "Error: Missing Data", 400

@app.route('/about')
def about():
    return render_template('About.html')

if __name__ == '__main__':
    app.run(debug=True)