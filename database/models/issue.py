from sqlalchemy import Column, DateTime, Integer, String, Text
from sqlalchemy.sql import func

from database.models import Base


class Issue(Base):
    __tablename__ = "issue"

    """
    제목, 내용, 메일, 비밀번호, 작성자, 작성 날짜
    추후에 로그인 기능 첨부 후 모델 변경
    """

    issue_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    contents = Column(Text, nullable=False)
    email = Column(String(100), nullable=False)
    issue_pw = Column(String(20), nullable=False)
    writer = Column(String(100), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
