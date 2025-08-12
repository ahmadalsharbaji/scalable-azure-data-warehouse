IF NOT EXISTS (SELECT * FROM sys.external_file_formats WHERE name = 'SynapseDelimitedTextFormat') 
	CREATE EXTERNAL FILE FORMAT [SynapseDelimitedTextFormat] 
	WITH ( FORMAT_TYPE = DELIMITEDTEXT ,
	       FORMAT_OPTIONS (
			 FIELD_TERMINATOR = ',',
			 FIRST_ROW = 1,
			 USE_TYPE_DEFAULT = FALSE
			))
GO

IF NOT EXISTS (SELECT * FROM sys.external_data_sources WHERE name = 'analyticsfilesystem_synapse0101_dfs_core_windows_net') 
	CREATE EXTERNAL DATA SOURCE [analyticsfilesystem_synapse0101_dfs_core_windows_net] 
	WITH (
		LOCATION = 'abfss://analyticsfilesystem@synapse0101.dfs.core.windows.net', 
		TYPE = HADOOP 
	)
GO

CREATE EXTERNAL TABLE dbo.rider (
	rider_id int,
	first_name varchar(50),
	last_name varchar(50),
	address varchar(50),
	birthdate varchar(50),
	account_start varchar(50),
	account_end varchar(50),
	is_member bit
	)
	WITH (
	LOCATION = 'public.rider.csv',
	DATA_SOURCE = [analyticsfilesystem_synapse0101_dfs_core_windows_net],
	FILE_FORMAT = [SynapseDelimitedTextFormat]
	)
GO


SELECT TOP 100 * FROM dbo.rider
GO