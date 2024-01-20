terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.6.0"
    }
  }
}

provider "google" {
  credentials = file(var.gcp_credential_file)
  project     = var.project
  region      = var.region
}

resource "google_storage_bucket" "de-zoomcamp-demo-bucket" {
  name          = var.gcs_bucket_name
  force_destroy = true
  storage_class = "REGIONAL"
  location      = var.region

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}

resource "google_bigquery_dataset" "de-zoomcamp-demo-dataset" {
  dataset_id = var.bq_dataset_name
  location   = var.region
}