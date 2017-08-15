from pandas import concat
class DataTransformer(object):
    def __init__(self):
        return

    def validate(self, data):
        data.dropna(how="any", inplace=True)
        data["intgeo"] = data["geofips"].astype(float)
        data = data[(data.intgeo != 0) & (data.intgeo < 60000)]
        del data["intgeo"]
        return True, data

    def runTransform(self, data):
        valid, transformed = self.validate(data)
        if(valid):
            return transformed[["geofips","value"]]

    def mapGeofips(self, data, lookup):
        del lookup["value"]
        lookup.reset_index(inplace=True)
        merged_one = data.merge(lookup, left_on="value", right_index=True)
        merged_two = merged_one.merge(lookup, left_on="i", right_index=True)
        return merged_two

    def mapNames(self, data, lookup):
        merged_one = data.merge(lookup, left_on="geofips_x", right_on="geofips", suffixes=("a","b"))
        merged_two = merged_one.merge(lookup, left_on="geofips_y", right_on="geofips", suffixes=("c","d"), how="left")
        return merged_two

    def concatenate(self, datasets):
        data = concat(datasets)
        return data

    def clean(self, data):
        del data["i"], data["value"], data["geofips_x"]
        del data["geofips_y"], data["index_x"], data["index_y"]
        data.columns = ["Rank","comparator","comparator_name","index","index_name"]
        return data
