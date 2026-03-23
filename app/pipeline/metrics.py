import time 

class PipelineMetrics:
    def __init__(self):
        self.start_time = None
        self.row_extracted = 0
        self.row_loaded = 0
        self.success = False

    def start(self):
        self.start_time = time.time()
    
    def finish(self , success: bool):
        self.success = success
        self.duration_seconds = time.time() - self.start_time