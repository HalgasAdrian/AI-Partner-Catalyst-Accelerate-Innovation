/*
 * Outputs from the Terraform deployment.  These are useful for referencing
 * resources in other modules or for manual verification after apply.
 */

/* Example output (commented out)
output "backend_url" {
  description = "URL of the deployed backend service"
  value       = google_cloud_run_service.backend.status[0].url
}
*/