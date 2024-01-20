# Question 1

Which tag has the following text? - *Automatically remove the container when it exits*

**<u>--rm</u>**

```bash
docker run --help | grep '\-\-rm'
      --rm                             Automatically remove the container when it exits
```

# Question 2

- Run docker with the python:3.9 image in an interactive mode and the entry point of bash.

  ```bash
  # Run python3.9 in interactive mode
  docker run -it --rm python:3.9 bash
  # Image id edb6b76b75ba
  ```

- Now check the python modules that are installed ( use `pip list` ).

  ```bash
  pip list
  # Package    Version
  # ---------- -------
  # pip        23.0.1
  # setuptools 58.1.0
  # wheel      0.42.0   <<<<< wheel version 0.42.0
  ```

  What is version of the package *wheel* ? **<u>0.42.0</u>**

# Question 3

How many taxi trips were totally made on September 18th 2019?

```sql
SELECT
	COUNT(*)
FROM green_taxi_data
WHERE
	lpep_pickup_datetime >= '2019-09-18 00:00:00' AND
	lpep_pickup_datetime < '2019-09-19 00:00:00' AND
	lpep_dropoff_datetime >= '2019-09-18 00:00:00' AND
	lpep_dropoff_datetime < '2019-09-19 00:00:00'
```

**<u>15612</u>**

# Question 4

Which was the pick up day with the largest trip distance Use the pick up time for your calculations.

```sql
SELECT
	lpep_pickup_datetime
FROM green_taxi_data
WHERE trip_distance = (
	SELECT MAX(trip_distance) FROM green_taxi_data
)
```

**<u>2019-09-26</u>**

# Question 5

Consider `lpep_pickup_datetime` in 2019-09-18 and ignoring Borough has Unknown. Which were the 3 pick up Boroughs that had a sum of `total_amount` superior to 50000?

```sql
SELECT
	zones."Borough"
FROM green_taxi_data
JOIN zones ON zones."LocationID" = green_taxi_data."PULocationID"
WHERE
	zones."Borough" != 'Unknown' AND
	green_taxi_data.lpep_pickup_datetime >= '2019-09-18 00:00:00' AND
	green_taxi_data.lpep_pickup_datetime < '2019-09-19 00:00:00'
GROUP BY zones."Borough"
HAVING SUM(total_amount) > 50000
LIMIT 3
```

**<u>Brooklyn, Manhattan, Queens</u>**

# Question 6

For the passengers picked up in September 2019 in the zone name Astoria which was the drop off zone that had the largest tip? We want the name of the zone, not the id.

```sql
WITH astoria_trips AS (
	SELECT
		green_taxi_data.*,
		pickup_zones."Zone" AS pickup_zone_name,
		dropoff_zones."Zone" AS dropoff_zone_name
	FROM green_taxi_data
	JOIN zones pickup_zones ON pickup_zones."LocationID" = green_taxi_data."PULocationID"
	JOIN zones dropoff_zones ON dropoff_zones."LocationID" = green_taxi_data."DOLocationID"
	WHERE
		pickup_zones."Zone" = 'Astoria'
)
SELECT
	dropoff_zone_name
FROM astoria_trips
WHERE tip_amount = (
	SELECT MAX(tip_amount) FROM astoria_trips
)
```

**<u>JFK Airport</u>**

# Question 7

Output of `terraform apply`:

```bash
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # google_bigquery_dataset.de-zoomcamp-demo-dataset will be created
  + resource "google_bigquery_dataset" "de-zoomcamp-demo-dataset" {
      + creation_time              = (known after apply)
      + dataset_id                 = "de_zoomcamp_bigquery_dataset_jiakai"
      + default_collation          = (known after apply)
      + delete_contents_on_destroy = false
      + effective_labels           = (known after apply)
      + etag                       = (known after apply)
      + id                         = (known after apply)
      + is_case_insensitive        = (known after apply)
      + last_modified_time         = (known after apply)
      + location                   = "australia-southeast1"
      + max_time_travel_hours      = (known after apply)
      + project                    = "artful-sky-411***"
      + self_link                  = (known after apply)
      + storage_billing_model      = (known after apply)
      + terraform_labels           = (known after apply)
    }

  # google_storage_bucket.de-zoomcamp-demo-bucket will be created
  + resource "google_storage_bucket" "de-zoomcamp-demo-bucket" {
      + effective_labels            = (known after apply)
      + force_destroy               = true
      + id                          = (known after apply)
      + location                    = "AUSTRALIA-SOUTHEAST1"
      + name                        = "de_zoomcamp_bucket_jiakai"
      + project                     = (known after apply)
      + public_access_prevention    = (known after apply)
      + self_link                   = (known after apply)
      + storage_class               = "REGIONAL"
      + terraform_labels            = (known after apply)
      + uniform_bucket_level_access = (known after apply)
      + url                         = (known after apply)

      + lifecycle_rule {
          + action {
              + type = "AbortIncompleteMultipartUpload"
            }
          + condition {
              + age                   = 1
              + matches_prefix        = []
              + matches_storage_class = []
              + matches_suffix        = []
              + with_state            = (known after apply)
            }
        }
    }

Plan: 2 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

google_storage_bucket.de-zoomcamp-demo-bucket: Creating...
google_bigquery_dataset.de-zoomcamp-demo-dataset: Creating...
google_storage_bucket.de-zoomcamp-demo-bucket: Creation complete after 3s [id=de_zoomcamp_bucket_jiakai]
google_bigquery_dataset.de-zoomcamp-demo-dataset: Creation complete after 3s [id=projects/artful-sky-411***/datasets/de_zoomcamp_bigquery_dataset_jiakai]

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.
```

