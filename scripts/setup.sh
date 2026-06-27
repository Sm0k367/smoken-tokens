# Epic Agent Fabric — One-command local bootstrap
# Usage: ./scripts/setup.sh

set -e

echo "🚀 Epic Agent Fabric — Local Setup"
echo "=================================="

# 1. Create volume directories
mkdir -p volume/{executor,voice,media,models}
echo "✓ Volume directories created"

# 2. Check for .env
if [ ! -f .env ]; then
  echo "⚠️  No .env file found. Creating from .env.example..."
  cp .env.example .env 2>/dev/null || echo "STRIPE_API_KEY=\nGROQ_API_KEY=\nOPENAI_API_KEY=\nZAPIER_API_KEY=" > .env
fi

# 3. Pull / build images
echo "📦 Pulling and building containers (this may take a few minutes)..."
docker compose pull || true
docker compose build --parallel

# 4. Start core services
echo "🔄 Starting core services..."
docker compose up -d executor-gateway tokenos redis

echo ""
echo "✅ Epic Agent Fabric is now running locally!"
echo ""
echo "Services:"
echo "  • Executor Gateway:  http://localhost:8787"
echo "  • TokenOS:           http://localhost:7777"
echo "  • Redis:             localhost:6379"
echo ""
echo "Next steps:"
echo "  1. Add your API keys to .env"
echo "  2. Run: docker compose up -d"
echo "  3. Visit the landing page or start an agent session"
echo ""
echo "Full stack (including Media + Intelligence):"
echo "  docker compose --profile full up -d"
echo ""
echo "Happy building. Local. Owned. Token-native."
