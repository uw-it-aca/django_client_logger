import logging



def process_log_message(message):
    for entry in message:
        write_log(entry['logger'], entry)


def write_log(log_name, entry):
    logger = logging.getLogger(log_name)
    logger.info(entry)


