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
#print(results[0][0])
#print(results[1][0])


#print(list)
#print(get_close_matches(word,list))
# def translate(word):
#     for i in results:
#         if word == i[0]:
#             return i[1]
#         elif len(get_close_matches(word,list)) > 0:
#             yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word,list)[0])
#             if yn == 'Y':
#                 return i
#             elif yn == 'N':
#                 return "The word does not exist. Please double check it."
#             else:
#                 return "We did not understand your entry."
#         else:
#             return "The word does not exist. Please double check it"
    #else:
     #   return "The word does not exist. Please double check it"

# if results:
#     for i in results:
#         print(i)
# else:
#     print("No result found")

# output = translate(word)
# print(output)
# if type(output)==list:
#     for answer in output:
#         print (answer)
# else:
#     print(output)
