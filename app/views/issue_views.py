from flask import Blueprint, render_template, request
from app.models.issue import Issue
from app import db


bp_issue = Blueprint('issue', __name__, url_prefix='/issue')

@bp_issue.route('/list/')
def get_list():
    issues = Issue.query.all()
    return render_template('issue/issue_list.html', issue_list = issues)

@bp_issue.route('/detail/<int:issue_id>/')
def get_detail(issue_id):
    issue = Issue.query.get_or_404(issue_id)
    return render_template('issue/issue_detail.html', issue = issue)

@bp_issue.route('/post/', methods=('POST',))
def post_issue():
    # render template 이후에 이 동작 일어나야하고 마지막 return은 다시 list창으론
    title = request.form['title']
    contents = request.form['contents']
    email = request.form['email']
    issue_pw = request.form['issue_pw']
    writer = request.form['writer']
    new_issue = Issue(title=title, contents=contents, email=email, issue_pw=issue_pw, writer=writer)
    db.session.add(new_issue)
    db.session.commit()
    return render_template('issue/issue_post.html')
    