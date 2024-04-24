from joblib import dump, load
import pandas as pd
import time
import sqlite3
import numpy as np
from sklearn.cluster import KMeans


def main():
    print('Starting light cluster training process')
    np.random.seed(int(round(time.time())))
    while True:
        try:                        
            conn = sqlite3.connect('data/project.db')
            c = conn.cursor()
            c.execute('SELECT id, light, timestamp FROM light ORDER BY id ASC')
            results = c.fetchall()
            df = pd.DataFrame(columns=['id', 'light', 'timestamp'])
            for result in results:                                 
                df = df.append({'id': result[0], 'light': result[1], 'timestamp': str(result[2])}, ignore_index=True)
            X = df['light'].values.reshape(-1,1)
            kmeans = KMeans(n_clusters=2, random_state=0)
            kmeans = kmeans.fit(X)
            result = pd.concat([df['light'], pd.DataFrame({'cluster':kmeans.labels_})], axis=1)
            for cluster in result.cluster.unique():
                print('{:d}\t{:.3f} ({:.3f})'.format(cluster, result[result.cluster==cluster].light.mean(), result[result.cluster==cluster].light.std()))
            dump(kmeans, 'plantcluster_light.joblib')
            
            
            c.execute('SELECT id, humidity, temperature, timestamp FROM light ORDER BY id ASC')
            results = c.fetchall()
            df = pd.DataFrame(columns=['id', 'humidity', 'timestamp'])
            for result in results:                                 
                df = df.append({'id': result[0], 'humidity': result[1], 'timestamp': str(result[2])}, ignore_index=True)
            X = df['humidity'].values.reshape(-1,1)
            kmeans = KMeans(n_clusters=2, random_state=0)
            kmeans = kmeans.fit(X)
            result = pd.concat([df['humidity'], pd.DataFrame({'cluster':kmeans.labels_})], axis=1)
            for cluster in result.cluster.unique():
                print('{:d}\t{:.3f} ({:.3f})'.format(cluster, result[result.cluster==cluster].light.mean(), result[result.cluster==cluster].light.std()))
            dump(kmeans, 'plantcluster_humidity.joblib')
            time.sleep(10)
                           
        except Exception as error:
            print('Error: {}'.format(error.args[0]))
            continue
        except KeyboardInterrupt:
            print('Program terminating...')    
            break