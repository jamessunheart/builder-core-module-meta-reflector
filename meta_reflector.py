# meta_reflector module
import requests
from collections import Counter

def run(_: str = None) -> dict:
    try:
        response = requests.post(
            "https://core-builder-v-2-jamesrickstinso.replit.app/api/modules/memory_core/run",
            json={"payload": {"action": "retrieve"}}
        )
        logs = response.json().get("results", [])
    except Exception as e:
        return {"error": str(e)}

    if not logs:
        return {"summary": "No memory logs found."}

    # Analyze type distribution
    types = [log['type'] for log in logs]
    type_counts = Counter(types)

    # Detect potential gaps
    expected = {"evolution", "decision", "insight", "event"}
    missing = list(expected - set(type_counts))

    return {
        "log_count": len(logs),
        "type_distribution": dict(type_counts),
        "missing_types": missing,
        "summary": f"Memory contains {len(logs)} entries. Missing categories: {', '.join(missing) if missing else 'none.'}"
    }