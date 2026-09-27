from typing import Any
import requests


class APIClient:

    def get_data(
        self,
        url: str
    ) -> dict[str, Any]:

        try:
            response = requests.get(
                url,
                timeout=10
            )

            response.raise_for_status()

            try:
                return response.json()

            except ValueError:
                return {
                    "error": "Invalid JSON response"
                }

        except requests.Timeout:
            return {
                "error": "API request timed out"
            }

        except requests.RequestException as error:
            return {
                "error": str(error)
            }

        finally:
            print("API request completed")