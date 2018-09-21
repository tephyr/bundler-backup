class BundleInfo(object):
    """All metadata for a git bundle *backup*."""
    def __init__(self):
        self._repo_path = ''
        self._bkp_path = ''

    def load(self, repo_path, bkp_path_root):
        """Store repo path, generate bkp path."""
        self._repo_path = repo_path
        