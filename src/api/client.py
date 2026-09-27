import requests


class APIClient:

    def get_data(self, url):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            try:
                return response.json()
            except ValueError:
                return {"error": "Invalid JSON response"}

        except requests.Timeout:
            return {"error": "API request timed out"}

        except requests.RequestException as e:
            return {"error": str(e)}

        finally:
            print("API request completed")