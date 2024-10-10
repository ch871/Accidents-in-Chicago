from flask import Blueprint, jsonify, request
from repository.date_repository import find_by_day, find_by_week, find_by_month
import json
from bson import json_util

date_bp = Blueprint('date', __name__)


@date_bp.route('/day', methods=['GET'])
def find_by_day_endpoint():
    # Get the date and area from query parameters
    date = request.args.get('date')
    area = request.args.get('area')
    if date is None or area is None:
        return jsonify({"error": "Both 'date' and 'area' parameters are required"}), 400

    # Query the database
    result = find_by_day(date, area)

    if result is None:
        return jsonify({"error": f"No data found for date: {date} and area: {area}"}), 404

    return json.loads(json_util.dumps(result))


@date_bp.route('/week', methods=['GET'])
def find_by_week_endpoint():
    week_start = request.args.get('week_start')
    area = request.args.get('area')

    if not week_start or not area:
        return jsonify({"error": "Both 'week_start' and 'area' parameters are required"}), 400

    # Query the database
    result = find_by_week(week_start,area)

    if not result:
        return jsonify({"error": f"No data found for week_start: {week_start} and area: {area}"}), 404

    return json.loads(json_util.dumps(result))


@date_bp.route('/month', methods=['GET'])
def find_by_month_endpoint():
    month = request.args.get('month')
    area = request.args.get('area')

    if not month or not area:
        return jsonify({"error": "Both 'month' and 'area' parameters are required"}), 400

    result = find_by_month(month,area)

    if not result:
        return jsonify({"error": f"No data found for month: {month} and area: {area}"}), 404

    return json.loads(json_util.dumps(result))
