from pandas import read_json, concat
from requests import Session

class DataExtractor(object):
    def __init__(self):
        return
    def gather(self, geo, year, code, api):
        """
        Return dataframe for the geography, year, code
        """
        url = ""
        if(geo != "COUNTY"):
            url = api+"?$select=year,code,value,geofips&$where=year='{0}' and code='{1}'&$limit=10000".format(year, code)
        else:
            url = api+"?$select=year,code,value,geofips&$where=year='{0}' and code='{1}' and geofips not like '%25000'&$limit=100000".format(year, code)
        with Session() as s:
            r = s.get(url)
            df = read_json(r.text, dtype={"geofips":object})
        return df
    def mapData(self):
        county = "https://bea.data.socrata.com/resource/ysef-iiz7.json?$select=geoid10,namelsad10&$limit=100000"
        state = "https://bea.data.socrata.com/resource/daik-biuk.json?$select=fips_5,state_name&$limit=1000000"
        msa = "https://bea.data.socrata.com/resource/xfhd-asq8.json?$select=cbsafp,cbsa_title&$limit=100000"
        dfs = []
        with Session() as s:
            r = s.get(county)
            d_c = read_json(r.text, dtype={"geoid10":object})
            d_c.columns = ["geofips","name"]
            dfs.append(d_c)

            r = s.get(state)
            d_s = read_json(r.text, dtype={"fips_5":object})
            d_s.columns = ["geofips","name"]
            dfs.append(d_s)

            r = s.get(msa)
            d_m = read_json(r.text, dtype={"cbsafp":object})
            d_m.columns = ["name","geofips"]
            dfs.append(d_m)
        data = concat(dfs)
        return data
    def contents(self):
        url = "https://bea.data.socrata.com/resource/cwy3-bgru.json"
        with Session() as s:
            r = s.get(url)
            df = read_json(r.text)
        return df
