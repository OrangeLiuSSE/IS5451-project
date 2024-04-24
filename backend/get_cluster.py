from joblib import load


def get_light_cluster(light):
    model = load('cluster/plantcluster_light.joblib')
    cluster = model.predict(light)
    if cluster == 0:
        return "on"
    else:
        return "off"
    

def get_humidity_cluster(humidity):
    model = load('cluster/plantcluster_humidity.joblib')
    cluster = model.predict(humidity)
    if cluster == 0:
        return "on"
    else:
        return "off"