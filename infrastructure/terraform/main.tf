/*
 * Terraform configuration for provisioning the cloud resources required by the
 * Self‑Debugging Coding Assistant.  The exact resources will depend on your
 * implementation choices.  Suggested resources include:
 *
 *  - A Cloud Run or Cloud Functions service to host the backend API.
 *  - A Cloud Storage bucket (optional) for storing artefacts or logs.
 *  - Service accounts with minimal permissions for Vertex AI and Datadog
 *    integration.
 *  - IAM bindings granting the service accounts access to the Vertex API,
 *    Code Execution sandbox (if using Agent Engine), and Datadog metrics API.
 *  - Optional networking configuration (VPC connectors) if your services
 *    require access to private resources.
 *
 * Replace the stub contents below with real Terraform resources.  Use
 * variables defined in `variables.tf` and output them via `outputs.tf`.
 */

terraform {
  required_version = ">= 1.5.0"
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = ">= 5.0"
    }
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
}

/* Example resource definition (commented out)

resource "google_cloud_run_service" "backend" {
  name     = "self-debug-backend"
  location = var.region
  template {
    spec {
      containers {
        image = var.backend_image
        env = [
          {
            name  = "VERTEX_MODEL"
            value = var.vertex_model
          },
          {
            name  = "DATADOG_API_KEY"
            value = var.datadog_api_key
          }
        ]
      }
    }
  }
  traffics {
    percent         = 100
    latest_revision = true
  }
}

*/