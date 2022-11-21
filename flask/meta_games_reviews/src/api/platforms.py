from flask import Blueprint, jsonify, abort, request
from ..models import Platforms, db

bp = Blueprint('platforms', __name__, url_prefix='/platforms')

# Show all platforms (index)

@bp.route('', methods=['GET'])
def index():
    platforms = Platforms.query.all()
    result = []
    for p in platforms:
        result.append(p.serialize())
    return jsonify(result)

# Show platform by id

@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    p = Platforms.query.get_or_404(id)
    return jsonify(p.serialize())

# Create platform

@bp.route('', methods=['POST'])
def create():
    if 'name' not in request.json:
        return abort(400)
    p = Platforms(
        name = request.json['name']
    )
    db.session.add(p)
    db.session.commit()
    return jsonify(p.serialize())

# Delete a platform

@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    p = Platforms.query.get_or_404(id)
    try:
        db.session.delete(p)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)