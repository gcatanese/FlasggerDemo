from flask import request, Blueprint, jsonify
from random import randint

import logging

api_blueprint = Blueprint('api_blueprint', __name__)


@api_blueprint.route('/version')
def get_version():
    """
    Returns the API version
    GET endpoint with no parameters and no security.
    ---
    security: [] # No security
    responses:
      200:
        description: returns API version
        content:
            text/plain:
              schema:
                type: string
                example: v.1.0.0
    """
    return "1.0"


@api_blueprint.route('/tree/<id>')
def get_tree(id):
    """
    Gets a Tree 🌳
    GET endpoint with path and query parameters
    ---
    security:
        - bearerAuth: []
    definitions:
      Tree:
        type: object
        properties:
          id:
            type: integer
          name:
            type: string
          max_height:
            type: integer
          endangered:
            type: boolean
    parameters:
        - in: path
          name: id
          schema:
            type: integer
          required: true
          description: ID of the tree
          example: 1
        - in: query
          name: extended
          schema:
            type: boolean
          required: false
          description: Boolean parameter, when true fetch all attributes
          example: true
    responses:
      200:
        description: returns a Tree
        content:
          application/json:
            schema:
              $ref: '#/definitions/Tree'
            examples:
              Dragon tree example:
                summary: returns Dragon tree
                value:
                  id: 1
                  name: Dragon tree
                  max_height: 15m
              Dragon tree extended version example:
                summary: returns extended Dragon tree
                value:
                  id: 1
                  name: Dragon tree
                  max_height: 15m
                  endangered: True
    """
    extended = request.args.get('extended')

    if extended:
        data = {"id": 1, "name": "Dragon tree", "max_height": "15m", "endangered": True}
    else:
        data = {"id": 1, "name": "Dragon tree", "max_height": "15m"}

    return jsonify(data)


@api_blueprint.route('/trees')
def get_trees():
    """
    Gets array of Tree 🌳
    GET endpoint returning arrays of entities
    ---
    security:
        - bearerAuth: []
    parameters:
        - in: path
          name: id
          schema:
            type: integer
          required: true
          description: ID of the entity
          example: 100
        - in: query
          name: extended
          schema:
            type: boolean
          required: false
          description: Boolean parameter, when true fetch all attributes
          example: true
    responses:
      200:
        description: returns API version
        content:
          text/plain:
            schema:
              $ref: '#/definitions/Tree'
            examples:
              - {"id": 1, "name": "Dragon tree", "max_height": "15m"}
    """
    data = {
        "trees": [
            {"id": 1, "name": "Dragon tree", "max_height": "15m"},
            {"id": 3, "name": "Giant sequoia", "max_height": "80m"},
            {"id": 3, "name": "Cacao tree", "max_height": "8m"}
        ]
    }
    return jsonify(data)


@api_blueprint.route('/tree', methods=['POST'])
def create_tree():
    """
    Creates a Tree 🌳
    POST endpoint
    ---
    security:
        - bearerAuth: []
    requestBody:
        description: JSON payload with the card attributes
        required: true
        content:
          application/json:
            schema:
              $ref: '#/definitions/Tree'
            examples:
              one:
                summary: Create new Tree
                value: {"name": "Dragon tree", "max_height": "15m", "endangered": true}
    responses:
      200:
        description: returns id of the newly planted Tree
        content:
            text/plain:
              schema:
                type: string
                example: 10
      401:
        description: Unauthorized. Token is missing or invalid
        content:
            text/plain:
              schema:
                type: string
                example: Missing token
    """

    return 'url'


@api_blueprint.route('/random')
def random():
    """
    Returns a random number
    GET endpoint documenting multiple Response Codes
    ---
    security:
      - bearerAuth: []
    responses:
      200:
        description: returns a random number
        content:
            text/plain:
              schema:
                type: integer
                example: 111
      400:
        description: Bad request. Parameter is missing or malformed
        content:
            text/plain:
              schema:
                type: string
                example: Parameter X not provided
      401:
        description: Unauthorized. Token is missing or invalid
        content:
            text/plain:
              schema:
                type: string
                example: Missing token
      500:
        description: Server error
        content:
            text/plain:
              schema:
                type: string
                example: An unexpected error has occurred
    """
    return randint(0, 1000)


def validate_api_token(request):
    """
    Validate token in API calls
    :param request:
    """
    if 'Authorization' not in request.headers:
        logging.warning('Authorization header not found')
        raise InvalidTokenException("Missing token")

    header = request.headers['Authorization']

    if not header.startswith('Bearer '):
        logging.warning('Invalid token: {} '.format(header))
        raise InvalidTokenException("Invalid token")

    token = header[7:]

    return True


def validate_input(json):
    if 'url' not in json:
        raise ValidationException("URL is missing")
    if 'title' not in json:
        raise ValidationException("Title is missing")
    if 'image' not in json:
        raise ValidationException("Image is missing")


class ValidationException(Exception):
    pass


class InvalidTokenException(Exception):
    pass


@api_blueprint.errorhandler(InvalidTokenException)
def invalid_token(e):
    return jsonify(error=str(e)), 401


@api_blueprint.errorhandler(ValidationException)
def validation_error(e):
    return jsonify(error=str(e)), 400


@api_blueprint.errorhandler(Exception)
def unexpected_error(e):
    return jsonify(error=str(e)), 500
