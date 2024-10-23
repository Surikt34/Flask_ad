import requests
import json

BASE_URL = "http://localhost:8000/ads"

# Функция для создания объявления (POST)
def create_ad(title, description, owner):
    data = {
        "title": title,
        "description": description,
        "owner": owner
    }
    response = requests.post(BASE_URL, json=data)
    if response.status_code == 201:
        print("Ad created successfully:", response.json())
    else:
        print("Failed to create ad:", response.status_code, response.text)

# Функция для получения объявления (GET)
def get_ad(ad_id):
    response = requests.get(f"{BASE_URL}/{ad_id}")
    if response.status_code == 200:
        print("Ad details:", response.json())
    else:
        print("Failed to get ad:", response.status_code, response.text)

# Функция для удаления объявления (DELETE)
def delete_ad(ad_id):
    response = requests.delete(f"{BASE_URL}/{ad_id}")
    if response.status_code == 200:
        print("Ad deleted successfully:", response.json())
    else:
        print("Failed to delete ad:", response.status_code, response.text)

if __name__ == "__main__":
    # Пример использования функций

    # 1. Создание объявления
    create_ad("Продам велосипед", "Горный велосипед, 21 скорость", "Андрей")

    # 2. Получение объявления (ад с ID 0)
    get_ad(0)

    # 3. Удаление объявления (ад с ID 0)
    delete_ad(0)