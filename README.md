
$ErrorActionPreference = "Stop"

# 1. Set repository location
$repo = "C:\Users\waqar\OneDrive\Desktop\fatima-github"
Set-Location $repo

# 2. Read the corrected README from clipboard
$content = Get-Clipboard -Raw

# 3. Validate README content
if ($content -notmatch '^# Numerical Artifacts') {
    throw "Clipboard does not contain the expected README. Copy the corrected README first."
}

if ($content -notmatch '## Reproducibility and Limitations') {
    throw "The copied README appears incomplete."
}

# 4. Create backup folder
$backupFolder = "C:\Users\waqar\OneDrive\Desktop\Fatima-Research-Archive"

New-Item -ItemType Directory -Force -Path $backupFolder | Out-Null

# 5. Back up existing README
$backup = Join-Path $backupFolder (
    "README-backup-" +
    (Get-Date -Format "yyyyMMdd-HHmmss") +
    ".md"
)

Copy-Item ".\README.md" $backup

Write-Host "Existing README backed up." -ForegroundColor Green

# 6. Save corrected README using UTF-8
$readmePath = Join-Path $repo "README.md"

[System.IO.File]::WriteAllText(
    $readmePath,
    $content.TrimEnd() + "`n",
    (New-Object System.Text.UTF8Encoding($false))
)

Write-Host "`nREADME successfully replaced!" -ForegroundColor Green

# 7. Preview updated README
Write-Host "`n=== README PREVIEW ===" -ForegroundColor Cyan
Get-Content ".\README.md" -TotalCount 20

# 8. Review Git changes
Write-Host "`n=== GIT CHANGES ===" -ForegroundColor Cyan
git --no-pager diff --stat -- README.md

# 9. Verify README formatting
Write-Host "`n=== FORMATTING CHECK ===" -ForegroundColor Cyan
git --no-pager diff --check -- README.md

if ($LASTEXITCODE -ne 0) {
    Write-Warning "Formatting problems detected. Review before publishing."
} else {
    Write-Host "README formatting check passed!" -ForegroundColor Green
}

Write-Host "`nBackup location: $backup" -ForegroundColor Cyan
Write-Host "README update completed!" -ForegroundColor Green
