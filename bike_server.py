#import mraa
import pymysql


def connect():
    user = 'root'
    passwd = 'intel123'
    db = 'captare'

    return pymysql.connect(host='127.0.0.1',
                           user=user,
                           password=passwd,
                           db=db) 

def db_Entry(d, db_name):
    sql_push = "INSERT INTO " + db_name + "(UserID, Timestamp, WorkoutID, Speed, Distance, HeartRate, Calories) values (" + d[UserID] +"," +  d[Timestamp] +"," +  d[WorkoutID] +"," +  d[Speed] +"," +  d[Distance] +"}"
    return sql_push

def main():
    """Script entry point."""    
    try:
        connection = connect()
        with connection.cursor() as cursor:
            tmp_data = {"UserID": "Sarah TMP", "Timestamp": 3, "WorkoutID": 0, "Speed": 22, "Distance":50}            
            cursor.execute(db_Entry(tmp_data, 'entries'))
                           
            sql = "SELECT * FROM entries"
            cursor.execute(sql)
            #result = cursor.fetchone()
            result = cursor.fetchall()
            print(result)
    finally:
        connection.close() 


if __name__ == '__main__':
    main()
