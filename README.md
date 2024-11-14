# Data-Engineering-Project-End-To-End
This project demonstrates an end-to-end data engineering solution on Microsoft Azure, designed to handle the ingestion, transformation, and analysis of data from an on-premises SQL Server database to a comprehensive reporting platform in Power BI. The solution uses Azure Data Lake Storage Gen2, Azure Data Factory, Databricks, and Azure Synapse Analytics, with added security managed through Azure Key Vault.

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
