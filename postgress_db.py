import psycopg2
from decouple import config

connect_db = {
    'dbname': config('DB_NAME'),
    'user': config('DB_USER'),
    'host': config('DB_HOST'),
    'password': config('DB_PASSWORD'),
    'port': config('DB_PORT')
}

def connect():

    try:
        conn = psycopg2.connect(**connect_db)
        cursor = conn.cursor()

        create_table = (
            """
            CREATE TABLE IF NOT EXISTS user_acct (
            id SERIAL PRIMARY KEY,
            user_name VARCHAR(100),
            password VARCHAR(100),
            address VARCHAR(100),
            email VARCHAR(50) UNIQUE NOT NULL,
            account_number NUMERIC(10) NULL,
            phone_no NUMERIC(11),
            balance NUMERIC(10, 2) DEFAULT 0.00, 
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );

            CREATE TABLE IF NOT EXISTS transactions (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            account_number NUMERIC(10) NOT NULL,
            amount NUMERIC(10, 2),
            transaction_type VARCHAR(100) NULL,
            user_id INT,
            FOREIGN KEY (user_id) REFERENCES user_acct(id),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """
        ) 

        cursor.execute(create_table)
        conn.commit()
        print("Table created successfully")
        return conn
    except psycopg2.Error as e:
        conn.rollback()
        print(e)
        return None
    # finally:
    #     if conn:
    #         conn.close()
    #     if cursor:
    #         cursor.close()
connect ()
