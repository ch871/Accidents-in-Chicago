from flask import Blueprint, jsonify, request
from database.connect import area_colaction
from bson import ObjectId
from repository.area_repository import get_statictic_injuries_by_area, get_count_eccident_by_area, get_contributing_factors

area_bp = Blueprint('area', __name__)


@area_bp.route('/count', methods=['GET'])
def get_count_eccident_by_area():
    area = request.args.get('area')
    if not area:
        return jsonify({"error": "Area parameter is required"}), 400

    result = get_count_eccident_by_area(area)
    if result is None:
        return jsonify({"error": f"No data found for area: {area}"}), 404

    return jsonify({"total_injuries": result})


@area_bp.route('/contributing-factors', methods=['GET'])
def get_contributing_factors_endpoint():
    area = request.args.get('area')
    if not area:
        return jsonify({"error": "Area parameter is required"}), 400

    result = get_contributing_factors(area)
    if result is None:
        return jsonify({"error": f"No data found for area: {area}"}), 404

    return jsonify({"contributing_factors": result})


@area_bp.route('/statistics', methods=['GET'])
def get_statictic_injuries_by_area_endpoint():
    area = request.args.get('area')
    if not area:
        return jsonify({"error": "Area parameter is required"}), 400

    result = get_statictic_injuries_by_area(area)
    if result is None:
        return jsonify({"error": f"No data found for area: {area}"}), 404

    return jsonify({"injuries": result})
