Stellar Burgers — Selenium автотесты (Sprint 5)

Что проверяем (соответствие требованиям)
Регистрация
tests/test_registration.py::TestRegistration::test_success_registration — успешная регистрация (имя не пустое, email в формате login@domain, пароль ≥ 6 символов).
tests/test_registration.py::TestRegistration::test_invalid_password_shows_error — ошибка при слишком коротком пароле.

Вход
tests/test_login.py::TestLogin::test_login_via_main_button — вход по кнопке «Войти в аккаунт» на главной.
tests/test_login.py::TestLogin::test_login_via_header_lk — вход через «Личный кабинет» в шапке.
tests/test_login.py::TestLogin::test_login_from_register_form — вход из формы регистрации (ссылка «Войти»).
tests/test_login.py::TestLogin::test_login_from_recovery_form — вход из формы восстановления пароля (ссылка «Войти»).

Личный кабинет и навигация
tests/test_navigation.py::TestNavigation::test_go_to_account — переход в ЛК по «Личный кабинет».
tests/test_navigation.py::TestNavigation::test_back_to_constructor_by_button_and_logo — возврат в «Конструктор» по кнопке и по логотипу.

Выход
tests/test_logout.py::TestLogout::test_logout — выход по кнопке «Выход» в личном кабинете.

Конструктор
tests/test_constructor_tabs.py::TestConstructorTabs::test_tab_switch — переключения вкладок «Булки», «Соусы», «Начинки».

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
# Запуск одного файла
pytest -q tests/test_registration.py
# Sprint_6
