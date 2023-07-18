import cdsapi

c = cdsapi.Client()

c.retrieve(
    'reanalysis-era5-pressure-levels',
    {
        'product_type': 'reanalysis',
        'format': 'netcdf',
        'variable': [
            'geopotential', 'relative_humidity', 'temperature',
            'u_component_of_wind', 'v_component_of_wind',
        ],
        'pressure_level': [
            '50', '500', '850',
            '1000',
        ],
        'year': '2023',
        'month': '3',
        'day': '27',
        'time': [
            '00:00', '06:00', '12:00',
            '18:00',
        ],
    },
    '/workspace/python/source_code/FCN/data/ERA5/mar_2023_27_pl.nc')
