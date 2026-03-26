def load_data(data, on_success=None):
    print("Loading data...")
    try:
        # simulate logic
        result = f"{data} loaded"
        if on_success:
            on_success(result)
    except Exception as e:
        print(f"Error: {e}")

def log_to_file(msg):
    print(f"Logging to file: {msg}")

def send_notification(msg):
    print(f"Sending notification: {msg}")

# Reuse the same function with different behaviors
load_data(["record1"], log_to_file)
load_data(["record2"], send_notification)