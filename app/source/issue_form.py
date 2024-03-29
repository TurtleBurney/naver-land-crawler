from flask_wtf import FlaskForm
from wtforms import (EmailField, PasswordField, StringField, SubmitField,
                     TextAreaField)
from wtforms.validators import DataRequired, Email, Length


class IssueForm(FlaskForm):
    title = StringField("title", validators=[DataRequired()])
    contents = TextAreaField("contents", validators=[DataRequired()])
    # 추후 EmailFiend써서 Email valid도 확인하기
    email = StringField("email", validators=[DataRequired()])
    issue_pw = PasswordField("issue_pw", validators=[DataRequired(), Length(min=4)])
    writer = StringField("writer", validators=[DataRequired()])
    submit = SubmitField("등록")
