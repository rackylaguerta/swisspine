# Flask API

This is a simple Flask API that provides endpoints for various functionalities.

## Endpoints

### 1. Mirror Word

**Endpoint**: `/api/mirror`

**Method**: GET

**Parameters**:
- `word` (string): The word to mirror.

**Description**:
Returns a JSON object with the mirrored version of the provided word. The mirrored version is obtained by reversing the word and swapping the case of each character.

### 2. Health Check

**Endpoint**: `/api/health`

**Method**: GET

**Description**:
Returns a JSON object indicating the status of the application. Always returns `{'status': 'ok'}` as long as the application is running.

### 3. Upload Random Numbers

**Endpoint**: `/api/upload-random`

**Method**: POST

**Description**:
Generates 100 random numbers between 1 and 1000, saves them to a file named `random_numbers.txt`, and uploads the file to an Azure Blob Storage container named `my-container`.

---

# Setup

# azure-pipelines.yml
# DevOps Engineering Test Pipeline

This Azure DevOps pipeline consists of two jobs: one for running unit tests and another for building and pushing Docker images.

## Pipeline Structure

### 1. Run Unit Tests

- **Job Name**: unittest
- **Display Name**: Run unittest
- **Description**: This job runs unit tests for the Flask application to ensure its functionality.
- **Steps**:
  - Checkout the source code from the repository.
  - Use Python version 3.9.19 and install dependencies specified in requirements.txt.
  - Execute pytest to run the unit tests located in unittest/test.py.

### 2. Build and Push Docker Image

- **Job Name**: build_and_push
- **Display Name**: Build and Push
- **Description**: This job builds a Docker image for the Flask application and pushes it to a Docker registry when changes are pushed to the master branch.
- **Dependencies**: Depends on the completion of the unittest job.
- **Condition**: Executes only when changes are pushed to the master branch.
- **Steps**:
  - Checkout the source code from the repository.
  - Create an image tag based on the source version.
  - Use Docker to build and push the Docker image to the specified Docker registry.

## Running the Pipeline

To run this pipeline:
1. Ensure that you have configured the required environment variables and permissions in your Azure DevOps project.
2. Push changes to your repository. This will trigger the pipeline to run automatically.
3. The pipeline will execute the defined jobs sequentially. First, it will run unit tests to validate the application's functionality. Then, if changes are pushed to the master branch, it will proceed to build and push the Docker image to the specified Docker registry.

---

# helm.yaml
# Helm Chart Deployment Pipeline for AKS

This Azure DevOps pipeline is designed to deploy a Helm chart to an Azure Kubernetes Service (AKS) cluster.

## Pipeline Structure

### 1. Deploy Helm Chart

- **Description**: This job logs in to Azure CLI using service principal credentials, sets the correct Azure subscription, packages the Helm chart located in the specified directory, and deploys it to the AKS cluster.
- **Steps**:
  - Checkout the source code from the repository.
  - Log in to Azure CLI using service principal credentials.
  - Set the correct Azure subscription.
  - Change directory to the Helm chart directory.
  - Package the Helm chart.
  - Deploy the Helm chart to the AKS cluster.

## Running the Pipeline

To run this pipeline:
1. Ensure that you have configured the required environment variables and permissions in your Azure DevOps project.
2. Push changes to your repository. Since the pipeline trigger is set to `none`, you need to manually trigger the pipeline from the Azure DevOps dashboard.
3. The pipeline will execute the defined job, which deploys the Helm chart to the AKS cluster.

---

# terraform.yaml
# Terraform Pipeline for Azure Resource Deployment

This Azure DevOps pipeline is designed to use Terraform to deploy Azure resources. The pipeline initializes Terraform, plans the infrastructure changes, and applies those changes.

## Pipeline Structure

### 1. Terraform Init and Apply

- **Description**: This job initializes Terraform, plans the infrastructure changes using the provided variables file, and applies those changes.
- **Steps**:
  - Checkout the source code from the repository.
  - Change directory to the Terraform folder.
  - Initialize Terraform to prepare the working directory for other commands.
  - Create an execution plan and save it to a plan file.
  - Apply the changes described in the execution plan to reach the desired state of the infrastructure.

## Running the Pipeline

To run this pipeline:
1. Ensure that you have configured the required environment variables and permissions in your Azure DevOps project.
2. Push changes to your repository. Since the pipeline trigger is set to `none`, you need to manually trigger the pipeline from the Azure DevOps dashboard.
3. The pipeline will execute the defined job, which initializes Terraform and applies the infrastructure changes.






