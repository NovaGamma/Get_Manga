import sys
import time

class ProgressBar():
    def __init__(self, size):
        self.size = size
        self.index = 0

    def start(self):
        sys.stdout.write(f"[{' '*(self.size)}]")
        sys.stdout.flush()
        sys.stdout.write("\b"*(self.size+1))

    def next(self):
        if self.index != self.size:
            sys.stdout.write("-")
            sys.stdout.flush()
            self.index += 1
            return True
        return False

class Progress():
    def __init__(self, size=0):
        self.size = size
        self.index = 0

    def start(self):
        percent = str(self.index/self.size*100)[:4]
        text = f"{self.index}/{self.size} {percent}%"
        sys.stdout.write(text)
        sys.stdout.flush()
        sys.stdout.write("\b"*len(text))

    def next(self):
        self.index += 1
        p = self.index/self.size*100
        percent = str(p)[:4] if p != 100 else str(p)[:3]
        text = f"{self.index}/{self.size} {percent}%"
        sys.stdout.write(text)
        sys.stdout.flush()
        sys.stdout.write("\b"*len(text))
