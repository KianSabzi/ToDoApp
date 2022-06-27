
from flask import jsonify, render_template
from . import category_api_blueprint
from backend.models import Category, db ,category_schema,categories_schema



@category_api_blueprint.route('/api/categories', methods=['GET'])
def get_categories():
    all_categories = Category.query.all()
    results = categories_schema.dump(all_categories)
    return jsonify(results)

@category_api_blueprint.route('/api/catDropdown', methods=['GET'])
def getAll():
    categories = Category.query.all()
    cats = categories_schema.dump(categories)
    return render_template("../../src/ui/index.html", cats = cats)

