from pathlib import Path

class BundleInfo(object):
    """All metadata for a git bundle *backup*."""
    def __init__(self, repo_root, bkp_root):
        self._repo_root = Path(repo_root)
        self._bkp_root = Path(bkp_root)
        self._repo_path = ''
        self._bkp_path = ''

    def load(self, repo_path):
        """Store repo path, generate bkp path."""
        self._repo_path = Path(repo_path)

        self._bkp_path = Path(self._bkp_root, self._repo_path.relative_to(self._repo_root))

    def backup(self):
        """Bundle the repo into a backup."""
        print("Will bundle {repo} into {bkp}".format(
            repo=self._repo_path,
            bkp=self._bkp_path))
