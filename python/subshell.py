"""subshell - simple non-persistent subshell for command execution"""
# From ActiveState recepies: this is recipe

import os
import subprocess

class SubShell(object):
    # Slight misnomer since it isn't persistent, but close enough...

    def __init__(self, env=None):
        if env is None:
            env = os.environ.copy()
        self.env = env

    def capture(self, cmd):
        """Captures stdout for shell command"""
        return subprocess.check_output(cmd, shell=True, env=self.env)

    def run(self, cmd):
        """Result is True if return code was 0, False otherwise"""
        return not subprocess.call(cmd, shell=True, env=self.env)

"""
Use is:
================================================================================
import subshell
shell = subshell.SubShell()
shell.run('ls -l')
listing = shell.capture('ls -l')

"""
