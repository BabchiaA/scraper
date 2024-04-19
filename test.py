import unittest
import sqlite3

from database import create_db  

class TestCreateDB(unittest.TestCase):

    def setUp(self):
        # Create an in-memory database for testing
        self.conn = sqlite3.connect(':memory:')
        self.cursor = self.conn.cursor()

    def tearDown(self):
        # Close the database connection
        self.conn.close()

    def test_create_db(self, data):
        # Call the function
        create_db(data, self.conn)

        # Check if records are inserted
        self.cursor.execute("SELECT COUNT(*) FROM facebook_posts")
        count = self.cursor.fetchone()[0]
        self.assertEqual(count, len(data))

if __name__ == '__main__':
    unittest.main()