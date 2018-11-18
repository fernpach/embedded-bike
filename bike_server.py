#import mraa
import pymysql


def connect():
    user = ''
    passwd = ''
    db = ''

    return pymysql.connect(host='127.0.0.1',
                           user=user,
                           password=passwd,
                           db=db) 


def sql_insert(connection, entry_dict):
    """Perform sql insert using column,value pairs in entry_dict."""
    with connection.cursor() as cursor:
        sql = ("INSERT INTO entries" 
               "({}) values ({});".format(db_name,
                                          ",".join(d.keys()),
                                          ",".join(d.values()))
              )
        cursor.execute(sql)


def sql_select(connection, workout_id):
    with connection.cursor() as cursor:
        # Need to make this select most recent record
        sql = "SELECT * FROM entries WHERE {}".format(workout_id)
        cursor.execute(sql)
        return cursor.fetchone()
    

def main():
    """Script entry point."""    
    try:
        connection = connect()
    except:
        print('Failed to connect...')
    else:
        connection.close() 


if __name__ == '__main__':
    main()
