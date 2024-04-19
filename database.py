import sqlite3

def create_db(data) :

    conn = sqlite3.connect('database') 
    c = conn.cursor()

    # Create a table
    c.execute('''CREATE TABLE IF NOT EXISTS facebook_posts 
                  (post TEXT, comments INTEGER, shares INTEGER)''')

    for post in data:
        c.execute('''INSERT INTO facebook_posts (post, comments, shares) 
                    VALUES (?, ?, ?)''', 
                    (post['post'], post['comments'], post['shares']))

    # Commit your changes in the database
    conn.commit()
    print("Records inserted........")

    # Closing the connection
    conn.close()