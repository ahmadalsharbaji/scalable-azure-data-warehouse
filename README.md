# Scalable Azure Data Warehouse

## Overview

This repository provides an end-to-end solution for building a scalable data warehouse on Microsoft Azure. It encompasses data ingestion, transformation, and storage, utilizing Azure Synapse Analytics for data processing, and PostgreSQL for storing ingested data. The solution includes Python-based orchestration for seamless data movement.

## Architecture

The system is designed to handle large datasets through a scalable architecture, ensuring efficient data processing and storage. The workflow involves ingesting data into PostgreSQL, performing data transformations, and storing processed data into Azure Synapse Analytics for analytics and reporting.

## Directory Structure

- `data`: Contains raw data files for ingestion.
- `data_ingestion`: Scripts for ingesting data into PostgreSQL and Azure Synapse Analytics.
- `external_tables_scripts`: SQL scripts for creating external tables in Synapse.
- `star_schema_scripts`: SQL scripts for defining the star schema in the data warehouse (dact and dimention tables).
- `requirements.txt`: Lists Python dependencies for the project.

## Prerequisites

- An active Azure subscription.
- Azure Synapse Analytics workspace.
- PostgreSQL instance for data storage.
- Python 3.8 or higher.
- Necessary Python libraries as specified in `requirements.txt`.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/ahmadalsharbaji/scalable-azure-data-warehouse.git
2. Navigate to the project directory:
   cd scalable-azure-data-warehouse
3. Install required Python libraries:
   pip install -r requirements.txt
4. Configure PostgreSQL connection in data_ingestion scripts.
5. Run the data ingestion scripts to load data into PostgreSQL.
6. Execute SQL scripts in Azure Synapse Analytics for schema setup.
7. PostgreSQL Integration
Data is ingested into PostgreSQL for storage and transformation before being moved to Azure Synapse Analytics for processing.

##
Thank you for checking out this project. Feel free to contribute or reach out for any questions!
