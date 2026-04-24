#!/bin/bash

set -e

echo "Running on start script..."

# Intall pre-commit hooks
if [ -f ".pre-commit-config.yaml" ]; then
    echo "Installing pre-commit hooks..."
    uv run pre-commit install
else
    echo "No .pre-commit-config.yaml found, skipping pre-commit hook installation."
fi

echo "On start script completed."
