# Week 2 Homework: Green Taxi ETL Pipeline

## Assignment Overview

The goal of this assignment is to construct an ETL pipeline for the green taxi dataset, performing loading, transformations, and exporting to a database and Google Cloud.

### Steps

1. **Create a new pipeline:**
    - Name: `green_taxi_etl`

2. **Data Loading:**
    - Add a data loader block using Pandas to read data for the final quarter of 2020 (months 10, 11, 12).
    - Use the same datatypes and date parsing methods from the course.
    - BONUS: Load the final three months using a for loop and `pd.concat`.

3. **Data Transformation:**
    - Add a transformer block and perform the following:
        - Remove rows where passenger count is 0 or trip distance is 0.
        - Create a new column `lpep_pickup_date` by converting `lpep_pickup_datetime` to a date.
        - Rename columns in Camel Case to Snake Case (e.g., VendorID to vendor_id).
        - Add three assertions:
            - `vendor_id` is one of the existing values in the column.
            - `passenger_count` is greater than 0.
            - `trip_distance` is greater than 0.

4. **Data Exporting:**
    - Use a Postgres data exporter (SQL or Python) to write the dataset to a table called `green_taxi` in a schema `mage`. Replace the table if it already exists.
    - Write data as Parquet files to a bucket in GCP, partitioned by `lpep_pickup_date`. Use the `pyarrow` library.

5. **Schedule the Pipeline:**
    - Schedule your pipeline to run daily at 5 AM UTC.

## Questions

### Question 1: Data Loading
- Once the dataset is loaded, what's the shape of the data?
    - [ ] 266,855 rows x 20 columns
    - [ ] 544,898 rows x 18 columns
    - [ ] 544,898 rows x 20 columns
    - [ ] 133,744 rows x 20 columns

### Question 2: Data Transformation
- Upon filtering the dataset, how many rows are left?
    - [ ] 544,897 rows
    - [ ] 266,855 rows
    - [ ] 139,370 rows
    - [ ] 266,856 rows

### Question 3: Data Transformation
- Which code creates a new column `lpep_pickup_date` by converting `lpep_pickup_datetime` to a date?
    - [ ] `data = data['lpep_pickup_datetime'].date`
    - [ ] `data('lpep_pickup_date') = data['lpep_pickup_datetime'].date`
    - [ ] `data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date`
    - [ ] `data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt().date()`

### Question 4: Data Transformation
- What are the existing values of VendorID in the dataset?
    - [ ] 1, 2, or 3
    - [ ] 1 or 2
    - [ ] 1, 2, 3, 4
    - [ ] 1

### Question 5: Data Transformation
- How many columns need to be renamed to snake case?
    - [ ] 3
    - [ ] 6
    - [ ] 2
    - [ ] 4

### Question 6: Data Exporting
- Once exported, how many partitions (folders) are present in Google Cloud?
    - [ ] 96
    - [ ] 56
    - [ ] 67
    - [ ] 108
