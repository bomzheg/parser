from dataclasses import dataclass

from sqlalchemy.ext.asyncio import AsyncSession


@dataclass
class HolderDao:
    session: AsyncSession

    async def commit(self):
        await self.session.commit()
