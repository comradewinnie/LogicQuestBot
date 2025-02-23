from sqlalchemy import select, func, and_
from app.database.models import async_session
from app.database.models import User, Task, CompletedTask
from sqlalchemy import select
from datetime import date

async def set_user(tg_id, tg_name): # функция для добавления пользователя в БД
    async with async_session() as session:  # открываем сессию
        user = await session.scalar(select(User).where(User.tg_id == tg_id)) # поиск tg_id в БД

        if not user: # если не найдено
            session.add(User(tg_id=tg_id, tg_name=tg_name, is_registered=False)) # добавляем tg_id в БД
            await session.commit() # завершаем сессию

async def is_registered(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        return user.is_registered if user else False

async def set_grade(tg_id, grade):
    async with async_session() as session: 
        result = await session.execute(select(User).where(User.tg_id == tg_id)) # ищем в БД строчки с таким же tg_id
        user = result.scalars().first() # фиксируем эту строчку
        user.grade = grade  # обновляем поле grade
        user.is_registered = True
        await session.commit()
        
async def get_user(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        return user
    
async def add_task(grade: int, input_type: str, text_lv: str, text_en: str, text_ru: str, answer_lv: str, answer_en: str, answer_ru: str, choices_lv: list[str], choices_en: list[str], choices_ru: list[str], points: int):
    async with async_session() as session:
        task = Task(
            grade=grade,
            input_type=input_type,
            text_lv=text_lv,
            text_en=text_en,
            text_ru=text_ru,
            answer_lv=answer_lv,
            answer_en=answer_en,
            answer_ru=answer_ru,
            choices_lv=choices_lv,
            choices_en=choices_en,
            choices_ru=choices_ru,
            points=points
        )
        session.add(task)  # добавляем задачу в сессию
        await session.commit()

async def get_random_uncompleted_task_for_user(user_id, grade):
    async with async_session() as session:
        completed_task_ids = select(CompletedTask.task_id).where(CompletedTask.user_id == user_id) # находим все задания, которые выполнены пользователем
        
        task = await session.execute(   # выбираем случайное задание среди невыполненных
            select(Task)
            .where(and_(Task.grade == grade, ~Task.id.in_(completed_task_ids)))
            .order_by(func.random())  # случайный порядок
            .limit(1)  # берём одно случайное задание
        )
        
        return task.scalars().first()

async def set_current_task(user_id, task_id):   # при старте задания устанавливаем его ИД в пользователя
    async with async_session() as session:
        user = await session.get(User, user_id)
        user.current_task_id = task_id
        await session.commit()
   
async def get_task_by_id(task_id: int):
    async with async_session() as session:
        result = await session.execute(select(Task).where(Task.id == task_id))
        task = result.scalar_one_or_none()
        return task
    
async def increment_user_points(tg_id: int, points: int): # увеличиваем очки пользователя и счётчик выполненных заданий
    async with async_session() as session:
        result = await session.execute(select(User).where(User.tg_id == tg_id))
        user = result.scalar_one_or_none()
        if user:
            user.earned_points += points
            user.completed_task_count += 1
            user.last_task_completed_date = date.today()
            await session.commit()

async def set_last_task_completed_date_for_incorrect_answer(tg_id: int):
    async with async_session() as session:
        result = await session.execute(select(User).where(User.tg_id == tg_id))
        user = result.scalar_one_or_none()
        if user:
            user.last_task_completed_date = date.today()
            await session.commit()

async def clear_current_task(tg_id: int): # очищаем статус текущего задания
    async with async_session() as session:
        result = await session.execute(select(User).where(User.tg_id == tg_id))
        user = result.scalar_one_or_none()
        if user:
            user.current_task_id = None
            await session.commit()

async def is_task_completed(user_id, task_id):
    async with async_session() as session:
        result = await session.execute(select(CompletedTask).where(CompletedTask.user_id == user_id, CompletedTask.task_id == task_id))
        return result.scalar() is not None
    
async def add_completed_task(user_id, task_id, was_correct):
    async with async_session() as session:
        completed_task = CompletedTask(user_id=user_id, task_id=task_id, was_correct=was_correct)
        session.add(completed_task)
        await session.commit()

async def annulate_points_and_tasks(tg_id: int):
    async with async_session() as session:
        result = await session.execute(select(User).where(User.tg_id == tg_id))
        user = result.scalar_one_or_none()
        if user:
            user.earned_points = 0
            user.completed_task_count = 0
            await session.commit()

async def get_leaderboard(user_id, limit=10):
    async with async_session() as session:
        result = await session.execute(
            select(User.tg_name, User.grade, User.earned_points) 
            .where(and_(User.is_registered == True, User.earned_points > 0)) # получаем список пользователей с очками > 0
            .order_by(User.earned_points.desc()) # отсортированный по количеству очков
            .limit(limit)
        )
        leaderboard = result.all()

        user_position = None # оределяем позицию текущего пользователя, если он есть в таблице лидеров
        if user_id:
            user_rank_query = await session.execute(
                select(User)
                .where(User.earned_points > 0)
                .order_by(User.earned_points.desc())
            )
            all_users_sorted = user_rank_query.scalars().all()
            for idx, user in enumerate(all_users_sorted, start=1):
                if user.tg_id == user_id:
                    user_position = idx
                    break
        
    return leaderboard, user_position

async def get_inactive_users():
    async with async_session() as session:
        today = date.today()
        result = await session.execute(
            select(User).where(and_(User.is_registered == True, User.last_task_completed_date != today)) # находим пользователей, не выполнявших задание сегодня
        )
        return result.scalars().all()

async def set_language(tg_id: int, language: str):
    async with async_session() as session:
        result = await session.execute(select(User).where(User.tg_id == tg_id))
        user = result.scalars().first()
        if user:
            user.language = language
            await session.commit()

async def disable_daily_reminders(tg_id):
    async with async_session() as session:
        result = await session.execute(select(User).where(User.tg_id == tg_id))
        user = result.scalars().first()
        if user:
            user.is_reminder_enabled = 0
            await session.commit()

async def enable_daily_reminders(tg_id):
    async with async_session() as session:
        result = await session.execute(select(User).where(User.tg_id == tg_id))
        user = result.scalars().first()
        if user:
            user.is_reminder_enabled = 1
            await session.commit()