from flask import Blueprint, jsonify, abort, request
from ..models import Review_sites, db

bp = Blueprint('review_sites', __name__, url_prefix='/review_sites')

# Show all review sites (index)

@bp.route('', methods=['GET'])
def index():
    review_sites = Review_sites.query.all()
    result = []
    for r in review_sites:
        result.append(r.serialize())
    return jsonify(result)

# Show review sites by id

@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    r = Review_sites.query.get_or_404(id)
    return jsonify(r.serialize())

# Create review site

@bp.route('', methods=['POST'])
def create():
    if 'name' not in request.json:
        return abort(400)
    r = Review_sites(
        name = request.json['name']
    )
    db.session.add(r)
    db.session.commit()
    return jsonify(r.serialize())

# Delete a review site

@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    r = Review_sites.query.get_or_404(id)
    try:
        db.session.delete(r)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)