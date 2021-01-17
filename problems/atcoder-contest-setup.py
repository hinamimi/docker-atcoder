#!/usr/bin/python

# EXECUTE: 
# ./atcoder-contest-setup ${URL-or-CONTEST}
#
# ARGUMENT:
# - CONTEST: contest name  e.g. abc100
# - URL: contest url  e.g. https://atcoder.jp/contests/abc100
#
# EXPLAIN:
# - making task directories and empty files and downloading testcases


import argparse
import os
import subprocess
import time
import urllib.request, urllib.error


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('url_contest')
    parser.add_argument('--problemset', default='abcdef')
    parser.add_argument('--no-download', action='store_true', default=False)
    return parser.parse_args()

def get_url_contest(args):
    if args.url_contest.startswith('https://'):
        url = args.url_contest
        contest = os.path.basename(url)
    else:
        contest = args.url_contest
        url = f'https://atcoder.jp/contests/{contest}'
    try:
        urllib.request.urlopen(url)
    except urllib.error.HTTPError as e:
        print(f'Invalid URL: {url}')
        exit(1)
    return url, contest

def is_login():
    args = ['oj', 'login', 'https://atcoder.jp', '--check']
    p = subprocess.run(args, stdout=subprocess.PIPE)
    message_log = p.stdout.decode('utf-8')
    login_message = None
    for message in message_log.split('\n'):
        if 'signed in' in message:
            login_message = message

    if login_message == '[SUCCESS] You have already signed in.':
        return True
    elif login_message == '[FAILURE] You are not signed in.':
        return False
    else:
        print(f'Undefined Message:\n {message_log}')
        exit(1)

def get_account():
    with open('.account', 'r') as f:
        username = f.readline().rstrip()
        password = f.readline().rstrip()
    return username, password

def login(username, password):
    subprocess.run(
        ['oj', 'login', '-u', username, '-p', password, 'https://atcoder.jp']
    )

if __name__ == "__main__":
    args = parse_args()
    url, contest = get_url_contest(args)
    print(url, contest)
    if not is_login():
        login(*get_account())
        time.sleep(1)

    if not os.path.exists(contest):
        os.mkdir(contest)
    os.chdir(contest)

    for problem in args.problemset:
        if not os.path.exists(problem):
            os.mkdir(problem)
        os.chdir(problem)

        if not os.path.exists(f'{problem}.py'):
            with open(f'{problem}.py', 'w') as f:
                f.write('#!/usr/bin/python')
            subprocess.run(['chmod', 'a+x', f'{problem}.py'])

        if not args.no_download:
            task_url = f'{url}/tasks/{contest}_{problem}'
            try:
                urllib.request.urlopen(task_url)
            except urllib.error.HTTPError as e:
                print(f'Not Available URL: {task_url}')
                os.chdir('..')
                continue
            if not os.path.exists('test'):
                subprocess.run(['oj', 'd', task_url])

        os.chdir('..')
