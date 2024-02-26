import requests
import json
import ssl


class CSRClient:
    def __init__(self, username: str, password: str, base_url: str) -> None:
        self.base_url = base_url
        self.username = username
        self.password = password
        self.token = ""

        self.authenticate()

    def authenticate(self):

        url = f"{self.base_url}auth/token-services"

        payload = {}
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": "Basic Y29kaW5nbmV0d29ya3M6Y29kaW5nMjE=",
        }

        response = requests.request(
            "POST", url, headers=headers, data=payload, verify=False
        )

        self.token = response.json()["token-id"]

        print(response.text)

    def get_interfaces(self):
        # Implement REST call to get interfaces (example)

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "X-auth-token": self.token,
        }
        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        response = requests.get(
            f"{self.base_url}/interfaces", headers=headers, verify=False
        )
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Failed to get interfaces")

    # Add similar methods for update_interface, etc.
