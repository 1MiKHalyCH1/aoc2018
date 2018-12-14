class Worker:
    def __init__(self):
        self.work = None
        self.time = 0

    def add_work(self, node):
        self.work = node
        self.time = node.seconds
    
    def make_work_second(self):
        self.time = self.time - 1 if self.time else 0
    
    def get_ready_work(self):
        if not self.time:
            res = self.work
            self.work = None
            return res
        else:
            return None