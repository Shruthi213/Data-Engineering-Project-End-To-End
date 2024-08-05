# Databricks notebook source
configs = {"fs.azure.account.auth.type": "OAuth",
"fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
"fs.azure.account.oauth2.client.id": "",
"fs.azure.account.oauth2.client.secret": '',
"fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com//oauth2/token"}


dbutils.fs.mount(
source = "abfss://bronze@salesdataengineering123.dfs.core.windows.net", # contrainer@storageacc
mount_point = "/mnt/bronze",
extra_configs = configs)

# COMMAND ----------

# MAGIC %fs
# MAGIC ls "/mnt/bronze/SalesLT/"

# COMMAND ----------

configs = {"fs.azure.account.auth.type": "OAuth",
"fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
"fs.azure.account.oauth2.client.id": "5a8b4ade-9001-4498-b23c-07a67028e07d",
"fs.azure.account.oauth2.client.secret": 'Vgx8Q~qK7rzxXvDLP2Qrl9g2CW4dAUD_LESnAcvS',
"fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/9817344c-1e08-49c9-9c75-f16dee9c8a35/oauth2/token"}


dbutils.fs.mount(
source = "abfss://silver@salesdataengineering123.dfs.core.windows.net", # contrainer@storageacc
mount_point = "/mnt/silver",
extra_configs = configs)

# COMMAND ----------

configs = {"fs.azure.account.auth.type": "OAuth",
"fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
"fs.azure.account.oauth2.client.id": "5a8b4ade-9001-4498-b23c-07a67028e07d",
"fs.azure.account.oauth2.client.secret": 'Vgx8Q~qK7rzxXvDLP2Qrl9g2CW4dAUD_LESnAcvS',
"fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/9817344c-1e08-49c9-9c75-f16dee9c8a35/oauth2/token"}


dbutils.fs.mount(
source = "abfss://gold@salesdataengineering123.dfs.core.windows.net", # contrainer@storageacc
mount_point = "/mnt/gold",
extra_configs = configs)

# COMMAND ----------


