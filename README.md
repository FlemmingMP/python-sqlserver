### Python SQL Server test access

The server settings are for a local SQL Server. They are the same as in the main Go project. If you have no server there is a basic docker compose included.

To run it locally you need a ODBC driver (https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver16).

The dockerfile is made to use all of the same dependencies that I used locally to make it work only using Debian 11 instead of MacOS.
