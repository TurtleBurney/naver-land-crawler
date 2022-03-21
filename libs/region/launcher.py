import sys, os

sys.path.append(
    os.path.dirname(
        os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
    )
)

from region_parser import RegionParser
from db_store import DbStorer
from database.models.region import Region


def run():
    region_parser = RegionParser()
    region_parser.run()
    db_store = DbStorer(Region, region_parser.regions)
    db_store.run()


if __name__ == "__main__":
    run()
