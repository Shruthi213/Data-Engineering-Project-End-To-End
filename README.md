# Data-Engineering-Project-End-To-End
Azure Data Engineering project.
This project is migrating on-prem (MS SQL Server) Data tables to Cloud Utilizing Azure Data Factory , Databricks, Saving files in Azure data lake Bronze layer, Silver layer, Gold Layer .
Utilizing Azure Synapse Analytics for analysis and transformation and reporting purpose.
### Project Architecture:
![image](https://github.com/user-attachments/assets/2d5b977d-5a57-48da-ac86-b66f4a1c1b39)

# Getting SQL Server Firewall Error : 26 
Tried using On-Prem SQL database but getting  firewall connection issues So I have using Azure SQL database with Azure SQL i did not face any firewall issues.
# PreRequisites
Data Source: Azure SQL Database , Data Destination : Azure Data Lake Gen2:Containers Siler, Bronze , Gold.
AzureDatafactory,Databricks, Synapse Analytics, ServerlessSQL pool,PowerBI, Azure Portal
# Using AzureDataFactory Loaded Data Into Bronze container
Using ADF loaded data into data lake bronze container.
# Transformation Bronze to Silver
Transform1: In this all tables date column transformed
# Silver to Gold Using Data bricks
Transformation2: Transformed silver layer to gold layer data using databricks
# Azure Synapse Analytics
Created pipelines in azure synapse serverless SQL pool
Created view pipelines.Loaded cleanest form of data and create powerBI report
