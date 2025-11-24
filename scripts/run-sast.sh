#!/bin/bash
set -e

echo "🔍 Ejecutando SAST con Bandit..."

bandit -r ../app -f json -o ../evidence/sast.json || true

echo "✅ SAST completado: evidence/sast.json"