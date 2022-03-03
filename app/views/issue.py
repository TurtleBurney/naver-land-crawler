from flask import render_template, request, redirect, url_for

from app import db
from app.forms import IssueForm
from app.views.blueprint import bp_issue

from database.models.issue import Issue


@bp_issue.route("/list/")
def get_list():
    issues = Issue.query.all()
    return render_template("issue/issue_list.html", issue_list=issues)


@bp_issue.route("/detail/<int:issue_id>/")
def get_detail(issue_id):
    issue = Issue.query.get_or_404(issue_id)
    return render_template("issue/issue_detail.html", issue=issue)


@bp_issue.route("/create/", methods=("GET", "POST"))
def create_issue():
    form = IssueForm()
    if request.method == "POST" and form.validate_on_submit():
        new_issue = Issue(
            title=form.title.data,
            contents=form.contents.data,
            email=form.email.data,
            issue_pw=form.issue_pw.data,
            writer=form.writer.data,
        )
        db.session.add(new_issue)
        db.session.commit()
        return redirect(url_for("issue.get_list"))
    return render_template("issue/issue_post.html", form=form)
