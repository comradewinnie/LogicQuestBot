from aiogram import F, Router
from aiogram.enums.parse_mode import ParseMode
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.filters import CommandStart
from aiogram.fsm.state import State, StatesGroup # импорт состояний
from aiogram.fsm.context import FSMContext

import app.keyboards as kb # дали короткое название
import app.database.requests as rq
import app.localization as local

router = Router()

class Register(StatesGroup): # создание класса с состояниями для регистрации
    language = State()
    grade = State()

class TaskState(StatesGroup):
    waiting_for_answer = State()  # Состояние ожидания ответа

class ChangeGrade(StatesGroup):
    waiting_for_change = State()

@router.message(CommandStart()) # должен ловить команду /start
async def cmd_start(message: Message, state: FSMContext = None): # приходит сообщение
    user = await rq.get_user(message.from_user.id)
    registered = await rq.is_registered(message.from_user.id)

    if registered:
        if state is not None:
            await state.clear()

        greetings_message = await local.get_text(user.language, "greetings")
        menu_keyboard = await kb.create_reply_keyboard(kb.MENU_SCHEME, user.language)
        await message.answer(greetings_message, parse_mode=ParseMode.HTML, reply_markup=menu_keyboard)
    else:
        await state.set_state(Register.language)
        await message.answer("Lūdzu, izvēlies valodu / Please, select language / Пожалуйста, выбери язык:", reply_markup=kb.languages)
        
@router.callback_query(Register.language, F.data.in_({"lang_lv", "lang_en", "lang_ru"}))
async def select_language(callback: CallbackQuery, state: FSMContext):
    await rq.set_user(callback.from_user.id, callback.from_user.first_name)

    selected_lang = callback.data.split("_")[1]  # получаем "en", "lv" или "ru"
    await rq.set_language(callback.from_user.id, selected_lang)  # сохраняем в БД

    if selected_lang == "en":
        confirmation_message = "English language selected"
    elif selected_lang == "lv":
        confirmation_message = "Izvēlētā latviešu valoda"
    elif selected_lang == "ru":
        confirmation_message = "Выбран русский язык"
    await callback.answer(confirmation_message)
    await state.clear()

    registered = await rq.is_registered(callback.from_user.id)

    if not registered:
        user = await rq.get_user(callback.from_user.id)
        welcome_message = await local.get_text(user.language, "welcome")
        registration_keyboard = await kb.create_inline_keyboard(kb.REGISTRATION_SCHEME, user.language)
        await callback.message.answer(welcome_message, parse_mode=ParseMode.HTML, reply_markup=registration_keyboard)
    else:
        user = await rq.get_user(callback.from_user.id)
        language_change_message = await local.get_text(user.language, "language_change")
        menu_keyboard = await kb.create_reply_keyboard(kb.MENU_SCHEME, user.language)
        await callback.message.answer(language_change_message, reply_markup=menu_keyboard)
    
@router.callback_query(F.data == "register")
async def register(callback: CallbackQuery, state: FSMContext): # передаём состояние
    registered = await rq.is_registered(callback.from_user.id)  # проверяем статус пользователя

    if registered:
        await callback.answer()  # просто закрываем callback без действий
        return  # ничего не делаем, если пользователь уже зарегистрирован
    
    await state.set_state(Register.grade) # устанавливаем состояние
    await callback.answer()

    user = await rq.get_user(callback.from_user.id)
    choose_grade_message = await local.get_text(user.language, "choose_grade")
    grades_keyboard = await kb.create_inline_keyboard(kb.GRADES_SCHEME, user.language)
    await callback.message.answer(choose_grade_message, reply_markup=grades_keyboard)

@router.callback_query(Register.grade, F.data == "grade7")
async def save_grade(callback: CallbackQuery, state: FSMContext):
    await state.update_data(grade=7)
    await callback.answer()
    data = await state.get_data()
    await rq.set_grade(callback.from_user.id,data["grade"])
    await state.clear()
    await rq.annulate_points_and_tasks(callback.from_user.id)

    user = await rq.get_user(callback.from_user.id)
    registration_completed_message = await local.get_text(user.language, "registration_completed")
    menu_keyboard = await kb.create_reply_keyboard(kb.MENU_SCHEME, user.language)
    await callback.message.answer(registration_completed_message, reply_markup=menu_keyboard)

@router.callback_query(Register.grade, F.data == "grade8")
async def save_grade(callback: CallbackQuery, state: FSMContext):
    await state.update_data(grade=8)
    await callback.answer()
    data = await state.get_data()
    await rq.set_grade(callback.from_user.id,data["grade"])
    await state.clear()
    await rq.annulate_points_and_tasks(callback.from_user.id)

    user = await rq.get_user(callback.from_user.id)
    registration_completed_message = await local.get_text(user.language, "registration_completed")
    menu_keyboard = await kb.create_reply_keyboard(kb.MENU_SCHEME, user.language)
    await callback.message.answer(registration_completed_message, reply_markup=menu_keyboard)

@router.callback_query(Register.grade, F.data == "grade9")
async def save_grade(callback: CallbackQuery, state: FSMContext):
    await state.update_data(grade=9)
    await callback.answer()
    data = await state.get_data()
    await rq.set_grade(callback.from_user.id,data["grade"])
    await state.clear()
    await rq.annulate_points_and_tasks(callback.from_user.id)

    user = await rq.get_user(callback.from_user.id)
    registration_completed_message = await local.get_text(user.language, "registration_completed")
    menu_keyboard = await kb.create_reply_keyboard(kb.MENU_SCHEME, user.language)
    await callback.message.answer(registration_completed_message, reply_markup=menu_keyboard)

@router.message(F.text.in_(["\U0001F464 Mans profils", "\U0001F464 My profile", "\U0001F464 Мой профиль"]))
async def show_profile(message: Message):
    user = await rq.get_user(message.from_user.id)  # получаем пользователя из базы данных

    if user and user.is_registered == 1:
        profile_info_message = await local.get_text(user.language, "profile_info")
        profile_info_message = profile_info_message.format(user=user)
        profile_keyboard = await kb.create_reply_keyboard(kb.PROFILE_SCHEME, user.language)
        await message.answer(profile_info_message, parse_mode=ParseMode.HTML, reply_markup=profile_keyboard)
    else:
        await message.answer("Profils nav atrasts. Lūdzu, reģistrējies, lai turpinātu.\nProfile not found. Please register to continue.\nПрофиль не найден. Пожалуйста, зарегистрируйся, чтобы продолжить.", parse_mode=ParseMode.HTML, reply_markup=ReplyKeyboardRemove()) # если пользователя нет в базе данных

@router.message(F.text.in_(["\u25C0\uFE0F Uz sākumu", "\u25C0\uFE0F Home", "\u25C0\uFE0F В начало"]))
async def go_on_homepage(message: Message):
    await cmd_start(message)
    
@router.message(F.text.in_(["\U0001F3EB Izmainīt klasi", "\U0001F3EB Change grade", "\U0001F3EB Сменить класс"]))
async def change_grade_warning(message: Message, state: FSMContext):
    await state.set_state(ChangeGrade.waiting_for_change)
    user = await rq.get_user(message.from_user.id)

    if user and user.is_registered == 1:
        grade_change_warning_message = await local.get_text(user.language, "grade_change_warning")
        confirmation_keyboard = await kb.create_reply_keyboard(kb.CONFIRMATION_SCHEME, user.language)
        await message.answer(grade_change_warning_message, reply_markup=confirmation_keyboard)
    else:
        await message.answer("Profils nav atrasts. Lūdzu, reģistrējies, lai turpinātu.\nProfile not found. Please register to continue.\nПрофиль не найден. Пожалуйста, зарегистрируйся, чтобы продолжить.", parse_mode=ParseMode.HTML, reply_markup=ReplyKeyboardRemove())

@router.message(F.text.in_(["\u2705 Jā", "\u2705 Yes", "\u2705 Да"]), ChangeGrade.waiting_for_change)
async def change_grade(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(Register.grade) # устанавливаем состояние
    user = await rq.get_user(message.from_user.id)

    choose_grade_message = await local.get_text(user.language, "choose_grade")
    grades_keyboard = await kb.create_inline_keyboard(kb.GRADES_SCHEME, user.language)
    await message.answer(choose_grade_message, reply_markup=grades_keyboard)

@router.message(F.text.in_(["\u274C Nē", "\u274C No", "\u274C Нет"]), ChangeGrade.waiting_for_change)
async def not_change_grade(message: Message, state: FSMContext):
    await state.clear()
    await show_profile(message)

@router.message(F.text.in_(["\U0001F31F TOP", "\U0001F31F Leaderboard", "\U0001F31F ТОП"]))
async def show_leaderboard(message: Message):
    user = await rq.get_user(message.from_user.id)
    
    if user and user.is_registered == 1:
        leaderboard, user_position = await rq.get_leaderboard(message.from_user.id)

        points_text = await local.get_text(user.language, "points_text")
        grade_text = await local.get_text(user.language, "grade_text")
        leaderboard_title = await local.get_text(user.language, "leaderboard_title")
        leaderboard_your_place = await local.get_text(user.language, "leaderboard_your_place")
        leaderboard_your_place = leaderboard_your_place.format(user_position=user_position)
        leaderboard_error = await local.get_text(user.language, "leaderboard_error")

        if leaderboard:
            # формируем текст для рейтинга
            leaderboard_text = leaderboard_title
            for i, (tg_name, grade, points) in enumerate(leaderboard, start=1):
                leaderboard_text += f"{i}. {tg_name} [{grade}{grade_text}] — {points} {points_text}.\n"
            # добавляем строку с местом пользователя
            if user_position:
                leaderboard_text += leaderboard_your_place
        else:
            leaderboard_text = leaderboard_error
        
        back_keyboard = await kb.create_reply_keyboard(kb.BACK_SCHEME, user.language)
        await message.answer(leaderboard_text, parse_mode=ParseMode.HTML, reply_markup=back_keyboard)
    else:
        await message.answer("Profils nav atrasts. Lūdzu, reģistrējies, lai turpinātu.\nProfile not found. Please register to continue.\nПрофиль не найден. Пожалуйста, зарегистрируйся, чтобы продолжить.", parse_mode=ParseMode.HTML, reply_markup=ReplyKeyboardRemove())

@router.message(F.text.in_(["\U0001F310 Izmainīt valodu", "\U0001F310 Change language", "\U0001F310 Сменить язык"]))
async def change_language(message: Message, state: FSMContext):
    await state.set_state(Register.language)
    await message.answer("Lūdzu, izvēlies valodu / Please, select language / Пожалуйста, выбери язык:", reply_markup=kb.languages)

@router.message(F.text.in_(["\U0001F6E0 Tehniskais atbalsts", "\U0001F6E0 Technical support", "\U0001F6E0 Техническая поддержка"]))
async def technical_support(message: Message):
    user = await rq.get_user(message.from_user.id)
    if user and user.is_registered == 1:
        technical_support_message = await local.get_text(user.language, "technical_support_message")
        await message.answer(technical_support_message, parse_mode=ParseMode.HTML)
    else:
        await message.answer("Profils nav atrasts. Lūdzu, reģistrējies, lai turpinātu.\nProfile not found. Please register to continue.\nПрофиль не найден. Пожалуйста, зарегистрируйся, чтобы продолжить.", parse_mode=ParseMode.HTML, reply_markup=ReplyKeyboardRemove())

@router.message(F.text.in_(["\U0001F514 Ieslēgt/izslēgt ikdienas atgādinājumus", "\U0001F514 Toggle daily reminders", "\U0001F514 Вкл./выкл. ежедневные напоминания"]))
async def toggle_daily_reminder(message: Message):
    user = await rq.get_user(message.from_user.id)
    if user and user.is_registered == 1 and user.is_reminder_enabled == 1:
        await rq.disable_daily_reminders(message.from_user.id)
        reminder_disabled_message = await local.get_text(user.language, "reminder_disabled")
        await message.answer(reminder_disabled_message, parse_mode=ParseMode.HTML)
    elif user and user.is_registered == 1 and user.is_reminder_enabled == 0:
        await rq.enable_daily_reminders(message.from_user.id)
        reminder_enabled_message = await local.get_text(user.language, "reminder_enabled")
        await message.answer(reminder_enabled_message, parse_mode=ParseMode.HTML)
    else:
        await message.answer("Profils nav atrasts. Lūdzu, reģistrējies, lai turpinātu.\nProfile not found. Please register to continue.\nПрофиль не найден. Пожалуйста, зарегистрируйся, чтобы продолжить.", parse_mode=ParseMode.HTML, reply_markup=ReplyKeyboardRemove())

@router.callback_query(F.data == "turn_off_reminder")
async def turn_off_reminder(callback: CallbackQuery):
    user = await rq.get_user(callback.from_user.id)
    if user.is_reminder_enabled == 1:
        await rq.disable_daily_reminders(callback.from_user.id)
        reminder_disabled_message = await local.get_text(user.language, "reminder_disabled")
        await callback.answer(reminder_disabled_message, parse_mode=ParseMode.HTML)

@router.message(F.text.in_(["\u270F\uFE0F Sākt uzdevumu", "\u270F\uFE0F Start the task", "\u270F\uFE0F Начать задание"]))
async def start_task(message: Message, state: FSMContext):
    user = await rq.get_user(message.from_user.id)

    if user and user.is_registered == 1:
        task = await rq.get_random_uncompleted_task_for_user(user.id, user.grade)  # получаем случайную задачу по классу

        if task:
            await rq.set_current_task(user.id, task.id)
            await state.set_state(TaskState.waiting_for_answer)
            # формируем сообщение с текстом задания
            if user.language == "lv":
                task_text = task.text_lv
            if user.language == "en":
                task_text = task.text_en
            if user.language == "ru":
                task_text = task.text_ru
            task_info_message = await local.get_text(user.language, "task_info")
            task_info_message = task_info_message.format(task_text=task_text, task=task)
            answer_keyboard = await kb.create_reply_keyboard(kb.ANSWER_SCHEME, user.language)

            if task.input_type == "multiple_choice":
                task_choices = getattr(task, f"choices_{user.language}", [])
                multiple_choice_keyboard = await kb.create_multiple_choice_keyboard(task_choices)
                choose_answer_message = await local.get_text(user.language, "choose_answer")
                await message.answer(task_info_message, parse_mode=ParseMode.HTML, reply_markup=multiple_choice_keyboard)
                await message.answer(choose_answer_message, reply_markup=answer_keyboard)

            if task.input_type == "text":
                await message.answer(task_info_message, parse_mode=ParseMode.HTML, reply_markup=answer_keyboard)  # Отправляем текст задания
        else:
            task_not_found_message = await local.get_text(user.language, "task_not_found")
            await message.answer(task_not_found_message, parse_mode=ParseMode.HTML)
            await state.clear()
    else:
        await message.answer("Lūdzu, reģistrējies, lai sāktu risināt uzdevumus.\nPlease register to start solving tasks.\nПожалуйста, зарегистрируйся, чтобы начать выполнять задания.", parse_mode=ParseMode.HTML, reply_markup=ReplyKeyboardRemove())
        await state.clear()

@router.message(TaskState.waiting_for_answer, F.text.in_(["\u274C Atcelt", "\u274C Cancel", "\u274C Отменить"]))
async def cancel_task(message: Message, state: FSMContext):
    await rq.clear_current_task(message.from_user.id)
    await state.clear()
    await cmd_start(message)

@router.message(TaskState.waiting_for_answer)
async def handle_answer(message: Message, state: FSMContext):
    user = await rq.get_user(message.from_user.id)
    if user and user.current_task_id:
        # получаем текущее задание
        task = await rq.get_task_by_id(user.current_task_id)

        if task:
            if task.input_type == "text":
                # проверяем правильность ответа
                if user.language == "lv":
                    task_answer = task.answer_lv
                if user.language == "en":
                    task_answer = task.answer_en
                if user.language == "ru":
                    task_answer = task.answer_ru

                if message.text.strip().lower() == task_answer.strip().lower():
                    # если ответ правильный
                    await rq.increment_user_points(user.tg_id, task.points)  # начисляем очки
                    await rq.clear_current_task(user.tg_id)  # очищаем текущее задание
                    await rq.add_completed_task(user.id, task.id, 1)
                    await state.clear()
                    correct_answer_message = await local.get_text(user.language, "correct_answer")
                    correct_answer_message = correct_answer_message.format(task=task)
                    menu_keyboard = await kb.create_reply_keyboard(kb.MENU_SCHEME, user.language)
                    await message.answer(correct_answer_message, reply_markup=menu_keyboard)
                else:
                    # если ответ неправильный
                    await rq.clear_current_task(user.tg_id)  # очищаем текущее задание
                    await rq.add_completed_task(user.id, task.id, 0)  # отмечаем задание как завершённое
                    await rq.set_last_task_completed_date_for_incorrect_answer(user.tg_id)
                    await state.clear()
                    incorrect_answer_message = await local.get_text(user.language, "incorrect_answer")
                    incorrect_answer_message = incorrect_answer_message.format(task_answer=task_answer)
                    menu_keyboard = await kb.create_reply_keyboard(kb.MENU_SCHEME, user.language)
                    await message.answer(incorrect_answer_message, parse_mode=ParseMode.HTML, reply_markup=menu_keyboard)

@router.callback_query(TaskState.waiting_for_answer)
async def handle_multiple_choice(callback: CallbackQuery, state: FSMContext):
    user = await rq.get_user(callback.from_user.id)
    if user and user.current_task_id:
        task = await rq.get_task_by_id(user.current_task_id)

        if task:
            if task.input_type == "multiple_choice":
                if user.language == "lv":
                    task_answer = task.answer_lv
                if user.language == "en":
                    task_answer = task.answer_en
                if user.language == "ru":
                    task_answer = task.answer_ru

                if callback.data.strip().lower() == task_answer.strip().lower():
                    await rq.increment_user_points(user.tg_id, task.points)
                    await rq.clear_current_task(user.tg_id)
                    await rq.add_completed_task(user.id, task.id, 1)
                    await state.clear()
                    correct_answer_message = await local.get_text(user.language, "correct_answer")
                    correct_answer_message = correct_answer_message.format(task=task)
                    menu_keyboard = await kb.create_reply_keyboard(kb.MENU_SCHEME, user.language)
                    await callback.message.answer(correct_answer_message, reply_markup=menu_keyboard)
                    await callback.answer()
                else:
                    await rq.clear_current_task(user.tg_id)
                    await rq.add_completed_task(user.id, task.id, 0)
                    await rq.set_last_task_completed_date_for_incorrect_answer(user.tg_id)
                    await state.clear()
                    incorrect_answer_message = await local.get_text(user.language, "incorrect_answer")
                    incorrect_answer_message = incorrect_answer_message.format(task_answer=task_answer)
                    menu_keyboard = await kb.create_reply_keyboard(kb.MENU_SCHEME, user.language)
                    await callback.message.answer(incorrect_answer_message, parse_mode=ParseMode.HTML, reply_markup=menu_keyboard)
                    await callback.answer()

@router.message()
async def fallback_message(message: Message, state: FSMContext):
    current_state = await state.get_state() # проверяем текущее состояние пользователя
    if current_state is None: # сообщение, если пользователь не в состоянии ожидания ответа
        user = await rq.get_user(message.from_user.id)
        unexpected_input_message = await local.get_text(user.language, "unexpected_input")
        await message.answer(unexpected_input_message)