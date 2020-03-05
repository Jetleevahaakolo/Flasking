from flask import Flask, render_template      
import Webscrapper

app = Flask(__name__)

consoles = Webscrapper.GetConsoles()

average = Webscrapper.AveragePrice(consoles)

@app.route("/")
def home():
    return render_template("home.html", len1 = len(consoles)-1, list1 = consoles, average = average)

if __name__ == "__main__":
    app.run(debug=True)