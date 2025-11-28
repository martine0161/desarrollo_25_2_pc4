# Resultados del Análisis - Proyecto 11

## Ejecución del Pipeline
```bash
$ make scan
🚀 Iniciando análisis completo...
✅ SAST completado: evidence/sast.json
✅ SCA completado: evidence/sca.json
✅ SBOM generado: evidence/sbom.json
✅ Pipeline completo
📊 SAST issues: 1
📊 SCA vulnerabilities: 110
📊 SBOM components: 2
```

## Hallazgos de Seguridad

### SAST (Bandit)

**Issue detectado:** B104 - hardcoded_bind_all_interfaces

- **Severidad:** MEDIUM
- **Confianza:** MEDIUM
- **Ubicación:** app/main.py línea 33
- **Código:**
```python
  app.run(host='0.0.0.0', port=5000)
```
- **Problema:** Expone la aplicación a todas las interfaces de red
- **Recomendación:** Usar `host='127.0.0.1'` en desarrollo o configurar firewall en producción

### SCA (pip-audit)

**Dependencias analizadas:** 110  
**CVEs encontrados:** 4

1. **Flask 2.3.0**
   - CVE-2023-30861 (PYSEC-2023-62)
   - Severidad: Media
   - Problema: Session cookie caching en proxies
   - Fix: Actualizar a Flask 2.3.2

2. **requests 2.31.0**
   - CVE-2024-35195 (GHSA-9wx4-h78v-vm56)
   - Severidad: Alta
   - Problema: SSL verification bypass
   - Fix: Actualizar a requests 2.32.0
   
   - CVE-2024-47081 (GHSA-9hjg-9r4m-mvj7)
   - Severidad: Media
   - Problema: .netrc credentials leak
   - Fix: Actualizar a requests 2.32.4

3. **pip 25.2**
   - CVE-2025-8869 (GHSA-4xh5-x5gv-qwph)
   - Severidad: Alta
   - Problema: Path traversal en tarfile extraction
   - Fix: Actualizar a pip 25.3

### SBOM (CycloneDX)

**Componentes catalogados:** 2

1. **flask@2.3.0**
   - PURL: `pkg:pypi/flask@2.3.0`
   - Tipo: library
   - Distribución: https://pypi.org/simple/flask/

2. **requests@2.31.0**
   - PURL: `pkg:pypi/requests@2.31.0`
   - Tipo: library
   - Distribución: https://pypi.org/simple/requests/

## Conclusiones

El pipeline detectó exitosamente:
- 1 vulnerabilidad de código (SAST)
- 4 CVEs en dependencias (SCA)
- 2 componentes principales inventariados (SBOM)

Las versiones vulnerables fueron usadas **intencionalmente** para validar que el pipeline funciona correctamente. En producción, todas las dependencias deberían actualizarse a sus versiones seguras.