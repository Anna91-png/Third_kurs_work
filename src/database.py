import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from config import DB_NAME, DB_USER, DB_PORT, DB_HOST, DB_PASSWORD


def create_database_if_not_exists() -> None:
    """
    Создание БД если не существует
    """
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database="postgres",
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT
        )
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

        with conn.cursor() as cur:
            cur.execute("select 1 from pg_database where datname=%s", (DB_NAME,))
            exists = cur.fetchone()

            if not exists:
                cur.execute(f"CREATE DATABASE {DB_NAME}")
                print(f"Создана база данных БД: {DB_NAME}")
            else:
                print(f"База данных {DB_NAME} уже существует")
    except psycopg2.Error as e:
        print(f"Error connecting to PostgreSQL: {e}")
    finally:
        if 'conn' in locals():
            conn.close()


def get_db_connection():
    create_database_if_not_exists()
    return psycopg2.connect(
        dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
    )


def create_tables():
    """
    Создаем таблицы employees и vacancies
    """
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS employees (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100),
                    position VARCHAR(100)
                )
            """)
            cur.execute("""
                CREATE TABLE IF NOT EXISTS vacancies (
                    id SERIAL PRIMARY KEY,
                    title VARCHAR(100),
                    salary INTEGER
                )
            """)
            conn.commit()
            print("Таблицы employees и vacancies созданы (если их не было)")


def add_employee(name, position):
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO employees (name, position) VALUES (%s, %s)",
                (name, position)
            )
            conn.commit()
            print(f"Сотрудник {name} добавлен")


def add_vacancy(title, salary):
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO vacancies (title, salary) VALUES (%s, %s)",
                (title, salary)
            )
            conn.commit()
            print(f"Вакансия {title} добавлена")


def get_employees():
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM employees")
            return cur.fetchall()


def get_vacancies():
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM vacancies")
            return cur.fetchall()
