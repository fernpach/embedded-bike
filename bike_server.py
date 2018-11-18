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


def main():
    """Script entry point."""
    try:
        connection = connect()

        with connection.cursor() as cursor:
            sql = "SELECT * FROM entries"
            cursor.execute(sql)
            result = cursor.fetchone()
            print(result)
    finally:
        connection.close() 


if __name__ == '__main__':
    main()
