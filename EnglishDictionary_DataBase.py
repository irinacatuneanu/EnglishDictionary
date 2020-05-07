import mysql.connector
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

con = mysql.connector.connect(
    user = 'ardit700_student',
    password = 'ardit700_student',
    host = '108.167.140.122',
    database = 'ardit700_pm1database'
)
cursor = con.cursor()
word = input("Enter a word: ")
query = cursor.execute('SELECT * FROM Dictionary WHERE Expression = "%s"' % word)
results = cursor.fetchall()

if results:
    for i in results:
        print(i[1])
else:
    print("word not found")
