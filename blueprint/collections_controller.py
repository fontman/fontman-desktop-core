""" Collections controller

Provides collections REST API for Fontman client GUI

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 22/1/2017
"""

from service import CollectionService
from service import FontCollectionService

from flask import Blueprint, jsonify, request

collections_blueprint = Blueprint("collections_blueprint", __name__)


@collections_blueprint.route("/collections")
def find_all_collections():
    response_data = []

    for collection in CollectionService().find_all():
        response_data.append(
            {
                "collection_id": collection.collection_id,
                "name": collection.name,
                "type": collection.type
            }
        )

    return jsonify(response_data)


@collections_blueprint.route("/collections/status")
def find_collections_status():
    if CollectionService().find_all().first is None:
        return jsonify(False)

    else:
        return jsonify(True)


@collections_blueprint.route("/collections/<collection_id>/fonts")
def find_fonts_by_collection_id(collection_id):
    response_data = []

    for record in FontCollectionService().find_by_collection_id(collection_id):
        response_data.append(record.font_id)

    return jsonify(response_data)


@collections_blueprint.route("/collections/<collection_id>/install")
def install_fonts_by_collection_id(collection_id):
    fonts = FontCollectionService().find_by_collection_id(collection_id)

    return jsonify(True)


@collections_blueprint.route("/collections/<collection_id>/fonts/<font_id>/add")
def add_font_by_collection_id(collection_id, font_id):
    FontCollectionService().add_new(collection_id, font_id)
    return jsonify(True)


@collections_blueprint.route("/collections/new", methods=["POST"])
def add_new_collection():
    json_data = request.json
    CollectionService().add_new(json_data["name"], json_data["type"])

    return jsonify(True)


@collections_blueprint.route(
    "/collections/<collection_id>/update", methods=["POST"]
)
def update_collection_by_id(collection_id):
    json_data = request.json
    CollectionService().update_by_collection_id(
        collection_id,
        {"name": json_data["name"], "type": json_data["type"]}
    )

    return jsonify(True)
