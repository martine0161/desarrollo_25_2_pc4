# Proyecto 11 - Local SARIF & Evidence Factory

Pipeline local de análisis de seguridad para código Python.

## ¿Qué hace?

- Analiza código con Bandit (SAST)
- Escanea dependencias con pip-audit (SCA)  
- Genera SBOM con CycloneDX
- Fusiona todo en un reporte JSON

## Estructura
```
local-sarif-evidence-factory/
├── app/              # API Flask de ejemplo
├── scripts/          # Scripts de análisis
├── analysis/         # Fusión de resultados
├── evidence/         # Reportes generados
├── docker/           # Dockerfile
└── Makefile
```

## Uso
```bash
# Instalar
make setup

# Analizar
make scan

# Docker
make docker-build
make docker-run

# Probar API
curl -X POST http://localhost:5000/calculate \
  -H "Content-Type: application/json" \
  -d '{"operation":"add","a":5,"b":3}'
```

## Resultados

El pipeline encontró **4 CVEs** en las dependencias:

- **Flask 2.3.0** - CVE-2023-30861 (session caching)
- **requests 2.31.0** - CVE-2024-35195 y CVE-2024-47081  
- **pip 25.2** - CVE-2025-8869 (path traversal)

Total: 110 dependencias analizadas.

## Comandos
```bash
make setup        # Instalar todo
make scan         # Ejecutar análisis
make docker-build # Construir imagen
make docker-run   # Correr contenedor
make clean        # Limpiar archivos
```

## Notas

- Flask y requests tienen versiones viejas **intencionalmente** para probar la detección
- El usuario Docker es `scanner` (no root)
- SBOM no funcionó, pendiente de revisar