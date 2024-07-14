# Building Data Pipeline on Reddit data using Airflow and AWS services
This project offers a robust and automated solution for processing and analyzing Reddit data. It leverages the power of AWS cloud-based services to ensure scalability, efficiency, and user-friendly access to valuable insights

### Architecture

![Architecture](project_overview.png)

## Technology Used
- Programming Language - Python
- Reddit dataengineering blog data

AWS services
1. S3 bucket
2. Glue job and Crawler
4. Athena
5. Redshift


## Overview
website: https://www.reddit.com/r/dataengineering/

 
1. **Reddit API**: Source of the data.
2. **Apache Airflow**: Orchestrates the ETL process and manages task distribution.
3. **PostgreSQL**: Temporary storage and metadata management.
4. **Amazon S3**: Raw data storage.
5. **AWS Glue**: Data cataloging and ETL jobs.
6. **Amazon Athena**: SQL-based data transformation.
7. **Amazon Redshift**: Data warehousing and analytics.

## Prerequisites
- AWS Account with appropriate permissions for S3, Glue, Athena, and Redshift.
- Reddit API credentials.
- Docker Installation
- Python 3.9 or higher
