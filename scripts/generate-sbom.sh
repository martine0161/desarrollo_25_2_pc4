#!/bin/bash
set -e

echo "📦 Generando SBOM..."

cd ../app
cyclonedx-py requirements requirements.txt -o ../evidence/sbom.json || true

echo "✅ SBOM generado: evidence/sbom.json"