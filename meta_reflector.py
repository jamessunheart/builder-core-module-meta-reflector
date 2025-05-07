# Resilient meta_reflector
import requests
from collections import Counter

def run(_: str = None) -> dict:
    try:
        response = requests.post(
            "https://core-builder-v-2-jamesrickstinso.replit.app/api/modules/memory_core/run",
            json={"payload": {"action": "retrieve"}}
        )
        raw = response.json()
        logs = raw.get("results", []) if isinstance(raw, dict) else []
    except Exception as e:
        return {"error": f"Failed to retrieve memory: {str(e)}"}

    if not logs:
        return {"summary": "No memory entries available."}

    # Analyze distribution
    types = [log.get('type', 'unknown') for log in logs]
    type_counts = Counter(types)

    # Expected coverage
    expected = {"evolution", "decision", "insight", "event"}
    missing = list(expected - set(type_counts))

    return {
        "log_count": len(logs),
        "type_distribution": dict(type_counts),
        "missing_types": missing,
        "summary": f"{len(logs)} memory entries. Missing: {', '.join(missing) if missing else 'none'}"
    }