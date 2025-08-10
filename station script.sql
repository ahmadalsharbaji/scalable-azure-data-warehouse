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

CREATE EXTERNAL TABLE dbo.station (
	station_id varchar(50),
	station_name varchar(100),
	latitude float,
	longitude float
	)
	WITH (
	LOCATION = 'public.station.csv',
	DATA_SOURCE = [analyticsfilesystem_synapse0101_dfs_core_windows_net],
	FILE_FORMAT = [SynapseDelimitedTextFormat]
	)
GO


SELECT TOP 100 * FROM dbo.station
GO
