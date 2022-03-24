import sys, os

SCRIPT_DIR = os.path.dirname(__file__)
ROOT_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, "../../"))
sys.path.insert(0, ROOT_DIR)

from region_parser import RegionParser
from db_storer import DBStorer
from database.models.region import Region


def run():
    region_parser = RegionParser()
    region_parser.run()

    region_storer = DBStorer(model=Region)
    region_storer.add_data(region_parser.regions)


if __name__ == "__main__":
    run()
