from collections import defaultdict

def analyze_logs(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    summary = defaultdict(int)

    for line in lines:
        if 'ERROR' in line:
            summary['ERROR'] += 1
        elif 'INFO' in line:
            summary['INFO'] += 1
        elif 'WARNING' in line:
            summary['WARNING'] += 1

    print("Log Summary Report:")
    for key, value in summary.items():
        print(f"{key}: {value} occurrence(s)")

if __name__ == "__main__":
    analyze_logs("sample_logs.txt")