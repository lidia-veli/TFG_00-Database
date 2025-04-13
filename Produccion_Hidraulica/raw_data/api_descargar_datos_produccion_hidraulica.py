import cdsapi

dataset = "sis-energy-derived-reanalysis"
request = {
    "variable": [
        #"hydro_power_generation_reservoirs",
        "hydro_power_generation_rivers",
        
    ],
    "spatial_aggregation": [
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

