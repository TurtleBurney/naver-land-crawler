from flask import Blueprint, render_template, request, redirect, url_for

from app.source.issue_form import IssueForm

from database.models.issue import Issue

bp_issue = Blueprint("issue", __name__, url_prefix="/issue")


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
        # 외부로 데이터 빼내어 저장은 다른 부분에서 로직으로 처리
        return redirect(url_for("issue.get_list"))
    else:
        return render_template("issue/issue_post.html", form=form)
