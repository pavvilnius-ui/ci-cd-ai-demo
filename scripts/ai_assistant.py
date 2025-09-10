import os

def analyze_logs(log_path):
    if not os.path.exists(log_path):
        print("No logs found.")
        return
    with open(log_path, "r") as f:
        logs = f.read()
    print("=== AI Assistant Analysis ===")
    if "AssertionError" in logs:
        print("❌ Test failed. Possible assertion mismatch. Did you check your expected vs actual values?")
    else:
        print("⚠️ Tests failed. Review the logs carefully.")
    print("=============================")

if __name__ == "__main__":
    analyze_logs("failed_pipeline.log")
