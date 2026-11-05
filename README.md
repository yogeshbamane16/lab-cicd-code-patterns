# Building CI/CD Pipelines - Final Project

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python 3.9](https://img.shields.io/badge/Python-3.9-green.svg)](https://shields.io/)

This repository contains the CI/CD pipeline implementation for the Coursera course **Building CI/CD Pipelines** (IBM-CD0215EN-SkillsNetwork Introduction to CI/CD).

## Project Overview
This project automates Continuous Integration (CI) and Continuous Delivery (CD) for a Python/Flask microservice:
- **Continuous Integration (CI):** Implemented using GitHub Actions (`.github/workflows/workflow.yml`) to automatically checkout code, install dependencies, lint with `flake8`, and execute unit tests with `nosetests`.
- **Continuous Delivery (CD):** Implemented using Tekton Pipelines on OpenShift (`.tekton/pipeline.yaml`, `.tekton/tasks.yaml`, `.tekton/pvc.yaml`) to clean up workspaces, clone repositories, run linting, execute automated tests, build container images with `buildah`, and deploy to OpenShift using `openshift-client`.

## Contents
- `.github/workflows/workflow.yml`: GitHub Actions automated CI workflow.
- `.tekton/tasks.yaml`: Tekton tasks (`cleanup`, `git-clone`, `flake8`, `nose`, `buildah`, `openshift-client`).
- `.tekton/pipeline.yaml`: Tekton CD pipeline chaining all workflow tasks.
- `.tekton/pvc.yaml`: PersistentVolumeClaim definition for Tekton workspace.
- `deploy/deployment.yaml`: OpenShift deployment, service, and route manifests.

## Instructor
John Rofrano, Senior Technical Staff Member, DevOps Champion, @ IBM Research

---
© IBM Corporation 2026. All rights reserved.
