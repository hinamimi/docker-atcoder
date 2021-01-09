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
import urllib.request, urllib.error


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('url_contest')

    args = parser.parse_args()
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

    subprocess.run(['oj', 'login', '-u', 'hinamimi', 'https://atcoder.jp'])
    if not os.path.exists(contest):
        os.mkdir(contest)
    os.chdir(contest)
    for problem in 'abcdef':
        task_url = f'{url}/tasks/{contest}_{problem}'
        try:
            urllib.request.urlopen(task_url)
        except urllib.error.HTTPError as e:
            continue
        if not os.path.exists(problem):
            os.mkdir(problem)
        os.chdir(problem)

        if not os.path.exists(f'{problem}.py'):
            with open(f'{problem}.py', 'w') as f:
                f.write('#!/usr/bin/python')
            subprocess.run(['chmod', 'a+x', f'{problem}.py'])

        if not os.path.exists('test'):
            subprocess.run(['oj', 'd', task_url])
        os.chdir('..')
