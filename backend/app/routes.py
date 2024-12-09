from flask import Blueprint, request, jsonify
from .models import PullRequest, Repository
from . import db
from .services import generate_pull_request_summary, perform_code_review

api = Blueprint('api', __name__)

@api.route('/pull_requests', methods=['POST'])
def create_pull_request():
    data = request.json
    summary = generate_pull_request_summary(data['code'])
    new_pr = PullRequest(title=data['title'], summary=summary, repository_id=data['repository_id'])
    db.session.add(new_pr)
    db.session.commit()
    return jsonify({'id': new_pr.id}), 201

@api.route('/code_review', methods=['POST'])
def code_review():
    data = request.json
    review = perform_code_review(data['code'])
    return jsonify(review), 200

@api.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    repositories = Repository.query.filter(Repository.name.ilike(f'%{query}%')).all()
    return jsonify([repo.name for repo in repositories]), 200
