from google.cloud import datastore

client = datastore.Client()

def addMetric(metric, key):
    client.key('Metric', key)
    
    metric_entity = datastore.Entity(key=key)
    metric_entity.update(metric)

    client.put(metric_entity)
