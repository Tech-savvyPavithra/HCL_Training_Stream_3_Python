class Logger:
    def log(self, message):
        print(f"[LOG]: {message}")

class FileLogger(Logger):
    def log(self, message):
        # Call parent method using super()
        super().log(message)
        
        # Additional behavior
        print(f"Writing '{message}' to file...")

logger = FileLogger()
logger.log("System started")