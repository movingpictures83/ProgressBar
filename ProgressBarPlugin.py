import sys


class ProgressBar:
    def __init__(self, size, progress_max=100, title=''):
        self.size = size
        self.progress = 0
        self.progress_max = progress_max
        self.title = title

    def print(self, end=''):
        size = self.size - 2
        percent = round(100 * (self.progress / self.progress_max))
        count = round(size * percent / 100)
        output = "\r[{:{size}}] {:3}%".format("=" * count, percent, size=size)
        if self.title:
            print("{} | {}".format(output, self.title), end=end)
        else:
            print(output, end=end)
        sys.stdout.flush()

    def print_complete(self):
        output = "\r{:<{size}} 100%".format("Complete!", size=self.size)
        if self.title:
            print("{} | {}".format(output, self.title))
        else:
            print(output)
        sys.stdout.flush()


class ProgressBarPlugin:
 def input(self, inputfile):
        pass
 def run(self):
        pass
 def output(self, outputfile):
    from time import sleep
    progress_bar = ProgressBar(30, title="Example title")
    for i in range(100):
        progress_bar.progress = i
        progress_bar.print()
        sleep(0.1)
    progress_bar.print_complete()
