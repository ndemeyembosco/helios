#!/usr/bin/env python3

import MySQLdb 
from getpass import getpass


def main(): 
    host     = input('HOST: ') 
    port     = input('PORT: ') 
    password = getpass() 
    database = input('DATABASE: ')
    d_or_c   = input('ACTION: ')
    
    db     = None 
    cursor = None 
    try: 
        db = MySQLdb.connect(host=host, port=port, password=password, database=database, use_unicode=True, charset='utf8mb4')
    except: 
        raise ConnectionError('Could not establish a connection to the database.')

    cursor = db.cursor() 

    query = ''

    if d_or_c == 'create': 
        query = '''
            CREATE TABLE diff(
                id INT(11), 
                file_path VARCHAR(256), 
                language VARCHAR(64),
                body LONGTEXT, 
                commit_id INT(11)
            )
        '''

    if d_or_c == 'delete': 
        query = '''
            DROP TABLE diff;
        '''

    cursor.execute(query)

    db.close() 



if __name__ == '__main__': 
    main()  