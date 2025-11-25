#!/bin/bash
set -e

echo "🔍 Ejecutando SCA con pip-audit..."

cd ../app
pip-audit --format json --output ../evidence/sca.json || true

echo "✅ SCA completado: evidence/sca.json"