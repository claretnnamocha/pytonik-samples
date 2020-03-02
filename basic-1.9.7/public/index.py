#!C:\Python36\python.exe
try:

  from pytonik import Web

except Exception as err:

  exit(err)


App = Web.App()

App.runs()
