from flask import request, Blueprint, jsonify, make_response
from random import randint

import logging

api_blueprint = Blueprint('api_blueprint', __name__)


@api_blueprint.route('/version')
def get_version():
    """
    Returns the API version
    GET endpoint with no parameters and **no security**.
    ---
    security: [] # No security
    tags:
        - get (no security)
    responses:
      200:
        description: returns API version
        content:
            text/plain:
              schema:
                type: string
                example: v.1.0.0
    """
    return "v1"


@api_blueprint.route('/markdown')
def markdown_demo():
    """
    Returns a message
    GET endpoint with markdown documentation

    tier 1 header
    # tier 5 header

    A **GET** endpoint to document usage of __markdown__
    Use of *italic*  is also  _possible_

    Check out the [markdown guide](https://www.markdownguide.org/basic-syntax/)

    show small bits of code with backticks: `print("hello world")`

    ---
    security: [] # No security
    tags:
        - get (no security)
    responses:
      200:
        description: ok
        content:
            text/plain:
              schema:
                type: string
                example: ok
    """
    return "ok"


@api_blueprint.route('/tree/<id>')
def get_tree(id):
    """
    Gets a Tree 🌳
    GET endpoint with path parameter
    ---
    security:
        - bearerAuth: []
    tags:
        - get
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
    data = {"id": id, "name": "Dragon tree", "max_height": "15m", "endangered": True}

    return jsonify(data)


@api_blueprint.route('/treeQueryParam')
def get_tree_query_parameter():
    """
    Gets a Tree 🌳
    GET endpoint with query parameter and deprecation of another parameter
    ---
    security:
        - bearerAuth: []
    tags:
        - get
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
        - in: query
          name: id
          schema:
            type: integer
          required: true
          description: ID of the tree
          example: 10
        - in: query
          name: identifier
          schema:
            type: integer
          deprecated: true
          required: false
          description: Identifier of the tree (deprecated)
          example: 10
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
    """
    # get query parameter
    id = request.args.get('id')

    data = {"id": id, "name": "Dragon tree", "max_height": "15m", "endangered": True}

    return jsonify(data)


@api_blueprint.route('/treeHeaderParam')
def get_tree_header_parameter():
    """
    Gets a Tree 🌳
    GET endpoint with header parameter
    ---
    security:
        - bearerAuth: []
    tags:
        - get
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
        - in: header
          name: X-Tree-ID
          schema:
            type: string
          required: true
          description: ID of the tree
          example: 1
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
    """
    # get query parameter
    id = request.headers.get('X-Request-ID')

    data = {"id": id, "name": "Dragon tree", "max_height": "15m", "endangered": True}

    return jsonify(data)


@api_blueprint.route('/treeEnumParam')
def get_tree_enum_parameter():
    """
    Gets a Tree 🌳
    GET endpoint with query parameter restricted to a fixed set of values (enum)
    ---
    security:
        - bearerAuth: []
    tags:
        - get
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
        - in: query
          name: id
          schema:
            type: integer
            default: 1
            enum:
              - 1
              - 2
              - 3
          required: false
          description: ID of the tree
          example: 1
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
    """
    # get query parameter
    id = request.args.get('id')

    data = {"id": id, "name": "Dragon tree", "max_height": "15m", "endangered": True}

    return jsonify(data)


@api_blueprint.route('/treeCookieParam')
def get_tree_cookie_parameter():
    """
    Gets a Tree 🌳
    GET endpoint with cookie parameter
    ---
    security:
        - bearerAuth: []
    tags:
        - get
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
        - in: cookie
          name: tree-id
          schema:
            type: string
          required: true
          description: ID of the tree
          example: 1
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
    """
    # get cookie (note: cookie must be set by the application)
    id = request.cookies.get('tree-id')

    data = {"id": 1, "name": "Dragon tree", "max_height": "15m", "endangered": True}

    return jsonify(data)


@api_blueprint.route('/tree/<name>')
def get_tree_by_name(name):
    """
    Gets a Tree 🌳 by name
    GET endpoint no longer supported
    ---
    deprecated: true
    security:
        - bearerAuth: []
    tags:
        - get
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
          name: name
          schema:
            type: string
          required: true
          description: Name of the tree
          example: Dragon tree
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
    tags:
        - get
    responses:
      200:
        description: returns list of Trees
        content:
          text/plain:
            schema:
              type: array
              items:
                $ref: '#/definitions/Tree'
            examples:
              list example:
                summary: returns array of trees
                value:
                  - id: 1
                    name: Dragon tree
                    max_height: 15m
                  - id: 2
                    name: Giant sequoia
                    max_height: 8m
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
    tags:
        - post
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
    tags:
        - get
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
