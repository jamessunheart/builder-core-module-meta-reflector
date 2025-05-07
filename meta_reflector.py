# meta_reflector (snapshot version)
import requests

def run(_: str = None) -> dict:
    try:
        response = requests.post(
            "https://core-builder-v-2-jamesrickstinso.replit.app/api/modules/memory_core/run",
            json={"payload": {"action": "snapshot"}}
        )
        data = response.json()
    except Exception as e:
        return {"error": f"Failed to retrieve snapshot: {str(e)}"}

    return {
        "summary": f"Memory contains {data.get('count', 0)} entries across {len(data.get('types', []))} types and {len(data.get('contexts', []))} contexts.",
        "details": data
    }