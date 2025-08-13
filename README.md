# Scalable Azure Data Warehouse

## Overview

This repository provides a solution for building a scalable data warehouse on Microsoft Azure. The solution is designed to handle and process data for a transportation business. It ingests raw data from various sources such as payment transactions, rider information, stations, and trip details into PostgreSQL. The system is designed to transform and store this data in a structured format, enabling analytics and reporting in Azure Synapse Analytics.

### Business Case

The data stored and processed includes:

- **payments.csv**: Records of payment transactions made by riders for their trips.
- **riders.csv**: Information about riders, including their details and account statuses.
- **stations.csv**: Data about transportation stations, including locations and other station-related information.
- **trips.csv**: Trip details including the start and end points, distance, and duration of the rides.

The goal is to create a robust, scalable data architecture that supports business operations by enabling efficient reporting, analytics, and insights into rider behavior, station performance, and payment trends.

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
