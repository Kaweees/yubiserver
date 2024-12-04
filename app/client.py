import requests
from typing import Dict, List, Optional
from app.models.item import Item

class FastAPIClient:
    def __init__(self, base_url: str = "http://localhost:8000"):
        """Initialize the client with a base URL"""
        self.base_url = base_url.rstrip('/')

    def create_item(self, name: str, description: str) -> Dict:
        """Create a new item"""
        payload = {
            "name": name,
            "description": description
        }
        try:
            response = requests.post(f"{self.base_url}/items/", json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to create item: {str(e)}")

    def get_items(self) -> List[Dict]:
        """Get all items"""
        try:
            response = requests.get(f"{self.base_url}/items/")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to get items: {str(e)}")

    def get_item(self, item_id: int) -> Optional[Dict]:
        """Get item by ID"""
        try:
            response = requests.get(f"{self.base_url}/items/{item_id}")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to get item: {str(e)}")

    def delete_item(self, item_id: int) -> Dict:
        """Delete an item"""
        try:
            response = requests.delete(f"{self.base_url}/items/{item_id}")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to delete item: {str(e)}")

if __name__ == "__main__":
    client = FastAPIClient()

    try:
        # Create some items
        item1 = client.create_item("Book", "An interesting book")
        print("Created item:", item1)

        item2 = client.create_item("Phone", "A smartphone")
        print("Created item:", item2)

        # Get all items
        items = client.get_items()
        print("\nAll items:", items)

        # Get specific item
        item = client.get_item(1)
        print("\nItem with ID 1:", item)

        # Delete an item
        result = client.delete_item(1)
        print("\nDelete result:", result)

        # Get all items again
        items = client.get_items()
        print("\nRemaining items:", items)

    except Exception as e:
        print(f"An error occurred: {str(e)}") 