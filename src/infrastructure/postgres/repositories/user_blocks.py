from sqlalchemy.orm import Session
from src.infrastructure.postgres.models.user_blocks import UserBlocks


class UserBlocksRepository:
    def get_user_blocks(self, user_id: int, db: Session):
        user_blocks = db.query(UserBlocks).filter_by(user_id=user_id).all()
        return user_blocks

    def create_user_block(self, user_id: int, block_id: int, statistics: float, db: Session):
        new_user_block = UserBlocks(
            user_id=user_id,
            block_id=block_id,
            statistics=statistics
        )
        db.add(new_user_block)
        db.commit()
        db.refresh(new_user_block)
        return new_user_block
    

user_blocks_repository: UserBlocksRepository = UserBlocksRepository()
