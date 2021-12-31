import logging


class Logger:

    def __init__(self):
        logging.basicConfig(level=logging.DEBUG,
                            format="%(levelname)s %(asctime)s - %(message)s")

        self.logger = logging.getLogger()

    def update(self, payload: str):
        self.logger.info(f"{payload}")
