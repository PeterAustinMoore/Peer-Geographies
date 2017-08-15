# BEAComparators
## About
This is a simple python script for extracting, transforming, and analyzing BEA data
in order to compare various geographies by various measures with the output being
a collection of similar geographies.

The purpose is to provide autosuggest functionality based upon similar geographies
as an addition to regional information.

## Algorithm
To determine similar geographies, this script relies on [sklearn library's k-nearest-neighbor](http://scikit-learn.org/stable/modules/neighbors.html).

This is done for two reasons:
1. There is a requirement for a minimum number of similar geographies (in this case 6) which
K-Means and other clustering algorithms cannot generally provide.
2. It is fairly well understood and replicable.

I found [this post by kevinzakka](https://kevinzakka.github.io/2016/07/13/k-nearest-neighbor/)
particularly useful for some more information on K-Nearest-Neighbor (KNN).

*Note* This application of KNN is not perfect. You will notice at no point
is there a training or test dataset created and there are no goodness of fit tests.
The primary reason for this is that I am intentionally overfitting this data and
have no intention of making predictions or further classifications on incoming data. Also,
by analyzing each measure independently, normalization issues can be avoided.  

Further, this analysis is a point in time. I really enjoyed [this presentation](https://forecasters.org/wp-content/uploads/gravity_forms/7-2a51b93047891f1ec3608bdbd77ca58d/2013/07/2013-ISF-KNN-for-Time-Series-Data.pdf) of KNN for time series (though for regression and some of the slides are messed up). It may be interesting in the future to do this analysis over a period of time instead.


## Requirements
Requirements can be installed using standard
```Shell
pip install -r requirements.txt
```

This is written in python 3.6, but also runs in 2.7

## Structure
Running the comparator can be run as:
```bash
python Comparator.py
```

An output CSV is created in the [output directory](/output) with a schema of:

| Field | Description |
| ----- | ----------- |
| Rank  | The ranking of nearest neighbor based on distance |
| comparator | The geofips code matching the rank |
| comparator_name | The comparators geographical name |
| index | The geofips code of the geography being compared |
| index_name | The name of the index geography |
| code | The measure being compared e.g. GDP_SAN is State GDP in current dollars |
| geo | The geographic scope of the row (MSA, State, or County) |
