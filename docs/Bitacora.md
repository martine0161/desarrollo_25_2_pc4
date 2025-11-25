# Bitácora - Proyecto 11

## 21 Nov 2025 - Mañana

### Setup inicial
- Creé la estructura de carpetas
- App Flask simple con code smells (variables globales, sin validación, etc)
- Scripts bash para cada herramienta: SAST, SCA, SBOM

### Problemas con Makefile
El Makefile no funcionaba porque usé espacios en vez de tabs. Git Bash me los convertía automáticamente. Tuve que recrearlo con nano.

### Scripts de análisis
- `run-sast.sh` - Bandit funcionó directo
- `run-sca.sh` - Cambié de safety a pip-audit porque safety está deprecated
- `generate-sbom.sh` - CycloneDX se instaló pero no generó nada, no sé por qué

Agregué `|| true` a todos para que no falle el pipeline si hay issues.

## 21 Nov 2025 - Tarde  

### Fusión de resultados
El script `merge_evidence.py` lee los 3 JSON y los junta. Uso `Path(__file__).parent.parent` para rutas absolutas porque las relativas fallaban.

Si un archivo no existe, retorna `{}` vacío en vez de explotar.

### Docker

**Primer intento:** Dockerfile se llamaba `Dockerfile.dockerfile` 🤦
**Solución:** Renombrar a solo `Dockerfile`

**Segundo intento:** Build exitoso, ~30 segundos, 183MB

Usuario `scanner` en el contenedor, no root. Se puede verificar con:
```bash
docker exec -it $(docker ps -q) whoami
```

### Pruebas de la API

```bash
# Suma
curl -X POST http://localhost:5000/calculate \
  -H "Content-Type: application/json" \
  -d '{"operation":"add","a":5,"b":3}'
# {"result":8} ✓

# División por cero (el code smell)
curl -X POST http://localhost:5000/calculate \
  -H "Content-Type: application/json" \
  -d '{"operation":"divide","a":10,"b":0}'
# ZeroDivisionError ✓ (esperado)
```

## Resultados

### SAST (Bandit)
- 0 issues encontrados
- Revisó 31 líneas de código
- Los code smells que puse no son "vulnerabilidades" que Bandit detecte

### SCA (pip-audit)  
- 110 dependencias analizadas
- **4 CVEs encontrados:**
  - Flask 2.3.0 → CVE-2023-30861
  - requests 2.31.0 → CVE-2024-35195, CVE-2024-47081
  - pip 25.2 → CVE-2025-8869

### SBOM
- No generó nada
- El script corre pero sbom.json queda vacío
- Pendiente: investigar flags de cyclonedx-py

## Problemas y soluciones

1. **Makefile con espacios** → Usar tabs, verificar con `cat -A`
2. **Dockerfile.dockerfile** → Renombrar a `Dockerfile`
3. **Rutas relativas en Python** → Usar `Path(__file__)`
4. **SBOM vacío** → Pendiente, pero el pipeline no falla

## Tiempo

- Setup y scripts: ~3 horas
- Docker: ~2 horas (incluyendo debugging)
- Pruebas y documentación: ~2 horas
- **Total: ~7 horas**

## Lo que aprendí

- pip-audit es mejor que safety
- `|| true` en bash es clave para pipelines que no deben fallar
- Docker multi-stage no era necesario aquí, pero lo consideré
- Usuario no root es importante hasta para contenedores de dev

## Próximos pasos (si hubiera tiempo)

- [ ] Arreglar SBOM
- [ ] Convertir a formato SARIF real
- [ ] Agregar más tests
- [ ] Integrar con GitHub Actions