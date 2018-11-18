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
