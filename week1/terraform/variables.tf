variable "gcp_credential_file" {
  description = "GCP Key file path"
  default     = "/keys/gcp/gcp_key.json"
}

variable "project" {
  description = "Project"
  default     = "artful-sky-411117"
}

variable "region" {
  description = "Region"
  default     = "australia-southeast1"
}

variable "gcs_bucket_name" {
  description = "DEZoomcamp Storage Bucket Name"
  default     = "de_zoomcamp_bucket_jiakai"
}

variable "bq_dataset_name" {
  description = "DEZoomcamp BigQuery Dataset Name"
  default     = "de_zoomcamp_bigquery_dataset_jiakai"
}
