def calculate_time_info(total_execution_count, completed_execution_count):
    total_time_estimate = 35 * total_execution_count
    actual_time_taken = 35 * completed_execution_count
    remaining_time = total_time_estimate - completed_execution_count * 35
    return total_time_estimate, actual_time_taken, remaining_time

def print_time_info(name, seconds):
    print(f"{name}: {seconds} seconds | {seconds / 60:.3f} minutes | {seconds / 3600:.3f} hours")

def display_time_info(total_execution_count, completed_execution_count):
    total_time_estimate, actual_time_taken, remaining_time = calculate_time_info(total_execution_count, completed_execution_count)
    print_time_info("Total estimated time for completion", total_time_estimate)
    print_time_info("Actual time taken so far", actual_time_taken)
    print_time_info("Remaining time until completion", remaining_time)
