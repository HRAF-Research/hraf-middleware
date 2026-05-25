from typing import List, Dict, Any

# 1. First Focused Function: Only handles splitting the raw string into lines
def parse_raw_data(raw_data: str) -> List[List[str]]:
    lines = raw_data.strip().split("\n")
    return [line.split(",") for line in lines if line.strip()]

# 2. Second Focused Function: Only validates formats and structures data
def validate_and_clean_users(parsed_lines: List[List[str]]) -> List[Dict[str, Any]]:
    valid_users = []
    for parts in parsed_lines:
        if len(parts) == 3:
            user_id = parts[0].strip()
            name = parts[1].strip()
            age_str = parts[2].strip()
            
            if user_id.startswith("USR") and age_str.isdigit():
                valid_users.append({"id": user_id, "name": name, "age": int(age_str)})
    return valid_users

# 3. Third Focused Function: Only transforms data aesthetics (formatting names)
def format_user_names(users: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    formatted_users = []
    for user in users:
        formatted_users.append({
            "id": user["id"],
            "name": user["name"].title(),
            "age": user["age"]
        })
    return formatted_users

# 4. Fourth Focused Function: Only does pure mathematical calculation
def calculate_average_age(users: List[Dict[str, Any]]) -> float:
    if not users:
        return 0.0
    total_age = sum(user["age"] for user in users)
    return total_age / len(users)

# 5. Fifth Focused Function: Only handles writing the data out to your drive
def save_report_to_file(users: List[Dict[str, Any]], average_age: float, filename: str) -> None:
    with open(filename, "w") as f:
        f.write("--- USER REPORT ---\n")
        for user in users:
            f.write(f"ID: {user['id']} | Name: {user['name']} | Age: {user['age']}\n")
        f.write("-------------------\n")
        f.write(f"Total Users: {len(users)}\n")
        f.write(f"Average Age: {average_age:.1f}\n")


# --- Orchestrator function to run them together smoothly ---
def run_middleware_pipeline() -> None:
    raw_input_data = """
    USR001, guneet kaur, 25
    INVALID_LINE, test, abc
    USR002, john doe, 42
    """
    
    # Executing the 5 steps sequentially
    raw_lines = parse_raw_data(raw_input_data)
    cleaned_data = validate_and_clean_users(raw_lines)
    final_users = format_user_names(cleaned_data)
    avg_age = calculate_average_age(final_users)
    
    save_report_to_file(final_users, avg_age, "user_report.txt")
    print("Processing complete! Split into 5 clean functions with type hints.")

if __name__ == "__main__":
    run_middleware_pipeline()