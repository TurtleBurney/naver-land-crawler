from . import db


class Region(db.Model):
    region_code = db.Column(db.String(50), primary_key=True)

    city = db.Column(db.String(10), nullable=False)
    gu = db.Column(db.String(10), nullable=True)
    dong = db.Column(db.String(10), nullable=True)

    parent_region_code = db.Column(db.String(50), nullable=True)

    # Back Reference
    buildings = db.relationship("Building", backref=db.backref("region"))
