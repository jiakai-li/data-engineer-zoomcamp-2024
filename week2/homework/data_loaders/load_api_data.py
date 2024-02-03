import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    dates = ['2020-10', '2020-11', '2020-12']

    schema = {
        'VendorID': pd.Int64Dtype(),
        'passenger_count': pd.Int64Dtype(),
        'trip_distance': float,
        'RatecodeID': pd.Int64Dtype(),
        'store_and_fwd_flag': str,
        'PULocationID': pd.Int64Dtype(),
        'DOLocationID': pd.Int64Dtype(),
        'payment_type': pd.Int64Dtype(),
        'fare_amount': float,
        'extra': float,
        'mta_tax': float,
        'tip_amount': float,
        'tolls_amount': float,
        'improvement_surcharge': float,
        'total_amount': float,
        'congestion_surcharge': float
    }

    datetime_cols = [
        'lpep_pickup_datetime',
        'lpep_dropoff_datetime'
    ]

    dfs = []
    for dt in dates:
        url = url = f"{kwargs['taxi_data_url']}/{kwargs['taxi_data_file']}_{dt}.csv.gz"
        dfs.append(pd.read_csv(url, sep=',', dtype=schema, parse_dates=datetime_cols))

    return pd.concat(dfs, ignore_index=True)


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
