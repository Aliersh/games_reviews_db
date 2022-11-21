from flask import Blueprint, jsonify, abort, request
from ..models import Publishers, db

bp = Blueprint('publishers', __name__, url_prefix='/publishers')

# Show all publishers (index)

@bp.route('', methods=['GET'])
def index():
    publishers = Publishers.query.all()
    result = []
    for p in publishers:
        result.append(p.serialize())
    return jsonify(result)

# Show publisher by id

@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    p = Publishers.query.get_or_404(id)
    return jsonify(p.serialize())

# Create publisher

@bp.route('', methods=['POST'])
def create():
    if 'name' not in request.json:
        return abort(400)
    p = Publishers(
        name = request.json['name']
    )
    db.session.add(p)
    db.session.commit()
    return jsonify(p.serialize())

# Delete a publisher

@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    p = Publishers.query.get_or_404(id)
    try:
        db.session.delete(p)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)