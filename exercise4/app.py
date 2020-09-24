from flask import Flask, escape, request, render_template
import requests

app = Flask(__name__)

@app.route('/welcome/<name>')
def index(name):
    return "Greetings sire, the Docker universe awaits you! "+name#+ request.args.get("name")
    #return render_template('welcome.html', page_title='Home')

@app.route("/weather/<city>")
def weather(city):
    response = requests.get("https://www.metaweather.com/api/location/search/?query="+city)
    data = response.json()

    response = requests.get("https://www.metaweather.com/api/location/"+str(data[0]['woeid']))
    data = response.json()    
    temp = data['consolidated_weather'][0]['the_temp']
    return "The temperature in " +city+ "is: " +str(round(temp))


if __name__ == "__main__":
    app.run(host='0.0.0.0')
