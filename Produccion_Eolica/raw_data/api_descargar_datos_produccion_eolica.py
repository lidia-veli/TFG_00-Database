import cdsapi

dataset = "sis-energy-derived-reanalysis"
request = {
    "variable": [
        #"wind_power_generation_offshore"
        "wind_power_generation_onshore"
        
    ],
    "spatial_aggregation": [
        #"maritime_country_level"
        "country_level"
    ],
    "energy_product_type": [
        "energy"
    ],
    "temporal_aggregation": [
        "daily"
    ],

}

client = cdsapi.Client()
client.retrieve(dataset, request).download()

