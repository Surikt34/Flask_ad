from flask import Flask, jsonify, request, abort
from datetime import datetime
from models import ads, Ad
from flask_cors import CORS

app = Flask('app')
CORS(app)  # Включаем CORS



# Создание объявления (POST)
@app.route('/ads', methods=['POST'])
def create_ad():
    data = request.get_json()

    # Проверка, что все необходимые поля присутствуют
    if not data or 'title' not in data or 'description' not in data or 'owner' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    new_ad = Ad(
        title=data['title'],
        description=data['description'],
        owner=data['owner']
    )
    ads.append(new_ad)  # Добавляем объявление в список

    return jsonify({'message': 'Объявление успешно создано', 'ad': new_ad.to_dict()}), 201

# Получение объявления по индексу (GET)
@app.route('/ads/<int:ad_id>', methods=['GET'])
def get_ad(ad_id):
    if 0 <= ad_id < len(ads):
        ad = ads[ad_id]
        return jsonify(ad.to_dict())
    else:
        abort(404)

# Удаление объявления (DELETE)
@app.route('/ads/<int:ad_id>', methods=['DELETE'])
def delete_ad(ad_id):
    if 0 <= ad_id < len(ads):
        deleted_ad = ads.pop(ad_id)
        return jsonify({'message': 'Объявление удалено', 'ad': deleted_ad.to_dict()})
    else:
        abort(404)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)