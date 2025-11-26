/*
 * Input variables for the Terraform configuration.  These allow you to
 * parameterize your deployment for different environments.  Populate
 * defaults as appropriate or use a `terraform.tfvars` file.
 */

variable "project_id" {
  description = "Google Cloud project ID"
  type        = string
}

variable "region" {
  description = "Google Cloud region for deployment"
  type        = string
  default     = "us-central1"
}

variable "backend_image" {
  description = "Container image for the backend service"
  type        = string
}

variable "vertex_model" {
  description = "Name of the Vertex AI model used for code generation"
  type        = string
}

variable "datadog_api_key" {
  description = "API key for Datadog"
  type        = string
}