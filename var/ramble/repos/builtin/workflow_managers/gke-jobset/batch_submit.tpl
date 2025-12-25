#!/bin/bash
set -e
cd "{experiment_run_dir}"
printf "Submitting {experiment_name} via JobSet...\n"

# Apply the generated JobSet
kubectl apply -f jobset.yaml

# Create a log file so Ramble knows something happened
echo "Submitted {experiment_name} at $(date)" > {log_file}
