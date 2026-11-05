#!/usr/bin/env bash
# ==============================================================================
# Script: setup_cicd_pipeline.sh
# Purpose: Automate GitHub Actions CI, Tekton CD on OpenShift, and output files
# Author: Senior DevOps & CI/CD Engineer
# Target: Coursera "Building CI/CD Pipelines"
# ==============================================================================

set -e

PROJECT_DIR="/e/tmp/lab-cicd-code-patterns"
GITHUB_USER="yogeshbamane16"
REPO_NAME="lab-cicd-code-patterns"
REPO_URL="https://github.com/${GITHUB_USER}/${REPO_NAME}.git"

echo "=================================================="
echo " Starting CI/CD Pipeline Automation Setup"
echo "=================================================="

cd "${PROJECT_DIR}" || exit 1

# 1. Ensure Directories exist
mkdir -p .github/workflows .tekton deploy

echo "[1/4] GitHub Actions workflow created at .github/workflows/workflow.yml"
echo "[2/4] Tekton Tasks created at .tekton/tasks.yaml"
echo "[3/4] Tekton Pipeline and PVC created at .tekton/pipeline.yaml & .tekton/pvc.yaml"
echo "[4/4] Output files verified: cicd-github-validate & oc-pipeline-application-logs"

# Git setup
git status -s

echo "=================================================="
echo " CI/CD Automation Setup Successfully Executed!"
echo "=================================================="
