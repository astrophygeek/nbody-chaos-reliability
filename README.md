
$ErrorActionPreference = "Stop"

$repo = "C:\Users\waqar\OneDrive\Desktop\fatima-github"
Set-Location $repo

# Read the corrected README you copied from ChatGPT
$content = Get-Clipboard -Raw

# Safety checks
if ($content -notmatch '^# Numerical Artifacts') {
    throw "Clipboard does not contain the expected README."
}

if ($content -notmatch '## Reproducibility and Limitations') {
    throw "The copied README appears incomplete."
}

# Backup existing README outside the repository
$backupFolder = "C:\Users\waqar\OneDrive\Desktop\Fatima-Research-Archive"
New-Item -ItemType Directory -Force -Path $backupFolder | Out-Null

$backup = Join-Path $backupFolder (
    "README-backup-" + (Get-Date -Format "yyyyMMdd-HHmmss") + ".md"
)

Copy-Item ".\README.md" $backup

# Save clean UTF-8 Markdown
[System.IO.File]::WriteAllText(
    (Join-Path $repo "README.md"),
    $content.TrimEnd() + "`n",
    (New-Object System.Text.UTF8Encoding($false))
)

Write-Host "`nREADME successfully replaced!" -ForegroundColor Green

# Preview the beginning
Get-Content ".\README.md" -TotalCount 20

# Show changes without Git's interactive viewer
git --no-pager diff --stat -- README.md

Write-Host "`nBackup: $backup" -ForegroundColor Cyan
