[CmdletBinding()]
param(
    [Parameter(Position = 0)]
    [string]$Target,
    [switch]$Update,
    [switch]$Force,
    [switch]$DryRun
)

$ErrorActionPreference = 'Stop'

if ($Force -and -not $Update) {
    throw '-Force requires -Update.'
}

$pythonCommand = if ($env:PYTHON) {
    Get-Command -Name $env:PYTHON -ErrorAction Stop
} else {
    Get-Command -Name 'python' -ErrorAction SilentlyContinue
}

if (-not $pythonCommand) {
    $pythonCommand = Get-Command -Name 'py' -ErrorAction SilentlyContinue
}
if (-not $pythonCommand) {
    throw 'Python 3 is required to validate and install this Skill suite.'
}

$installer = Join-Path $PSScriptRoot 'scripts\install_suite.py'
$arguments = @()
if ($pythonCommand.Name -eq 'py.exe' -or $pythonCommand.Name -eq 'py') {
    $arguments += '-3'
}
$arguments += '-B'
$arguments += $installer
if ($Target) { $arguments += $Target }
if ($Update) { $arguments += '--update' }
if ($Force) { $arguments += '--force' }
if ($DryRun) { $arguments += '--dry-run' }

& $pythonCommand.Source @arguments
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}
