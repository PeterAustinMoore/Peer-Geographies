from utils import ExtractData, TransformData, AnalyzeData
import os
if __name__ == "__main__":
    years = 2012
    datasets = []
    extractor = ExtractData.DataExtractor()
    transformer = TransformData.DataTransformer()
    analyzer = AnalyzeData.DataAnalyzer()
    contentsTable = extractor.contents()
    mapper = extractor.mapData()
    for idx, row in contentsTable.iterrows():
        data = extractor.gather(geo=row["geo"], year=years, code=row["code"], api=row["api"])
        valid_data = transformer.runTransform(data)
        output, original = analyzer.analyze(valid_data)
        with_geofips = transformer.mapGeofips(output, original)
        with_names = transformer.mapNames(with_geofips, mapper)
        final = transformer.clean(with_names)
        final["code"] = row["code"]
        final["geo"] = row["geo"]
        datasets.append(final)
    df = transformer.concatenate(datasets)
    df.drop_duplicates(inplace=True)
    filename = "output"
    df.to_csv("{0}/output/{1}.csv".format(os.getcwd(),filename), index=False)
