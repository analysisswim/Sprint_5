Stellar Burgers — Selenium автотесты (Sprint 5)

Учебный проект по автоматизации UI-тестов сервиса Stellar Burgers.
Покрывает регистрацию, авторизацию разными путями, переходы между разделами, выход из аккаунта и вкладки «Конструктора».

Что проверяем (соответствие требованиям)

Регистрация
tests/test_registration.py::test_registration_success — успешная регистрация (имя не пустое, email в формате login@domain, пароль ≥ 6 символов).
tests/test_registration.py::test_registration_error_short_password — ошибка при слишком коротком пароле.

Вход
tests/test_login.py::test_login_via_main_button — по кнопке «Войти в аккаунт» на главной.
tests/test_login.py::test_login_via_header_lk — через «Личный кабинет».
tests/test_login.py::test_login_from_register_form — через кнопку в форме регистрации.
tests/test_login.py::test_login_from_recovery_form — через кнопку в форме восстановления пароля.

Личный кабинет и навигация
tests/test_navigation.py::test_go_to_account — переход в ЛК по «Личный кабинет».
tests/test_navigation.py::test_back_to_constructor_by_button_and_logo — возврат в «Конструктор» по кнопке и по логотипу.

Выход
tests/test_logout.py::test_logout — выход по кнопке «Выйти» в личном кабинете.

Раздел «Конструктор»
tests/test_constructor_tabs.py::test_tabs_switch — переключения «Булки», «Соусы», «Начинки».

Структура проекта:
Sprint_5/
├─ conftest.py                 # фикстуры: драйвер, базовый URL, кросс-браузерный запуск
├─ pytest.ini                  # настройки pytest (маркеры, опции)
├─ helpers/
│  ├─ __init__.py
│  ├─ overlays.py              # убийца модальных/оверлеев + ожидание их отсутствия
│  └─ clicks.py                # безопасный клик (с прокруткой/JS-фолбэком)
├─ utils/
│  ├─ __init__.py
│  └─ data.py                  # локаторы и тестовые константы
├─ tests/
│  ├─ __init__.py
│  ├─ test_registration.py
│  ├─ test_login.py
│  ├─ test_navigation.py
│  ├─ test_constructor_tabs.py
│  └─ test_logout.py
└─ requirements.txt




## Setup
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt

# env (или через Run/Debug → Environment variables)
export STELLAR_EMAIL="siarhei_ivashyn_34_999@yandex.ru"
export STELLAR_PASSWORD="12345Zz"

## Run Chrome
pytest -q
## Run Firefox
pytest -q --browser=firefox
# или часть:
pytest -q -k login
pytest -q -m smoke
# Запуск одного файла
pytest -q tests/test_registration.py
