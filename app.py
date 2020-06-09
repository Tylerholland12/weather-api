from flask import Flask, render_template
import requests
import json

app = Flask(__name__, template_folder='.')

@app.route('/')
def main():
    params = {
    'api_key': '{API_KEY}',
    }
    r = requests.get(
        'https://www.parsehub.com/api/v2/projects/{PROJECT_TOKEN}/last_ready_run/data',
        params=params)
        
    return render_template('weather.html', weather=json.loads(r.text)[''])

    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)