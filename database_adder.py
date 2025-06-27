import sqlite3

def database_adder(episode_data):
    
    title = episode_data[0][0]
    doctor = episode_data[2][0]
    companions = ', '.join(episode_data[3])
    featuring = ', '.join(episode_data[4])
    villains = ', '.join(episode_data[5])
    writer = ', '.join(episode_data[6])
    director = ', '.join(episode_data[7])
    
    # Connect to SQLite DB
    conn = sqlite3.connect('doctor_who.db')
    cursor = conn.cursor()

    # Create table 
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS episodes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        doctor TEXT,
        companions TEXT,
        featuring TEXT,
        villains TEXT,
        writer TEXT,
        director TEXT
    )
    ''')

    cursor.execute('''
    INSERT INTO episodes (title, doctor, companions, featuring, villains, writer, director)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (title, doctor, companions, featuring, villains, writer, director))


    # Save and close
    conn.commit()
    conn.close()