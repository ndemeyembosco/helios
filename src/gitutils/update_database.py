#!/usr/bin/env python3

import os
import sys

import MySQLdb
from db_interface import *

HOST = 'sansa.cs.uoregon.edu'
USERNAME = '' # edit this
PASSWORD = '' # edit this
PORT = 3331
DATABASE = 'ideas_db'
LOG_DIR = '/shared/soft/ideas_db/logs/'

if len(sys.argv)>2: 
    USERNAME=sys.argv[1]
    PASSWORD=sys.argv[2]

def run(cmd: str, dry_run=True):
    print(cmd)
    if not dry_run:
        os.system(cmd)


def update():
    db = MySQLdb.connect(host=HOST,
                         port=PORT,
                         user=USERNAME,
                         password=PASSWORD,
                         database=DATABASE,
                         use_unicode=True,
                         charset='utf8mb4')
    cursor = db.cursor()
    query = 'select name, source_url from project'
    cursor.execute(query)
    project_info = cursor.fetchall()
    cursor.close()
    db.close()

    os.makedirs(LOG_DIR, exist_ok=True)

    for name, source_url in project_info:
        # Python -- 3.9 preferred
        # Add git info
        # This can take a long time, but is not subject to any API limits, so all projects can be updated simultaneously
        git_log_path = os.path.join(LOG_DIR, f'{name}_git.log')
        git_command = f'nohup python -m src.gitutils.db_interface --username {USERNAME} --password {PASSWORD} --add_project {source_url} 2>&1 | tee {git_log_path} &'
        run(git_command, dry_run=False)

    all_commands = ''
    for name, source_url in project_info:
        # The updates below are subject to the GraphQL API limits (5000 points per hour), so these are run in order
        # Add prs
        pr_log_path = os.path.join(LOG_DIR, f'{name}_pr.log')
        pr_command = f'nohup python -m src.gitutils.db_interface --username {USERNAME} --password {PASSWORD} --add_prs {source_url} 2>&1 | tee {pr_log_path} ;\n'
        # Add issues
        issue_log_path = os.path.join(LOG_DIR, f'{name}_issue.log')
        issue_command = f'nohup python -m src.gitutils.db_interface --username {USERNAME} --password {PASSWORD} --add_issues {source_url} 2>&1 | tee {issue_log_path};\n'
        # Add events
        event_log_path = os.path.join(LOG_DIR, f'{name}_event.log')
        event_command = f'nohup python -m src.gitutils.db_interface --username {USERNAME} --password {PASSWORD} --add_events {source_url} 2>&1 | tee {event_log_path};\n '
        all_commands += pr_command + issue_command + event_command

    run(all_commands, dry_run=False)
        
if __name__ == '__main__':
    update()
