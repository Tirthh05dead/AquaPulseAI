import pandas as pd

def load_station_data():

    return pd.DataFrame({

        "Station":[
            "North Zone",
            "South Zone",
            "East Zone",
            "West Zone",
            "Central Zone"
        ],

        "pH":[
            7.2,
            6.8,
            5.4,
            7.1,
            6.9
        ],

        "TDS":[
            90,
            140,
            430,
            120,
            100
        ],

        "Turbidity":[
            1,
            2,
            8,
            2,
            1
        ],

        "Temperature":[
            25,
            27,
            31,
            26,
            25
        ],

        "Latitude":[
            12.9716,
            12.9750,
            12.9780,
            12.9820,
            12.9860
        ],

        "Longitude":[
            77.5946,
            77.6000,
            77.6050,
            77.6100,
            77.6150
        ]
    })

def load_forecast_data():

    return pd.DataFrame({

        "Day":[
            "Mon",
            "Tue",
            "Wed",
            "Thu",
            "Fri",
            "Sat",
            "Sun"
        ],

        "Demand":[
            100,
            112,
            125,
            138,
            150,
            164,
            178
        ]
    })

def load_ai_actions():

    return pd.DataFrame({

        "Priority":[
            1,
            2,
            3
        ],

        "Action":[
            "Inspect East Zone",
            "Increase Water Sampling",
            "Deploy Mobile Filtration Unit"
        ],

        "Urgency":[
            "High",
            "Medium",
            "Low"
        ]
    })