$exclude = @("venv", "ProjetoWeb.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "ProjetoWeb.zip" -Force