"""Notes API route handlers."""
from flask import Blueprint, request, jsonify
from .models import db, Note
from .auth import require_api_key

notes_bp = Blueprint("notes", __name__, url_prefix="/notes")


@notes_bp.route("", methods=["GET"])
@require_api_key
def get_notes():
    notes = Note.query.order_by(Note.created_at.desc()).all()
    return jsonify([n.to_dict() for n in notes])


@notes_bp.route("/<int:note_id>", methods=["GET"])
@require_api_key
def get_note(note_id):
    note = db.get_or_404(Note, note_id)
    return jsonify(note.to_dict())


@notes_bp.route("", methods=["POST"])
@require_api_key
def create_note():
    data = request.get_json()
    if not data or not data.get("title") or not data.get("content"):
        return jsonify({"error": "title and content are required"}), 400

    note = Note(title=data["title"], content=data["content"])
    db.session.add(note)
    db.session.commit()
    return jsonify(note.to_dict()), 201


@notes_bp.route("/<int:note_id>", methods=["PUT"])
@require_api_key
def update_note(note_id):
    note = db.get_or_404(Note, note_id)
    data = request.get_json()
    if not data:
        return jsonify({"error": "Request body required"}), 400

    if "title" in data:
        note.title = data["title"]
    if "content" in data:
        note.content = data["content"]

    db.session.commit()
    return jsonify(note.to_dict())


@notes_bp.route("/<int:note_id>", methods=["DELETE"])
@require_api_key
def delete_note(note_id):
    note = db.get_or_404(Note, note_id)
    db.session.delete(note)
    db.session.commit()
    return "", 204
