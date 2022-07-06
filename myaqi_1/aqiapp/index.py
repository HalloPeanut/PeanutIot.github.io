from flask import  Flask, render_template, request
from models import *

# create an app in flask
app = Flask(__name__)

@app.route("/")
def home():
    sensor_list = ['node2','node6',]
    sensor_name = 'node2'
    my_sensor_data = []
    pm25 = []
    temp = []
    hum = []
    sensor_name = request.args.get("choose_node")
    #print(sensor_name)

    for sensor in sensor_list:
        my_sensor = MyNode(sensor)
        my_sensor.get_last_data()
        my_sensor_data.append(my_sensor.node_data)

        if sensor == sensor_name:
            my_sensor.get_online_data_chart()
            pm25 = my_sensor.node_data_pm25
            temp = my_sensor.node_data_temp
            hum = my_sensor.node_data_hum

    print(temp)

    #print(my_sensor_data)

    return render_template("index.html",data=my_sensor_data,pm25=pm25,name=sensor_name,
                           date_time=my_sensor.date_time,temp=temp,hum=hum)

if __name__=="__main__":
    # run app
    app.run(debug=True)