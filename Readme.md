# Proyecto 11 - Local SARIF & Evidence Factory

Pipeline local de análisis de seguridad para código Python.

## ¿Qué hace?

- Analiza código con Bandit (SAST)
- Escanea dependencias con pip-audit (SCA)  
- Genera SBOM con CycloneDX
- Fusiona todo en un reporte JSON

## Instalación

```bash
make setup
```

## Uso

```bash
# Ejecutar análisis completo
make scan

# Ver resultados
cat evidence/combined_report.json
```

## Docker

```bash
make docker-build
make docker-run

# Probar API
curl -X POST http://localhost:5000/calculate \
  -H "Content-Type: application/json" \
  -d '{"operation":"add","a":5,"b":3}'
```

## Resultados

El pipeline detectó:
- **SAST**: 1 issue (B104 - hardcoded bind all interfaces)
- **SCA**: 4 CVEs (Flask, requests, pip)
- **SBOM**: 2 componentes catalogados

## Documentación

- `docs/Readme.md` - Guía detallada
- `docs/Bitacora.md` - Log de desarrollo
- `docs/Resultados.md` - Análisis de hallazgos