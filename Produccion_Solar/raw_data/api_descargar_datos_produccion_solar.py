import cdsapi

dataset = "sis-energy-derived-reanalysis"
request = {
    "variable": [
        "solar_photovoltaic_power_generation"
    ],
    "spatial_aggregation": [
        "country_level"
    ],
    "energy_product_type": [
        "capacity_factor_ratio",
        "energy",
        "power"
    ],
    "temporal_aggregation": [
        "daily"
    ],

}

client = cdsapi.Client()
client.retrieve(dataset, request).download()

# en conda CMD ejecutar:
# conda activate base (donde está la librería cdsapi)
# python api_descargar_datos_produccion_solar.py

