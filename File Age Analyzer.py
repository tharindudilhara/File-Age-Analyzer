import os
from datetime import datetime, timedelta


def file_age_analyzer(parent_directory):
    # Define age categories
    now = datetime.now()
    week_ago = now - timedelta(weeks=1)
    month_ago = now - timedelta(days=30)

    # Initialize counters and trackers
    less_than_week = 0
    between_week_and_month = 0
    older_than_month = 0
    newest_file = None
    oldest_file = None
    newest_time = None
    oldest_time = None

    # Walk through the directory
    for root, _, files in os.walk(parent_directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                # Get file creation/modification time
                file_time = datetime.fromtimestamp(os.path.getmtime(file_path))

                # Categorize files based on age
                if file_time >= week_ago:
                    less_than_week += 1
                elif week_ago > file_time >= month_ago:
                    between_week_and_month += 1
                else:
                    older_than_month += 1

                # Update newest and oldest files
                if newest_time is None or file_time > newest_time:
                    newest_time = file_time
                    newest_file = file_path
                if oldest_time is None or file_time < oldest_time:
                    oldest_time = file_time
                    oldest_file = file_path

            except Exception as e:
                print(f"Error processing file {file_path}: {e}")

    # Summary report
    print("File Age Analysis Report")
    print("========================")
    print(f"Files created less than a week ago: {less_than_week}")
    print(f"Files created between a week and a month ago: {between_week_and_month}")
    print(f"Files older than a month: {older_than_month}")
    print()
    print(f"Newest file: {newest_file} (Modified: {newest_time})")
    print(f"Oldest file: {oldest_file} (Modified: {oldest_time})")


# Example usage:
if __name__ == "__main__":
    directory = input("Enter the parent directory to analyze: ")
    file_age_analyzer(directory)
