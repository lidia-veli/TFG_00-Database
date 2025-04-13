import cdsapi

dataset = "sis-energy-derived-reanalysis"
request = {
    "variable": [
        "electricity_demand"
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

# en conda CMD ejecutar:
# conda activate base (donde está la librería cdsapi)
# python api_descargar_datos_demanda_electrica.py

