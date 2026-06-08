# End-to-End Data Engineering Project

## Overview

This project demonstrates an end-to-end data engineering pipeline using Azure Data Factory, Azure Data Lake Storage, Azure Databricks, PySpark and Delta Lake.

The pipeline ingests customer transaction data, performs transformations using Medallion Architecture and stores curated datasets for analytics.

## Data Flow

Customer CSV Files
        ↓
Azure Data Factory
        ↓
Azure Data Lake Storage
        ↓
Azure Databricks (PySpark)
        ↓
Bronze Layer
        ↓
Silver Layer
        ↓
Gold Layer
        ↓
Business Reporting

## Project Components

- Azure Data Factory for orchestration
- Azure Data Lake Storage for raw data storage
- Azure Databricks for data processing
- PySpark transformations
- Delta Lake storage format
- Bronze, Silver and Gold architecture
- Incremental loading
- Data quality validation

## Files Included

### architecture.md
Overall architecture and data flow design.

### bronze_layer.py
Loads raw source data into Bronze layer.

### silver_layer.py
Performs data cleansing and transformations.

### gold_layer.py
Creates business-ready datasets.

### incremental_load.py
Implements incremental data loading.

### data_quality_checks.py
Validates data quality and detects null or duplicate records.

## Technologies Used

- Azure Data Factory
- Azure Data Lake Storage
- Azure Databricks
- PySpark
- Delta Lake
- SQL

## Key Concepts Demonstrated

- Medallion Architecture
- Incremental Loading
- Data Validation
- ETL Pipeline Design
- Data Lake Architecture
- Distributed Data Processing
