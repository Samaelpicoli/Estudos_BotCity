$exclude = @("venv", "ExcelPlugin.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "ExcelPlugin.zip" -Force