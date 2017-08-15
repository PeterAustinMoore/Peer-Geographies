from sklearn import neighbors
from sklearn import preprocessing
import pandas as pd
class DataAnalyzer(object):
    def __init__(self):
        return
    def analyze(self, data):
        X = data["value"]
        Y = data["geofips"].astype(object)
        knn = neighbors.KNeighborsClassifier()
        neighbor = neighbors.NearestNeighbors(n_neighbors=7, algorithm="brute")
        fit = knn.fit(X.to_frame(), Y.to_frame().values.ravel())
        p = neighbor.fit(X.to_frame())
        pred = p.kneighbors(X.to_frame())
        predicted = pred[1]
        cols = ["i","1","2","3","4","5","6"]
        df = pd.DataFrame(predicted, columns=cols)
        df_melt = pd.melt(df, id_vars=["i"])
        return df_melt, data
