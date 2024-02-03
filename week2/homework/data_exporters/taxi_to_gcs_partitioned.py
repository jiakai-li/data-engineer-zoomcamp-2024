from pandas import DataFrame
import pyarrow as pa
import pyarrow.parquet as pq
import os

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/src/gcp_key.json'

bucket_name = 'data-engineer-zoomcamp'
project_id = 'artful-sky-411117'
table_name = 'nyc_taxi_data_green'

root_path = f'{bucket_name}/{table_name}'


@data_exporter
def export_data_to_google_cloud_storage(df: DataFrame, **kwargs) -> None:
    table = pa.Table.from_pandas(df)
    gcs = pa.fs.GcsFileSystem()

    pq.write_to_dataset(
        table,
        root_path=root_path,
        partition_cols=['lpep_pickup_date'],
        filesystem=gcs
    )
