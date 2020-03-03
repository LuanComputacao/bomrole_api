def change_db_engine_to_gdal(db_engine):
    if db_engine.endswith('psycopg2'):
        db_engine = 'django.contrib.gis.db.backends.postgis'
    elif db_engine.endswith('psycopg2'):
        db_engine = 'django.contrib.gis.db.backends.spatialite'
    return db_engine
