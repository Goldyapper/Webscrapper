import sqlite3

def database_adder(episode_data):
    
    name = episode_data[0][0] if episode_data[0] else None
    season = episode_data[1][0] if episode_data[1] else "1"
    doctor = episode_data[2][0] if episode_data[2] else None
    companions = ', '.join(episode_data[3]) if episode_data[3] else ''
    featuring = ', '.join(episode_data[4]) if episode_data[4] else ''
    villains = ', '.join(episode_data[5]) if episode_data[5] else ''
    setting = ', '.join(episode_data[6]) if episode_data[5] else ''
    writer = ', '.join(episode_data[7]) if episode_data[6] else ''
    director = ', '.join(episode_data[8]) if episode_data[7] else ''
    air_date = ', '.join(episode_data[9]) if episode_data[8] else ''
    
    # Connect to SQLite DB
    conn = sqlite3.connect('doctor_who.db')
    cursor = conn.cursor()

    # Create table 
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS episodes (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        season TEXT,
        doctor TEXT NOT NULL,
        companions TEXT,
        featuring TEXT,
        villains TEXT,
        setting TEXT,
        writer TEXT NOT NULL,
        director TEXT NOT NULL,
        air_date TEXT
    )
    ''')

    # Get the highest ID manually
    cursor.execute('SELECT MAX(id) FROM episodes')
    result = cursor.fetchone()
    id = (result[0] or 0) + 1


    cursor.execute('''
    INSERT INTO episodes (id, name, doctor, season, companions, featuring, villains, setting, writer, director, air_date)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (id, name, doctor, season, companions, featuring, villains, setting, writer, director, air_date))


    # Save and close
    conn.commit()
    conn.close()