from sqlalchemy import BigInteger, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from sqlalchemy.dialects.postgresql import JSON
from datetime import date

engine = create_async_engine(url='sqlite+aiosqlite:///db.sqlite3') # создали БД

async_session = async_sessionmaker(engine) # подключение к БД

class Base(AsyncAttrs, DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger) # ид тг - это уже бигинтеджер
    tg_name: Mapped[str] = mapped_column(String(250))
    grade: Mapped[int] = mapped_column(nullable=True)
    is_registered: Mapped[bool] = mapped_column(default=False)
    completed_task_count: Mapped[int] = mapped_column(default=0)
    earned_points: Mapped[int] = mapped_column(default=0)
    current_task_id: Mapped[int] = mapped_column(nullable=True)
    last_task_completed_date: Mapped[date] = mapped_column(nullable=True)
    language: Mapped[str] = mapped_column(String(10), default="lv")
    is_reminder_enabled: Mapped[bool] = mapped_column(default=1)

    completed_tasks = relationship("CompletedTask", back_populates="user")  # связи

class Task(Base):
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(primary_key=True)
    grade: Mapped[int] = mapped_column()
    input_type: Mapped[str] = mapped_column(String(25))

    text_lv: Mapped[str] = mapped_column(String(1500))
    answer_lv: Mapped[str] = mapped_column(String(100))
    choices_lv: Mapped[list[str]] = mapped_column(JSON, nullable=True) 

    text_en: Mapped[str] = mapped_column(String(1500))
    answer_en: Mapped[str] = mapped_column(String(100))
    choices_en: Mapped[list[str]] = mapped_column(JSON, nullable=True)
                                           
    text_ru: Mapped[str] = mapped_column(String(1500))
    answer_ru: Mapped[str] = mapped_column(String(100))
    choices_ru: Mapped[list[str]] = mapped_column(JSON, nullable=True)

    points: Mapped[int] = mapped_column()

class CompletedTask(Base):
    __tablename__ = "completed_tasks"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    task_id: Mapped[int] = mapped_column(ForeignKey("tasks.id"))
    was_correct: Mapped[bool] = mapped_column()

    user = relationship("User", back_populates="completed_tasks") # связи
    task = relationship("Task")

async def async_main():  # запуск синхронизации
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)