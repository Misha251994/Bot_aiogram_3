import bcrypt
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from app.database.models import User


async def create_user(
    async_session: async_sessionmaker[AsyncSession],
    user_id,
    username,
    email,
    mb_phone,
    password,
):
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    async with async_session() as session:
        session.add(
            user_id=user_id,
            username=username,
            email=email,
            mb_phone=mb_phone,
            password=hashed_password,
        )
        await session.commit()
        result = await session.execute(select(User).filter_by(user_id=user_id))
        added_user = result.scalar()
        return added_user
