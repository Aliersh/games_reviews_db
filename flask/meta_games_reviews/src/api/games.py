from flask import Blueprint, jsonify, abort, request
from ..models import Games, Developers, Publishers, db

bp = Blueprint('games', __name__, url_prefix='/games')

# Show all games (index)

@bp.route('', methods=['GET'])
def index():
    games = Games.query.all()
    result = []
    for g in games:
        result.append(g.serialize())
    return jsonify(result)

# Show game by id

@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    g = Games.query.get_or_404(id)
    return jsonify(g.serialize())

# Create game

@bp.route('', methods=['POST'])
def create():
    if 'name' not in request.json or 'genre' not in request.json or 'release_date' not in request.json or 'multiplayer' not in request.json or 'developer_id' not in request.json or 'publisher_id' not in request.json:
        return abort(400)
    Developers.query.get_or_404(request.json['developer_id'])
    Publishers.query.get_or_404(request.json['publisher_id'])
    g = Games(
        name = request.json['name'],
        genre = request.json['genre'],
        esrb_rating = request.json['esrb_rating'],
        release_date = request.json['release_date'],
        multiplayer = request.json['multiplayer'],
        developer_id = request.json['developer_id'],
        publisher_id = request.json['publisher_id'],
    )
    db.session.add(g)
    db.session.commit()
    return jsonify(g.serialize())

# Delete a game

@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    g = Games.query.get_or_404(id)
    try:
        db.session.delete(g)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)
