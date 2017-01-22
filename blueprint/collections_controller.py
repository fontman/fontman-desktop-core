""" Collections controller

Provides collections REST API for Fontman client GUI

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 22/1/2017
"""

from flask import Blueprint, jsonify, request

from service import CollectionService
from service import FontCollectionService

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


@collections_blueprint.route("/collections/<collection_id>/fonts")
def find_fonts_by_collection_id(collection_id):
    response_data = []

    for record in FontCollectionService().find_by_collection_id(collection_id):
        response_data.append(record.font_id)

    return jsonify(response_data)


@collections_blueprint.route("/collections/new", methods=["POST"])
def add_new_collection():
    json_data = request.json