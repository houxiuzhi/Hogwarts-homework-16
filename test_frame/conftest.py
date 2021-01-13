import signal
from shlex import shlex
import pytest
import os
import subprocess
import shlex

@pytest.fixture(scope='module',autouse=True)
def record_vedio():
    cmd = "scrcpy --record tmp.mp4"
    p = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    print(p)
    yield
    os.kill(p.pid,signal.CTRL_C_EVENT)

