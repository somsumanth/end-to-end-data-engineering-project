# End-to-End Data Engineering Architecture

## Business Problem

Customer transaction data arrives daily as CSV files.
The goal is to ingest, validate, transform and store the data for analytics.

## Architecture Flow

Source Files (CSV)
        |
        v
Azure Data Factory
        |
        v
Azure Data Lake Storage
        |
        v
Azure Databricks (PySpark)
        |
        v
Bronze Layer (Raw Data)
        |
        v
Silver Layer (Cleaned Data)
        |
        v
Gold Layer (Business Aggregations)
        |
        v
Delta Lake Tables
        |
        v
Analytics & Reporting

## Components

### Azure Data Factory
- Ingest source files
- Trigger Databricks notebooks
- Monitor pipeline execution

### Azure Databricks
- Execute PySpark transformations
- Apply business rules
- Perform data quality checks

### Delta Lake
- ACID transactions
- Incremental processing
- Merge operations

### Medallion Architecture

Bronze -> Raw data

Silver -> Cleaned and validated data

Gold -> Business-ready datasets
