powershell -command "Get-Process | Sort-Object WorkingSet -Descending | Select-Object -First 5"
