from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from config.settings import Settings, env


class DBManager:
    __slots__ = ("engine", "session_maker")

    def __init__(self, settings: Settings) -> None:
        self.engine: AsyncEngine = create_async_engine(
            url=settings.DB_URL,
            echo=settings.DEBUG,
            pool_pre_ping=True,
            pool_recycle=300,
            max_overflow=10,
        )

        self.session_maker: async_sessionmaker[AsyncSession] = (
            async_sessionmaker(
                self.engine, class_=AsyncSession, expire_on_commit=False
            )
        )


manager = DBManager(env)
