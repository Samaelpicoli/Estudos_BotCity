$exclude = @("venv", "GoogleFormulario.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "GoogleFormulario.zip" -Force