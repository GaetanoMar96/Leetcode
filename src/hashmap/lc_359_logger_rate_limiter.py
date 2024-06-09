class Logger:
    def __init__(self):
        # hashmap of key (message), value (timestamp)
        self.messages = {}
    
    def should_print(self, timestamp: int, message: str) -> bool:
        if message not in self.messages:
            self.messages[message] = timestamp + 10 #when it will be available again
            return True
        
        prev_timestamp = self.messages[message]
        if timestamp < prev_timestamp:
            return False
        
        self.messages[message] = timestamp + 10
        return True
