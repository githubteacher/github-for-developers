from git.api import Clone


class GitClone:
    """An Github API for Clone"""
    
    def __init__(repo_url, auth)
        """Initilaze the git repo with URL and authentication"""
        
        self.__url = repo_url
        self.__auth = auth
        
    def clone(local_repo_dir=None, branch=None)
        """Clone the git repo to the specified directory
        
        Args:
            local_repo_dir: Local directory path where we need to clone the repo
            branch: a branch to clone, default will be master
        """
    
