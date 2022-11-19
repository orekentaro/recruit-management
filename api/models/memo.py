import sys

from models.base_model import ENGINE, BaseModel
from sqlalchemy import Column, ForeignKey, Integer, Text


class Memo(BaseModel):
    """求職者情報"""

    __tablename__ = "memo"
    memo_id = Column("memo_id", Integer, nullable=False, primary_key=True)
    job_id = Column(
        "job_id",
        Integer,
        ForeignKey("job_seeker.job_id", onupdate="CASCADE", ondelete="CASCADE"),
    )
    memo = Column("memo", Text, nullable=False)


def create_memo(args):
    BaseModel.metadata.create_all(bind=ENGINE)


if __name__ == "__main__":
    create_memo(sys.argv)