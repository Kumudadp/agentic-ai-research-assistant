import time

def stream_log(container, message, delay=0.6):
    container.markdown(f"- {message}")
    time.sleep(delay)
