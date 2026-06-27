# Epic Agent Fabric — Windows PowerShell Setup
# Run this in PowerShell (not Command Prompt)

Write-Host "🚀 Epic Agent Fabric — Windows Setup" -ForegroundColor Cyan
Write-Host "=====================================" -ForegroundColor Cyan

# Check if Docker is installed
if (-not (Get-Command docker -ErrorAction SilentlyContinue)) {
    Write-Host "❌ Docker is not installed or not in PATH." -ForegroundColor Red
    Write-Host "Please install Docker Desktop from: https://www.docker.com/products/docker-desktop" -ForegroundColor Yellow
    exit 1
}

# Create volume directories
$volumes = @("volume\executor", "volume\voice", "volume\media", "volume\models")
foreach ($v in $volumes) {
    New-Item -ItemType Directory -Force -Path $v | Out-Null
}
Write-Host "✓ Volume directories created" -ForegroundColor Green

# Check for .env
if (-not (Test-Path .env)) {
    Write-Host "⚠️  No .env file found. Creating from .env.example..." -ForegroundColor Yellow
    if (Test-Path .env.example) {
        Copy-Item .env.example .env
    } else {
        @"
STRIPE_API_KEY=
GROQ_API_KEY=
OPENAI_API_KEY=
ZAPIER_API_KEY=
"@ | Out-File -FilePath .env -Encoding utf8
    }
}

# Pull and build images
Write-Host "📦 Pulling and building containers (this may take a few minutes)..." -ForegroundColor Cyan
docker compose pull
docker compose build --parallel

# Start core services
Write-Host "🔄 Starting core services..." -ForegroundColor Cyan
docker compose up -d executor-gateway tokenos redis

Write-Host ""
Write-Host "✅ Epic Agent Fabric is now running!" -ForegroundColor Green
Write-Host ""
Write-Host "Services:" -ForegroundColor White
Write-Host "  • Executor Gateway:  http://localhost:8787" -ForegroundColor Gray
Write-Host "  • TokenOS:           http://localhost:7777" -ForegroundColor Gray
Write-Host "  • Redis:             localhost:6379" -ForegroundColor Gray
Write-Host ""
Write-Host "Next steps:" -ForegroundColor White
Write-Host "  1. Add your API keys to .env" -ForegroundColor Gray
Write-Host "  2. Run: docker compose up -d" -ForegroundColor Gray
Write-Host "  3. Open the landing page or visit the services above" -ForegroundColor Gray
Write-Host ""
Write-Host "Full stack (Media + Intelligence):" -ForegroundColor White
Write-Host "  docker compose --profile full up -d" -ForegroundColor Gray
Write-Host ""
Write-Host "Happy building. Local. Owned. Token-native." -ForegroundColor Cyan
