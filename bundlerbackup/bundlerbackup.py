import argparse
from pathlib import Path
import sys

from sh import git

from bundleinfo import BundleInfo

args = None
bundles = []

def parse_args():
    global args
    parser = argparse.ArgumentParser(description='Find and bundle git repos.')
    parser.add_argument('--repo-root', dest='repo_root', help='Root location of the git repos')
    parser.add_argument('--backup-root', dest='backup_root', help='Root location to store backups')

    args = parser.parse_args()

def verify_args():
    global args

    if not Path(args.repo_root).is_dir():
        raise FileNotFoundError('repo_root not found: {0}'.format(args.repo_root))

    if not Path(args.backup_root).is_dir():
        raise FileNotFoundError('backup_root not found: {0}'.format(args.backup_root))

def find_repos(start_path):
    global bundles

    root_path = Path(start_path)
    for child in root_path.iterdir():
        if is_repo(child):
            print("Found repo at {0}".format(child))
            bundle = BundleInfo()
            bundle.load(child, args.backup_root)
            bundles.append(bundle)
        elif child.is_dir():
            find_repos(child)


def is_repo(repo_path):
    """Return t/f if this path is a git repo."""
    if repo_path.exists() and repo_path.is_dir():
        git_path = Path(repo_path, '.git')
        if git_path.exists() and git_path.is_dir():
            return True

    return False

def run():
    global bundles;

    parse_args()

    try:
        verify_args()
    except FileNotFoundError as fnfErr:
        print('VERIFY ARGS FAILED; exiting')
        print(fnfErr)
        sys.exit(1)

    verify_args()
    find_repos(args.repo_root)
    [b for b in bundles]

if __name__ == '__main__':
    run()
