import json
from pathlib import Path
from datetime import datetime
from typing import Any, Dict


def load_json(filepath: Path) -> Dict[str, Any]:
    """Carga un archivo JSON. Si falla, retorna un dict vacío."""
    if not filepath.exists():
        print(f"Archivo no encontrado: {filepath}")
        return {}

    if filepath.stat().st_size == 0:
        print(f"Archivo vacío: {filepath}")
        return {}

    try:
        with filepath.open('r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error de formato JSON en {filepath}: {e}")
    except Exception as e:
        print(f"Error cargando {filepath}: {e}")

    return {}

def save_json(filepath: Path, data: Dict[str, Any]) -> None:
    """Guarda JSON con formato, creando directorios si es necesario."""
    filepath.parent.mkdir(parents=True, exist_ok=True)
    try:
        with filepath.open('w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Archivo guardado: {filepath}")
    except Exception as e:
        print(f"Error guardando {filepath}: {e}")
        
def summarize_data(sast: Dict, sca: Dict, sbom: Dict) -> Dict[str, int]:
    """Genera el resumen de cantidades de evidencias."""
    return {
        "sast_issues": len(sast.get("results", [])),
        "sca_vulnerabilities": len(sca.get("dependencies", [])),
        "sbom_components": len(sbom.get("components", [])),
    }
           
def merge_evidence():
    base_path = Path(__file__).resolve().parent.parent / "evidence"

    files = {
        "sast": base_path / "sast.json",
        "sca": base_path / "sca.json",
        "sbom": base_path / "sbom.json",
    }

    print("🔍 Cargando evidencias...")

    # Cargar cada evidencia
    evidence = {key: load_json(path) for key, path in files.items()}

    # Crear resumen
    summary = summarize_data(
        evidence["sast"],
        evidence["sca"],
        evidence["sbom"],
    )

    # Crear reporte combinado
    combined_report = {
        "timestamp": datetime.now().isoformat(),
        "pipeline": "local-sarif-evidence-factory",
        "summary": summary,
        "evidence": evidence,
    }

    # Guardar reporte final
    output_file = base_path / "combined_report.json"
    save_json(output_file, combined_report)

    # Print resumen
    print("\nResumen de evidencias:")
    for key, value in summary.items():
        print(f"   - {key.replace('_', ' ').title()}: {value}")

    print("\nReporte combinado generado exitosamente.")


if __name__ == "__main__":
    merge_evidence()