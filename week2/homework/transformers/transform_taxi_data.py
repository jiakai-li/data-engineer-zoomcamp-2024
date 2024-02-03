import re
import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


def clean_data(data):
    print(f"Before processing: {data.shape[0]}")
    cleaned_data= data.loc[
        (data['passenger_count'] > 0) &
        (data['trip_distance'] > 0)
    ]
    print(f"After processing: {cleaned_data.shape[0]}")
    print(cleaned_data.shape)

    return cleaned_data

def add_date_cols(data):
    data['lpep_dropoff_date'] = data['lpep_dropoff_datetime'].dt.date
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date

    return data

def clean_col_names(data):
    data.columns = data.columns.str.replace(' ', '_')
    data.rename(columns={
        'VendorID': 'vendor_id',
        'RatecodeID': 'rate_code_id',
        'PULocationID': 'pu_location_id',
        'DOLocationID': 'do_location_id'
    }, inplace=True)

    return data


@transformer
def transform(data, *args, **kwargs):
    data = clean_data(data)
    data = add_date_cols(data)
    data = clean_col_names(data)
    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'

@test
def test_passenger_count(output, *args) -> None:
    assert output['passenger_count'].isin([0]).sum() == 0, "There are rides with 0 passenger"
