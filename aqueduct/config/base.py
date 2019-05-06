"""-"""

import os


SETTINGS = {
    'logging': {
        'level': 'DEBUG'
    },
    'service': {
        'port': os.getenv('PORT')
    },
    'carto': {
        'service_account': os.getenv('CARTODB_USER'),
        'uri': 'carto.com/api/v2/sql'
    },
    'geopy': {
        'places_api_key': os.getenv('GP_PRIVATE_KEY')
    }
}
