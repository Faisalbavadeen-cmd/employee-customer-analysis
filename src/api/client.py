import requests
from typing import Any


class APIClient:
    def get_data(self, url: str) -> dict[str, Any]:
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.json()

        except requests.Timeout:
            return {"error": "API request timed out"}

        except ValueError:
            return {"error": "Invalid JSON response"}

        except requests.RequestException as e:
            return {"error": str(e)}

        finally:
            print("API request completed")