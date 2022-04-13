import csv
import time
import logging
import os
import datetime
from itertools import islice
import kuksa_viss_client as kuksa

KUKSAVAL_HOST = os.environ['KUKSAVAL_HOST']
KUKSAVAL_PORT = os.environ['KUKSAVAL_PORT']


def readData(client):
    with open("bottas_monza21race.csv", "r", newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')

        signals_list = next(reader)

        while True:
            csvfile.seek(0)
            prev_time = 0
            for row in islice(reader, 1, None):

                curr_time = row[1]

                if prev_time != 0:
                    curr = datetime.datetime.strptime(curr_time, '%Y-%m-%d %H:%M:%S.%f')
                    prev = datetime.datetime.strptime(prev_time, '%Y-%m-%d %H:%M:%S.%f')
                    delta = (curr-prev).total_seconds()
                else:
                    delta = 0

                for i in range(5, 14):

                    if row[i] != "":
                        drivetime_str = row[5]
                        dt = datetime.datetime.strptime(drivetime_str[7:], '%H:%M:%S.%f') #strip '0 days' from front of string
                        drivetime_seconds = dt.second + dt.minute*60 + dt.hour*3600

                        ### Send values to kuksa.val server
                        client.setValue("Vehicle.DriveTime", drivetime_seconds)
                        client.setValue("Vehicle.Powertrain.CombustionEngine.Engine.Speed", row[6])
                        client.setValue("Vehicle.OBD.Speed", row[7])
                        client.setValue("Vehicle.Powertrain.Transmission.Gear", row[8])
                        client.setValue("Vehicle.Powertrain.CombustionEngine.Engine.TPS", row[9])
                        client.setValue("Vehicle.Chassis.Brake.PedalPosition", row[10])
                        client.setValue("Vehicle.TravelledDistance", (float(row[13]) / 1000) ) # convert meters to kilometers


                time.sleep(delta)
                prev_time = curr_time


def main():
    config = {
        "ip" : KUKSAVAL_HOST,
        "port" : KUKSAVAL_PORT
    }
    client = kuksa.KuksaClientThread(config)
    client.authorize()
    client.start()
    readData(client)


if __name__ == "__main__":
    main()
