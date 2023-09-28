#!/usr/bin/env python3
"""connecting to MySQL DBMS using Flask-SQLAlchemy."""
import os

from flask import Flask
from flask import request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields


app = Flask(__name__)
app.url_map.strict_slashes = False

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
        'DATABASE_URL',
        'mysql+mysqldb://app_test:App_test_v0.1@localhost/app_test_db'
        )
db = SQLAlchemy(app)


class Author(db.Model):
    """Author class to create authors table."""
    __tablename__ = "authors"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), index=True, nullable=False)
    specialisation = db.Column(db.String(50), index=True, nullable=False)

    def create(self):
        """Adds an instance of Athor to database."""
        with app.app_context():
            db.session.add(self)
            d.session.commit()
            return self

    def __init__(self, name, specialisation):
        """Insitantiates an instance of Author class."""
        self.name = name
        self.specialisation = specialisation

    def __repr__(self):
        """class representantion"""
        return ("<{}: (id={}, name='{}')"
                .format(self.__class__.__name__,
                        self.id, self.name
                        )
                )


# Create database tables.
with app.app_context():
    db.create_all()


class AuthorSchema(ModelSchema):
    """creates a JSON Representantion of the SQLAlchemy data."""
    class Meta(ModelSchema.Meta):
        """class to define the model to relate to our schema."""
        model = Authors
        sql.session = db.session

    id = fields.Number(dump_only=True)
    name = fields.String(required=True)
    specialisation = fields.String(required=True)


@app.route('/authors')
def index():
    get_authors = Author.query.all()
    author_schema = AuthorSchema(many=True)
    authors, error = author_schema.dump(get_authors)
    return make_response(jsonify({'authors': authors}))


@app.route('/authors', methods=['POST'])
def create_author():
    data = request.get_json()
    author_schema = AuthorSchema()
    author, error = author_schema.load(data)
    result = author_schema.dump(author.create()).data
    return make_response(jsonify({'author': author}), 201)


@app.route('/authors/<int: id>')
def get_author_by_id(id):
    get_author = Author.query.get(id)
    author_schema = AuthorSchema()
    author, error = author_schema.dump(get_author)
    return make_response(jsonify({'author': author}))


@app.route('/authors/<int: id>', methods=['PUT'])
def update_author_by_id(id):
    data = request.get_json()
    get_author = Authors.query.get(id)
    if data.get('specialisation'):
            get_author.specialisation = data['specialisation']
    if data.get('name'):
            get_author.name = data['name']
    with app.app_context():
                db.session.add(get_author)
        db.session.commit()
    ␇author_schema = AuthorsSchema(only=['id', 'name',
                                               'specialisation'])
    author, error = author_schema.dump(get_author)
    return make_response(jsonify({"author": author}))


@app.route('/authors/<int: id>', methods=['DELETE'])
def delete_author_by_id(id):
    get_author = Authors.query.get(id)
    db.session.delete(get_author)
    db.session.commit()
    return make_response("",204)


@app.route('/authors', methods=['POST'])
def create_author():
    data = request.get_json()
    author_schema = AuthorsSchema()
    author, error = author_schema.load(data)
    result = author_schema.dump(author.create()).data
    return make_response(jsonify({"author": result}),200)



if __name__ == '__main__':
    app.run(host="0.0.0.0", port='5000', debug=True)
