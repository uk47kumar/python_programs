import mysql.connector
db_connection = mysql.connector.connect(
    host="localhost",
    user="put_your_username_here",
    passwd="put_your_password_here",
    database="database_name"
)
my_database = db_connection.cursor()
sql_query = "DELETE FROM codespeedy where category='Python'"
my_database.execute(sql_query)
db_connection.commit()
print("Row(s) deleted successfully!!!!")
