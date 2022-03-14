from . import db
from sqlalchemy.sql import func


class Issue(db.Model):
    """
    제목, 내용, 메일, 비밀번호, 작성자, 작성 날짜
    추후에 로그인 기능 첨부 후 모델 변경
    """

    issue_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    contents = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(100), nullable=False)
    issue_pw = db.Column(db.String(20), nullable=False)
    writer = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
