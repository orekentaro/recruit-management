import sys

from models.base_model import ENGINE, BaseModel
from sqlalchemy import Column, Integer, Text


class ProgressMaster(BaseModel):
    """進捗マスタ"""

    __tablename__ = "progress_master"
    progress_id = Column("progress_id", Integer, nullable=False, primary_key=True)
    title = Column("title", Text, nullable=False)


def create_progress_master(args):
    BaseModel.metadata.create_all(bind=ENGINE)


if __name__ == "__main__":
    create_progress_master(sys.argv)