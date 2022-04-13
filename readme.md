# F1 demo data feeder for Kuksa Val
For demonstration purposes.

This application feeds F1 demo data to Kuksa.Val server. Data is sourced with the help of fastf1 library. f1csv.py is a helper tool getting the car data to a csv file.
COVESA VSS signal paths used.
```
"Vehicle.DriveTime"
"Vehicle.Powertrain.CombustionEngine.Engine.Speed"
"Vehicle.OBD.Speed"
"Vehicle.Powertrain.Transmission.Gear"
"Vehicle.Powertrain.CombustionEngine.Engine.TPS"
"Vehicle.Chassis.Brake.PedalPosition"
"Vehicle.TravelledDistance"
```

## Environment variables
```
KUKSAVAL_HOST: <kuksa.val server address>
KUKSAVAL_PORT: <kuksa.val server port>
```