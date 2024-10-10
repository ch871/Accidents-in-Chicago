from flask import Blueprint, jsonify, request
from repository.csv_repository import init_accidents


init_bp = Blueprint('date', __name__)


@init_bp.route('/', methods=['GET'])
def init_db_endpoint():
    result = init_accidents()
    if result is None:
        return jsonify({"error": "dat wasnt inserted"}), 404

    return jsonify({'secces':'data was inserted'}), 200

