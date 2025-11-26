#!/bin/bash
set -eo pipefail

# Directorio en donde está este script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Directorio raíz del proyecto (uno arriba de /scripts)
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

# Definimos varaibles
APP_DIR="$PROJECT_ROOT/app"
OUTPUT_DIR="$PROJECT_ROOT/evidence"
OUTPUT_JSON="$OUTPUT_DIR/sast.json"
OUTPUT_HTML="$OUTPUT_DIR/sast.html"

echo "🔍 Ejecutando SAST con Bandit..."

# Creamos directorio para salida de reportes
mkdir -p "$OUTPUT_DIR"

# Ejecutamos bandit evita que el script falle si Bandit encuentra vulnerabilidades
bandit -r "$APP_DIR" -f json -o "$OUTPUT_JSON" || true
bandit -r "$APP_DIR" -f html -o "$OUTPUT_HTML" || true

echo "SAST completado y reportes generados en: evidence"
echo "  - JSON: $OUTPUT_JSON"
echo "  - HTML: $OUTPUT_HTML"
