from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', devices = sensor_request())
def sensor_request():
    headers = {
    }
    data = {
    }
    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        print("Device info retrieved.")
        if response.text.strip():
            text = response.json()
            return parse_json_text(text)
        else:
            print("Response is empty.")
    else:
        print(f"Error: {response.status_code}")

def parse_json_text(json_data):
    devices = []
    try:
        for device in json_data.get('devices', []):
            device_name = device.get('name', 'Unknown')
            group_name = device.get('group', {}).get('name', 'Unknown')
            battery = device.get('battery', 'Unknown')

            temperature = None
            humidity = None

            for channel in device.get('channel', []):
                if channel.get('name') == 'Temperatura':
                    temperature = channel.get('value')
                elif channel.get('name') == 'Wilgotność':
                    humidity = channel.get('value')

            device_data = {
                'Device Name': device_name,
                'Group Name': group_name,
                'Temperatura': temperature,
                'Wilgotnosc': humidity,
                'Battery': battery
            }

            devices.append(device_data)
    except Exception as e:
        print(f"Error: {e}")

    return devices

if __name__ == '__main__':
    app.run(debug=True)
