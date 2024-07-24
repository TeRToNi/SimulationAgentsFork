class Logger:
    def __init__(self, path):
        from loguru import logger

        self.path = path
        logger.add(path, format="{level}: {message}")

    def info(self, msg):
        from loguru import logger
        import os

        try:
            os.remove(self.path)
        except FileNotFoundError:
            pass

        logger.info(msg)
