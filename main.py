from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message

BOT_TOKEN = ''

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# начать квест
@dp.message(Command(commands=["start"]))
async def start(message: types.Message):
    await message.answer("Вы отправились на поиски забытой пещеры, о которой слышали много легенд. "
                         "По пути вы встречаете различных персонажей из игры Genshin Impact, "
                         "которые могут помочь или помешать вам в поисках.",
                         reply_markup=types.ReplyKeyboardMarkup(
                             keyboard=[
                                 [
                                     types.KeyboardButton(text="Я готов к приключениям и хочу начать!"),
                                     types.KeyboardButton(text="Я хочу отказаться от квеста и пройти его позднее")
                                 ]
                             ],
                             resize_keyboard=True
                         ))


# выход из квеста
@dp.message(lambda message: message.text == "Я хочу отказаться от квеста и пройти его позднее")
async def run_away(message: types.Message):
    await message.answer("До скорой встречи, Путешественник) Надеюсь, что мы еще увидимся."
                         "\nНажмите /start, чтобы начать квест"
                         "\nНажмите /help, чтобы понять, что происходит",
                         reply_markup=types.ReplyKeyboardRemove())


# начало квеста, выбор 1
@dp.message(lambda message: message.text == "Я готов к приключениям и хочу начать!")
async def go_left(message: types.Message):
    await message.answer("Вы видите перед собой Сяо, который предлагает вам присоединиться к его группе "
                         "исследователей. Они могут рассказать вам о скоровищах спрятанных внутри.",
                         reply_markup=types.ReplyKeyboardMarkup(
                             keyboard=[
                                 [
                                     # выбор 2
                                     types.KeyboardButton(text="Присоединиться к группе"),
                                     # выбор 3
                                     types.KeyboardButton(text="Отказаться и идти самостоятельно")
                                 ]
                             ],
                             resize_keyboard=True
                         ))


# выбор 2
@dp.message(lambda message: message.text == "Присоединиться к группе")
async def go_left(message: types.Message):
    await message.answer("Сяо говорит, что внутри пещеры находится артефакт, потерянный когда-то архонтами. "
                         "Вместе с группой вы находите вход в пещеру, но перед вами возникает выбор:",
                         reply_markup=types.ReplyKeyboardMarkup(
                             keyboard=[
                                 [
                                     # выбор 4
                                     types.KeyboardButton(text="Идти вперед по карте Сяо"),
                                     # выбор 5
                                     types.KeyboardButton(text="Исследовать боковые коридоры")
                                 ]
                             ],
                             resize_keyboard=True
                         ))


# выбор 3
@dp.message(lambda message: message.text == "Отказаться и идти самостоятельно")
async def go_left(message: types.Message):
    await message.answer("Идя самостоятельно, вы сталкиваетесь с Чичи (Ци ци), которая предлагает вам помощь "
                         "в обмен на часть найденного сокровища и обнимашки. ",
                         reply_markup=types.ReplyKeyboardMarkup(
                             keyboard=[
                                 [
                                     # выбор 6
                                     types.KeyboardButton(text="Принять предложение"),
                                     # выбор 7
                                     types.KeyboardButton(text="Отказаться")
                                 ]
                             ],
                             resize_keyboard=True
                         ))


# выбор 4
@dp.message(lambda message: message.text == "Идти вперед по карте Сяо")
async def go_left(message: types.Message):
    await message.answer("Вы и ваша группа приближаетесь к сундуку, в тени которого лежит странный предмет, "
                         "но замечаете, что пещера охраняется монстрами.",
                         reply_markup=types.ReplyKeyboardMarkup(
                             keyboard=[
                                 [
                                     # выбор 8
                                     types.KeyboardButton(text="Сразиться с ними"),
                                     # выбор 9
                                     types.KeyboardButton(text="Попытаться обойти")
                                 ]
                             ],
                             resize_keyboard=True
                         ))


# выбор 5
@dp.message(lambda message: message.text == "Исследовать боковые коридоры")
async def go_left(message: types.Message):
    await message.answer("Исследуя темные боковые коридоры пещеры, именно вы находите древний артефакт, который "
                         "может быть ключом к разгадке тайны пещеры.",
                         reply_markup=types.ReplyKeyboardMarkup(
                             keyboard=[
                                 [
                                     # выбор 10
                                     types.KeyboardButton(text="Взять его с собой"),
                                     # выбор 11
                                     types.KeyboardButton(text="Оставить на месте")
                                 ]
                             ],
                             resize_keyboard=True
                         ))


# выбор 6
@dp.message(lambda message: message.text == "Принять предложение")
async def go_left(message: types.Message):
    await message.answer("Приняв предложение Чичи (Ци Ци), вы приближаетесь к ней, чтобы забрать оружие, которое"
                         " она вам протягивает. В её поведении вы замечаете что-то странное и делаете шаг назад. "
                         "Она набрасывается на вас.",
                         reply_markup=types.ReplyKeyboardMarkup(
                             keyboard=[
                                 [
                                     # выбор 12
                                     types.KeyboardButton(text="Сразиться с ней"),
                                     # выбор 13
                                     types.KeyboardButton(text="Убежать")
                                 ]
                             ],
                             resize_keyboard=True
                         ))


# выбор 7
@dp.message(lambda message: message.text == "Отказаться")
async def go_left(message: types.Message):
    await message.answer("Отказавшись от предложения Чичи (Ци Ци), вы идете дальше одни и сталкиваетесь "
                         "с опасными ловушками.",
                         reply_markup=types.ReplyKeyboardMarkup(
                             keyboard=[
                                 [
                                     # выбор 14
                                     types.KeyboardButton(text="Попытаться преодолеть их"),
                                     # выбор 15
                                     types.KeyboardButton(text="Вернуться назад")
                                 ]
                             ],
                             resize_keyboard=True
                         ))


# выбор 8
@dp.message(lambda message: message.text == "Сразиться с ними")
async def go_left(message: types.Message):
    await message.answer("После сражения с монстрами вы находите сокровище, но оно оказывается защищено заклятием.",
                         reply_markup=types.ReplyKeyboardMarkup(
                             keyboard=[
                                 [
                                     # выбор 16
                                     types.KeyboardButton(text="Попытаться избежать заклятия"),
                                     # выбор 17
                                     types.KeyboardButton(text="Активировать его ради сокровища")
                                 ]
                             ],
                             resize_keyboard=True
                         ))


# выбор 9
@dp.message(lambda message: message.text == "Попытаться обойти")
async def go_left(message: types.Message):
    await message.answer("Пока группа сражается с монстрами, вы обходите их и находите артефакт, а также вам "
                         "удается забрать часть сокровищ. Перед вами возникает выбор:",
                         reply_markup=types.ReplyKeyboardMarkup(
                             keyboard=[
                                 [
                                     # выбор 18
                                     types.KeyboardButton(text="Забрать всё себе"),
                                     # выбор 19
                                     types.KeyboardButton(text="Забрать и вернуться к группе")
                                 ]
                             ],
                             resize_keyboard=True
                         ))


# выбор 10
@dp.message(lambda message: message.text == "Взять его с собой")
async def go_left(message: types.Message):
    await message.answer("Взяв артефакт, вы обнаруживаете, что он привлекает монстров.",
                         reply_markup=types.ReplyKeyboardMarkup(
                             keyboard=[
                                 [
                                     # выбор 21
                                     types.KeyboardButton(text="Бежать с артефактом"),
                                     # выбор 22
                                     types.KeyboardButton(text="Попытаться использовать артефакт против врагов")
                                 ]
                             ],
                             resize_keyboard=True
                         ))


# выбор 11
@dp.message(lambda message: message.text == "Оставить на месте")
async def go_left(message: types.Message):
    await message.answer("Оставив артефакт на месте, вы продолжаете свой путь, но встречаете Чичу (Ци Ци), "
                         "которая, в отличие от вас, забрала артефакт.",
                         reply_markup=types.ReplyKeyboardMarkup(
                             keyboard=[
                                 [
                                     # выбор 23
                                     types.KeyboardButton(text="Попытаться забрать артефакт себе"),
                                     # выбор 24
                                     types.KeyboardButton(text="Уйти, чтобы избежать конфликта")
                                 ]
                             ],
                             resize_keyboard=True
                         ))


# выбор 12
@dp.message(lambda message: message.text == "Сразиться с ней")
async def go_left(message: types.Message):
    await message.answer("В результате схватки с Чичей (Ци Ци) вы побеждаете её, но теперь перед вами стоит выбор,"
                         "что делать с артефактом:",
                         reply_markup=types.ReplyKeyboardMarkup(
                             keyboard=[
                                 [
                                     # выбор 18
                                     types.KeyboardButton(text="Забрать всё себе"),
                                     # выбор 19
                                     types.KeyboardButton(text="Забрать и вернуться к группе")
                                 ]
                             ],
                             resize_keyboard=True
                         ))


# выбор 13
@dp.message(lambda message: message.text == "Убежать")
async def go_left(message: types.Message):
    await message.answer("Убежав от Чичи (Ци Ци), вы продолжаете свой путь, но сталкиваетесь с ловушками.",
                         reply_markup=types.ReplyKeyboardMarkup(
                             keyboard=[
                                 [
                                     # выбор 14
                                     types.KeyboardButton(text="Попытаться преодолеть их"),
                                     # выбор 15
                                     types.KeyboardButton(text="Вернуться назад")
                                 ]
                             ],
                             resize_keyboard=True
                         ))


# выбор 14
@dp.message(lambda message: message.text == "Попытаться преодолеть их")
async def go_left(message: types.Message):
    await message.answer("Преодолев ловушки, вы находите цель своего путешествия, но перед вами возникает"
                         " выбор, что делать с артефактом:",
                         reply_markup=types.ReplyKeyboardMarkup(
                             keyboard=[
                                 [
                                     # выбор 18
                                     types.KeyboardButton(text="Забрать всё себе"),
                                     # выбор 19
                                     types.KeyboardButton(text="Забрать и вернуться к группе")
                                 ]
                             ],
                             resize_keyboard=True
                         ))


# выбор 15
@dp.message(lambda message: message.text == "Вернуться назад")
async def go_left(message: types.Message):
    await message.answer("Вернувшись назад, вы обнаруживаете, что Чича (Ци Ци) оказалась вашим союзником и помогает"
                         " вам пройти через опасности.",
                         reply_markup=types.ReplyKeyboardMarkup(
                             keyboard=[
                                 [
                                     # выбор 25
                                     types.KeyboardButton(text="Продолжить путь вместе с ней"),
                                     # выбор 26
                                     types.KeyboardButton(text="Продолжить свой путь в одиночестве")
                                 ]
                             ],
                             resize_keyboard=True
                         ))


# выбор 16
@dp.message(lambda message: message.text == "Попытаться избежать заклятия")
async def go_left(message: types.Message):
    await message.answer("Избежав ловушки, вы достаёте артефакт, но перемещаетесь в окружение монстров.",
                         reply_markup=types.ReplyKeyboardMarkup(
                             keyboard=[
                                 [
                                     # выбор 27
                                     types.KeyboardButton(text="Сразиться с врагами"),
                                     # выбор 28
                                     types.KeyboardButton(text="Попытаться убежать")
                                 ]
                             ],
                             resize_keyboard=True
                         ))


# выбор 17
@dp.message(lambda message: message.text == "Активировать его ради сокровища")
async def go_left(message: types.Message):
    await message.answer("Активировав ловушку, вы сталкиваетесь со странным дымом, но отмахиваетесь от него и "
                         "получаете артефакт и сокровище.",
                         reply_markup=types.ReplyKeyboardMarkup(
                             keyboard=[
                                 [
                                     # выбор 18
                                     types.KeyboardButton(text="Забрать всё себе"),
                                     # выбор 19
                                     types.KeyboardButton(text="Забрать и вернуться к группе")
                                 ]
                             ],
                             resize_keyboard=True
                         ))


# выбор 18
@dp.message(lambda message: message.text == "Забрать всё себе")
async def go_left(message: types.Message):
    await message.answer("Получив артефакт, вы чувствуете удовлетворение, но тут же перед вами возникает новая "
                         "проблема: как его использовать?",
                         reply_markup=types.ReplyKeyboardMarkup(
                             keyboard=[
                                 [
                                     # выбор 29
                                     types.KeyboardButton(text="Решить этот вопрос самостоятельно"),
                                     # выбор 30
                                     types.KeyboardButton(text="Вернуться домой и посоветоваться с Чжун Ли")
                                 ]
                             ],
                             resize_keyboard=True
                         ))


# выбор 19
@dp.message(lambda message: message.text == "Забрать и вернуться к группе")
async def go_left(message: types.Message):
    await message.answer("Вы возвращаетесь к группе, но они не прошли все припятствия вместе с вами. "
                         "Стоит ли с ними делиться сокровищами и показать им артефакт?",
                         reply_markup=types.ReplyKeyboardMarkup(
                             keyboard=[
                                 [
                                     # выбор 31
                                     types.KeyboardButton(text="Поделиться сокровищами с группой"),
                                     # выбор 20
                                     types.KeyboardButton(text="Пойти к выходу из пещеры одному, пряча артефакт")
                                 ]
                             ],
                             resize_keyboard=True
                         ))


# концовка 20
@dp.message(lambda message: message.text == "Пойти к выходу из пещеры одному, пряча артефакт")
async def fight_dragon(message: types.Message):
    await message.answer("Разозленный Сяо вместе с группой нападает на Вас, пытаясь похитить сокровище. Истощенные "
                         "поиском сокровищ вы проигрываете эту битву, но они не находят у Вас ничего ценного и уходят."
                         "\nПоздравляю вас, маленький жадный и эгоистичный говнюк, вы заслужили свой темный артефакт."
                         "\nУдачи в следующих приключениях!"
                         "\n"
                         "\nP.S. Если хотите пройти квест еще раз - введите /start",
                         reply_markup=types.ReplyKeyboardRemove())


# выбор 21
@dp.message(lambda message: message.text == "Бежать с артефактом")
async def go_left(message: types.Message):
    await message.answer("Бежа от монстров с артефактом, вы случайно активируете его способности и получаете"
                         " его благословение. Монстры теряют вас.",
                         reply_markup=types.ReplyKeyboardMarkup(
                             keyboard=[
                                 [
                                     # выбор 19
                                     types.KeyboardButton(text="Забрать и вернуться к группе"),
                                     # выбор 32
                                     types.KeyboardButton(text="Убить всю группу и переместиться с артефактом подальше"
                                                               " от пещеры")
                                 ]
                             ],
                             resize_keyboard=True
                         ))


# выбор 22
@dp.message(lambda message: message.text == "Попытаться использовать артефакт против врагов")
async def go_left(message: types.Message):
    await message.answer("Используя артефакт против монстров, вы одерживаете победу, но теперь перед вами "
                         "возникает выбор: использовать его дальше или вернуть на место?",
                         reply_markup=types.ReplyKeyboardMarkup(
                             keyboard=[
                                 [
                                     # выбор 33
                                     types.KeyboardButton(text="Продолжить использование"),
                                     # выбор 34
                                     types.KeyboardButton(text="Вернуть на место")
                                 ]
                             ],
                             resize_keyboard=True
                         ))


# выбор 23
@dp.message(lambda message: message.text == "Попытаться забрать артефакт себе")
async def go_left(message: types.Message):
    await message.answer("Забирая артефакт у Чичи (Ци Ци), вы обнаруживаете, что она находится под заклятием.",
                         reply_markup=types.ReplyKeyboardMarkup(
                             keyboard=[
                                 [
                                     # выбор 35
                                     types.KeyboardButton(text="Рискнуть и сразиться с ней"),
                                     # выбор 36
                                     types.KeyboardButton(text="Обнять её и бежать со всех ног")
                                 ]
                             ],
                             resize_keyboard=True
                         ))


# выбор 24
@dp.message(lambda message: message.text == "Уйти, чтобы избежать конфликта")
async def go_left(message: types.Message):
    await message.answer("Уйдя от Чичи (Ци Ци), вы продолжаете свой путь и находите другой способ "
                         "выйти из пещеры.",
                         reply_markup=types.ReplyKeyboardMarkup(
                             keyboard=[
                                 [
                                     # выбор 37
                                     types.KeyboardButton(text="Продолжить поиски артефакта"),
                                     # выбор 38
                                     types.KeyboardButton(text="Выйти из пещеры")
                                 ]
                             ],
                             resize_keyboard=True
                         ))


# концовка 25
@dp.message(lambda message: message.text == "Продолжить путь вместе с ней")
async def go_left(message: types.Message):
    await message.answer("Продолжая свой путь вместе с Чичей, вы обнаруживаете узкий проход в стене. "
                         "Чича маленькая, поэтому боиться идти первой. Вы берете её за ручку и протискиваетесь в "
                         "проход. Почти дойдя до конца вы чувствуете адскую боль. Чича оказалась под заклятием и"
                         "воткнула в вас нож. Вам удалось дотащить ее до поверхности и Чича пришла в себя."
                         "\n"
                         "\nЯ в тебе разочарована путешественник, не стоит доверять даже миленьким малознакомым "
                         "девочкам. Надеюсь в следующих приключениях ты будешь осторожнее. Однако я очень рада, что ты"
                         " остался вживых, иногда это само по себе достижение) "
                         "\n"
                         "\nP.S. Если хотите пройти квест еще раз - введите /start",
                         reply_markup=types.ReplyKeyboardRemove())


# выбор 26
@dp.message(lambda message: message.text == "Продолжить свой путь в одиночестве")
async def go_left(message: types.Message):
    await message.answer("Продолжая свой путь одни, вы находите желанное сокровище, но вот вопрос: "
                         "Что вы будете с ним делать?",
                         reply_markup=types.ReplyKeyboardMarkup(
                             keyboard=[
                                 [
                                     # выбор 29
                                     types.KeyboardButton(text="Решить этот вопрос самостоятельно"),
                                     # выбор 30
                                     types.KeyboardButton(text="Вернуться домой и посоветоваться с Чжун Ли")
                                 ]
                             ],
                             resize_keyboard=True
                         ))


# концовка 27
@dp.message(lambda message: message.text == "Сразиться с врагами")
async def go_left(message: types.Message):
    await message.answer("Вы были наказаны за самоуверенность и отсутствие хитрости. Проиграв монстрам, вы остались "
                         "в пещере под их стражей навсегда и попали под влияние артефакта, став заманивать других "
                         "путешественников в ловушку."
                         "\n"
                         "\nПостарайтесь в следующих приключениях не лезть сразу в драку и удачи в путешествиях!"
                         "\n"
                         "\nP.S. Если хотите пройти квест еще раз - введите /start",
                         reply_markup=types.ReplyKeyboardRemove())


# концовка 28
@dp.message(lambda message: message.text == "Попытаться убежать")
async def go_left(message: types.Message):
    await message.answer("Убежав от монстров, вы потеряли возможность получить сокровища, зато остались в живых."
                         "Иногда это само по себе достижение :)."
                         ""
                         "Удачи в следующих приключениях!"
                         ""
                         "P.S. Если хотите пройти квест еще раз - введите /start",
                         reply_markup=types.ReplyKeyboardRemove())


# концовка 29
@dp.message(lambda message: message.text == "Решить этот вопрос самостоятельно")
async def go_left(message: types.Message):
    await message.answer("Хм ну тут, конечно, зависит от вашего интеллекта, но, просто чтоб ты знал: трогать "
                         "всё, что находишь в странных пещерах не стоит, ты не всегда можешь предугадать последствия..."
                         "В этот раз тебе повезло и удалось выбраться из пещеры живым, но артефакт ты, к сожалению, "
                         "сломал так, что его не починить даже изолентой. Зато ты остался жив."
                         "Иногда это само по себе достижение :)"
                         ""
                         "Удачи в следующих приключениях!"
                         ""
                         "P.S. Если хотите пройти квест еще раз - введите /start",
                         reply_markup=types.ReplyKeyboardRemove())


# концовка 30
@dp.message(lambda message: message.text == "Вернуться домой и посоветоваться с Чжун Ли")
async def go_left(message: types.Message):
    await message.answer("Чжун Ли благодарит вас за найденный артефакт и забирает его себе, пряча в сокровищницу, "
                         "но плаит вам кругленькую сумму за хорошую находку. Поздравляю с хорошей концовкой, денюжки "
                         "любят все!"
                         "\n"
                         "\nУдачи в следующих приключениях!"
                         "\n"
                         "\nP.S. Если хотите пройти квест еще раз - введите /start",
                         reply_markup=types.ReplyKeyboardRemove())


# концовка 31
@dp.message(lambda message: message.text == "Поделиться сокровищами с группой")
async def go_left(message: types.Message):
    await message.answer("Вместе с группой вы продаете найденный артефакт и заслуживаете уважение Сяо. Жаль, что"
                         " деньги вы делили поровну и вам досталась всего пара монет. "
                         "\n"
                         "\nПостарайтесь в следующих приключениях быть чуть-чуть прагматичнее и удачи! "
                         "\n"
                         "P.S. Если хотите пройти квест еще раз - введите /start",
                         reply_markup=types.ReplyKeyboardRemove())


# концовка 32
@dp.message(lambda message: message.text == "Убить всю группу и переместиться с артефактом подальше от пещеры")
async def go_left(message: types.Message):
    await message.answer("Артефакт почувствовал вашу ярость и запутал ваш разум, подчинив себе. Теперь вы навсегда"
                         " заперты в пещере и обречены заманивать других путешественников в ловушку."
                         "\n"
                         "\nПостарайтесь в следующих приключениях не лезть сразу в драку и удачи в путешествиях!"
                         "\n"
                         "P.S. Если хотите пройти квест еще раз - введите /start",
                         reply_markup=types.ReplyKeyboardRemove())


# концовка 33
@dp.message(lambda message: message.text == "Продолжить использование")
async def go_left(message: types.Message):
    await message.answer("Артефакт почувствовал вашу ярость и запутал ваш разум, подчинив себе. Теперь вы навсегда"
                         " заперты в пещере и обречены заманивать других путешественников в ловушку."
                         "\n"
                         "\nПостарайтесь в следующих приключениях не лезть сразу в драку и удачи в путешествиях!"
                         "\n"
                         "P.S. Если хотите пройти квест еще раз - введите /start",
                         reply_markup=types.ReplyKeyboardRemove())


# концовка 34
@dp.message(lambda message: message.text == "Вернуть на место")
async def go_left(message: types.Message):
    await message.answer("Оставив артефакт, вы направились на поиски выхода. Вам удалось выбраться из пещеры и даже"
                         " добраться до Чжун Ли. Он сообщил вам, что вы нашли очень ценный артефакт, но найти обратный "
                         "путь к нему вы, к сожалению, не смогли. Вы потеряли возможность получить сокровища, "
                         "зато остались в живых."
                         "\nИногда это само по себе достижение :)."
                         "\n"
                         "\nУдачи в следующих приключениях!"
                         "\n"
                         "P.S. Если хотите пройти квест еще раз - введите /start",
                         reply_markup=types.ReplyKeyboardRemove())


# концовка 35
@dp.message(lambda message: message.text == "Рискнуть и сразиться с ней")
async def go_left(message: types.Message):
    await message.answer("Мне очень жаль, но вас угандошила маленькая девочка. Надеюсь, вы возродитесеь где-нибудь"
                         " подальше от этой пещеры и забудете это как страшный сон."
                         "\n"
                         "\nПостарайтесь в следующих приключениях не лезть сразу в драку и удачи в путешествиях!"
                         "\n"
                         "P.S. Если хотите пройти квест еще раз - введите /start",
                         reply_markup=types.ReplyKeyboardRemove())


# концовка 36
@dp.message(lambda message: message.text == "Обнять её и бежать со всех ног")
async def go_left(message: types.Message):
    await message.answer("Вам удалось выбраться из пещеры. Чича бежала за вами со всех ног и только после выхода "
                         "вы поняли, что заклятие пропало. Вы вместе добрались до Чжун Ли. Он сообщил вам, что вы нашли"
                         " очень ценный артефакт, но найти обратный путь к нему вы, к сожалению, не смогли. Вы потеряли"
                         " возможность получить сокровища, зато остались в живых и обрели нового друга (Чичу), теперь "
                         "она будет рада путешествовать вместе с вами."
                         "\nИногда это само по себе достижение :)."
                         "\n"
                         "\nУдачи в следующих приключениях!"
                         "\n"
                         "P.S. Если хотите пройти квест еще раз - введите /start",
                         reply_markup=types.ReplyKeyboardRemove())


# концовка 37
@dp.message(lambda message: message.text == "Продолжить поиски артефакта")
async def go_left(message: types.Message):
    await message.answer("Вы нашли только разозленную группу, которая жаждала получить артефакт. Он затуманил им "
                         "разум, всем кроме Сяо. Вместе вам удалось выбраться из пещеры с серьезными ранами."
                         "Больше возвращаться вы туда не планируете, но вряд ли у вас скоро получится вернутся к "
                         "путешествиям. Зато вы остались в живых."
                         "\nИногда это само по себе достижение :)."
                         "\n"
                         "Удачи в следующих приключениях!"
                         "\n"
                         "P.S. Если хотите пройти квест еще раз - введите /start",
                         reply_markup=types.ReplyKeyboardRemove())


# концовка 38
@dp.message(lambda message: message.text == "Выйти из пещеры")
async def go_left(message: types.Message):
    await message.answer("Вам удалось выбраться из пещеры и даже добраться до Чжун Ли. Он сообщил вам, что вы "
                         "нашли очень ценный артефакт, но найти обратный путь к нему вы, к сожалению, не смогли. Вы "
                         "потеряли возможность получить сокровища, зато остались в живых."
                         "\nИногда это само по себе достижение :)."
                         "\n"
                         "Удачи в следующих приключениях!"
                         "\n"
                         "P.S. Если хотите пройти квест еще раз - введите /start",
                         reply_markup=types.ReplyKeyboardRemove())


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(
        "Я небольшой квест-бот. Вместе со мной ты можешь отправиться в путешествие в мире игры Genshin Impact"
    )


# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"
@dp.message()
async def send_echo(message: Message):
    await message.reply(text="Извини, я не понял, какой выбор ты сделал. Перейди в /help, если не понимаешь, что "
                             "происходт, или нажми на кнопку с выбором ответа. ")


if __name__ == '__main__':
    dp.run_polling(bot)
