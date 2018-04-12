import datetime
import os

import issue


ISSUE_HIDDEN_DIRECTORY = '.issue'

_ISSUE_REPOSITORY_PATH = None


def first(seq):
    return seq[0]


def get_repository_path() -> str:
    global _ISSUE_REPOSITORY_PATH
    if _ISSUE_REPOSITORY_PATH is None:
        repository_path = os.getcwd()
        isdir = lambda d: os.path.isdir(os.path.join(d, ISSUE_HIDDEN_DIRECTORY))
        while not isdir(repository_path) and repository_path != '/':
            repository_path = first(os.path.split(repository_path))
        repository_path = os.path.join(repository_path, ISSUE_HIDDEN_DIRECTORY)
        if not os.path.isdir(repository_path):
            raise issue.exceptions.RepositoryNotFound()
        _ISSUE_REPOSITORY_PATH = repository_path
    return _ISSUE_REPOSITORY_PATH


def objects_path() -> str:
    return os.path.join(get_repository_path(), 'objects')


def issues_path() -> str:
    return os.path.join(objects_path(), 'issues')


def comments_path_of(issue_id: str) -> str:
    return os.path.join(issues_path(), issue_id[:2], issue_id, 'comments')


def diffs_path_of(issue_id: str) -> str:
    return os.path.join(issues_path(), issue_id[:2], issue_id, 'diff')


def indexed_path_of(issue_id: str) -> str:
    return os.path.join(issues_path(), issue_id[:2], '{0}.json'.format(issue_id))


def timestamp(dt: datetime.datetime = None) -> float:
    return (dt or datetime.datetime.now()).timestamp()