#!/bin/bash
set -e

echo "🚀 Iniciando análisis completo..."

./run-sast.sh
./run-sca.sh
./generate-sbom.sh

echo "🔗 Fusionando evidencias..."
cd ../analysis
python merge_evidence.py

echo "✅ Pipeline completo. Ver: evidence/combined_report.json"