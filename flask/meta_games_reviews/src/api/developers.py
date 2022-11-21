from flask import Blueprint, jsonify, abort, request
from ..models import Developers, db

bp = Blueprint('developers', __name__, url_prefix='/developers')

# Show all developers (index)

@bp.route('', methods=['GET'])
def index():
    developers = Developers.query.all()
    result = []
    for d in developers:
        result.append(d.serialize())
    return jsonify(result)

# Show developer by id

@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    d = Developers.query.get_or_404(id)
    return jsonify(d.serialize())

# Create developer

@bp.route('', methods=['POST'])
def create():
    if 'name' not in request.json:
        return abort(400)
    d = Developers(
        name = request.json['name']
    )
    db.session.add(d)
    db.session.commit()
    return jsonify(d.serialize())

# Delete a developer

@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    d = Developers.query.get_or_404(id)
    try:
        db.session.delete(d)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)