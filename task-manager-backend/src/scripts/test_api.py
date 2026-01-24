#!/usr/bin/env python3
"""
Automated API Test Script for Task Manager Backend
Run with: python test_api.py
Make sure the server is running on localhost:3000
"""

import requests
import sys
import time

BASE_URL = "http://localhost:3000"

# Unique suffix for this test run (avoids duplicate email conflicts)
TEST_RUN_ID = str(int(time.time()))

# Colors for terminal output
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"

passed = 0
failed = 0


def log_pass(message):
    global passed
    passed += 1
    print(f"{GREEN}[PASS]{RESET} {message}")


def log_fail(message, details=""):
    global failed
    failed += 1
    print(f"{RED}[FAIL]{RESET} {message}")
    if details:
        print(f"       {details}")


def log_section(title):
    print(f"\n{BLUE}{'='*50}")
    print(f" {title}")
    print(f"{'='*50}{RESET}\n")


def log_info(message):
    print(f"{YELLOW}[INFO]{RESET} {message}")


# ============================================
# USER TESTS
# ============================================
def test_create_user(name, email):
    """Create a user and return the user object"""
    response = requests.post(f"{BASE_URL}/users", json={
        "name": name,
        "email": email
    })
    if response.status_code == 201:
        log_pass(f"Created user: {name}")
        return response.json()
    else:
        log_fail(f"Create user: {name}", f"Status: {response.status_code}")
        return None


def test_get_all_users():
    """Get all users"""
    response = requests.get(f"{BASE_URL}/users")
    if response.status_code == 200:
        users = response.json()
        log_pass(f"Get all users (found {len(users)})")
        return users
    else:
        log_fail("Get all users", f"Status: {response.status_code}")
        return []


def test_get_user_by_id(user_id):
    """Get user by ID"""
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    if response.status_code == 200:
        log_pass(f"Get user by ID: {user_id}")
        return response.json()
    else:
        log_fail(f"Get user by ID: {user_id}", f"Status: {response.status_code}")
        return None


def test_update_user(user_id, name, email):
    """Update user by ID"""
    response = requests.put(f"{BASE_URL}/users/{user_id}", json={
        "name": name,
        "email": email
    })
    if response.status_code == 200:
        log_pass(f"Updated user {user_id}: {name}")
        return response.json()
    else:
        log_fail(f"Update user {user_id}", f"Status: {response.status_code}")
        return None


def test_delete_user(user_id):
    """Delete user by ID"""
    response = requests.delete(f"{BASE_URL}/users/{user_id}")
    if response.status_code == 200:
        log_pass(f"Deleted user: {user_id}")
        return True
    else:
        log_fail(f"Delete user: {user_id}", f"Status: {response.status_code}")
        return False


def test_get_user_not_found(user_id):
    """Test 404 for non-existent user"""
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    if response.status_code == 404:
        log_pass(f"User not found returns 404 (ID: {user_id})")
        return True
    else:
        log_fail(f"User not found should return 404", f"Got: {response.status_code}")
        return False


# ============================================
# GROUP TESTS
# ============================================
def test_create_group(name, description=None):
    """Create a group and return the group object"""
    data = {"name": name}
    if description:
        data["description"] = description

    response = requests.post(f"{BASE_URL}/groups", json=data)
    if response.status_code == 201:
        log_pass(f"Created group: {name}")
        return response.json()
    else:
        log_fail(f"Create group: {name}", f"Status: {response.status_code}")
        return None


def test_get_all_groups():
    """Get all groups"""
    response = requests.get(f"{BASE_URL}/groups")
    if response.status_code == 200:
        groups = response.json()
        log_pass(f"Get all groups (found {len(groups)})")
        return groups
    else:
        log_fail("Get all groups", f"Status: {response.status_code}")
        return []


def test_get_group_by_id(group_id):
    """Get group by ID"""
    response = requests.get(f"{BASE_URL}/groups/{group_id}")
    if response.status_code == 200:
        log_pass(f"Get group by ID: {group_id}")
        return response.json()
    else:
        log_fail(f"Get group by ID: {group_id}", f"Status: {response.status_code}")
        return None


def test_delete_group(group_id):
    """Delete group by ID"""
    response = requests.delete(f"{BASE_URL}/groups/{group_id}")
    if response.status_code == 200:
        log_pass(f"Deleted group: {group_id}")
        return True
    else:
        log_fail(f"Delete group: {group_id}", f"Status: {response.status_code}")
        return False


def test_get_group_not_found(group_id):
    """Test 404 for non-existent group"""
    response = requests.get(f"{BASE_URL}/groups/{group_id}")
    if response.status_code == 404:
        log_pass(f"Group not found returns 404 (ID: {group_id})")
        return True
    else:
        log_fail(f"Group not found should return 404", f"Got: {response.status_code}")
        return False


# ============================================
# MEMBER TESTS
# ============================================
def test_add_member(group_id, user_id):
    """Add a member to a group"""
    response = requests.post(f"{BASE_URL}/groups/{group_id}/members", json={
        "userId": user_id
    })
    if response.status_code == 201:
        log_pass(f"Added user {user_id} to group {group_id}")
        return response.json()
    else:
        log_fail(f"Add user {user_id} to group {group_id}", f"Status: {response.status_code}")
        return None


def test_get_members(group_id):
    """Get all members of a group"""
    response = requests.get(f"{BASE_URL}/groups/{group_id}/members")
    if response.status_code == 200:
        members = response.json()
        log_pass(f"Get members of group {group_id} (found {len(members)})")
        return members
    else:
        log_fail(f"Get members of group {group_id}", f"Status: {response.status_code}")
        return []


def test_delete_member(group_id, user_id):
    """Remove a member from a group"""
    response = requests.delete(f"{BASE_URL}/groups/{group_id}/members/{user_id}")
    if response.status_code == 200:
        log_pass(f"Removed user {user_id} from group {group_id}")
        return True
    else:
        log_fail(f"Remove user {user_id} from group {group_id}", f"Status: {response.status_code}")
        return False


# ============================================
# TASK TESTS
# ============================================
def test_create_task(group_id, title, description=None):
    """Create a task in a group"""
    data = {"title": title}
    if description:
        data["description"] = description

    response = requests.post(f"{BASE_URL}/groups/{group_id}/tasks", json=data)
    if response.status_code == 201:
        log_pass(f"Created task: {title}")
        return response.json()
    else:
        log_fail(f"Create task: {title}", f"Status: {response.status_code}")
        return None


def test_get_tasks_by_group(group_id):
    """Get all tasks for a group"""
    response = requests.get(f"{BASE_URL}/groups/{group_id}/tasks")
    if response.status_code == 200:
        tasks = response.json()
        log_pass(f"Get tasks for group {group_id} (found {len(tasks)})")
        return tasks
    else:
        log_fail(f"Get tasks for group {group_id}", f"Status: {response.status_code}")
        return []


def test_get_task_by_id(group_id, task_id):
    """Get task by ID"""
    response = requests.get(f"{BASE_URL}/groups/{group_id}/tasks/{task_id}")
    if response.status_code == 200:
        log_pass(f"Get task by ID: {task_id}")
        return response.json()
    else:
        log_fail(f"Get task by ID: {task_id}", f"Status: {response.status_code}")
        return None


def test_update_task(group_id, task_id, title=None, description=None):
    """Partial update task"""
    data = {}
    if title:
        data["title"] = title
    if description:
        data["description"] = description

    response = requests.patch(f"{BASE_URL}/groups/{group_id}/tasks/{task_id}", json=data)
    if response.status_code == 200:
        log_pass(f"Updated task {task_id}")
        return response.json()
    else:
        log_fail(f"Update task {task_id}", f"Status: {response.status_code}")
        return None


def test_complete_task(group_id, task_id):
    """Mark task as complete"""
    response = requests.put(f"{BASE_URL}/groups/{group_id}/tasks/{task_id}")
    if response.status_code == 200:
        log_pass(f"Marked task {task_id} as complete")
        return True
    else:
        log_fail(f"Complete task {task_id}", f"Status: {response.status_code}")
        return False


def test_delete_task(group_id, task_id):
    """Delete task"""
    response = requests.delete(f"{BASE_URL}/groups/{group_id}/tasks/{task_id}")
    if response.status_code == 200:
        log_pass(f"Deleted task: {task_id}")
        return True
    else:
        log_fail(f"Delete task: {task_id}", f"Status: {response.status_code}")
        return False


def test_get_task_not_found(group_id, task_id):
    """Test 404 for non-existent task"""
    response = requests.get(f"{BASE_URL}/groups/{group_id}/tasks/{task_id}")
    if response.status_code == 404:
        log_pass(f"Task not found returns 404 (ID: {task_id})")
        return True
    else:
        log_fail(f"Task not found should return 404", f"Got: {response.status_code}")
        return False


# ============================================
# MAIN TEST RUNNER
# ============================================
def run_all_tests():
    print(f"\n{BLUE}{'#'*50}")
    print(f"  TASK MANAGER API - AUTOMATED TESTS")
    print(f"  Server: {BASE_URL}")
    print(f"{'#'*50}{RESET}")

    # Check if server is running
    try:
        requests.get(f"{BASE_URL}/users", timeout=5)
    except requests.exceptions.ConnectionError:
        print(f"\n{RED}ERROR: Cannot connect to server at {BASE_URL}")
        print(f"Make sure the server is running with: npm run start:dev{RESET}\n")
        sys.exit(1)

    # ========== USERS ==========
    log_section("USERS")

    user1 = test_create_user("Alice Johnson", f"alice_{TEST_RUN_ID}@example.com")
    user2 = test_create_user("Bob Smith", f"bob_{TEST_RUN_ID}@example.com")

    test_get_all_users()

    if user1:
        test_get_user_by_id(user1["id"])
        test_update_user(user1["id"], "Alice Updated", f"alice.updated_{TEST_RUN_ID}@example.com")

    # ========== GROUPS ==========
    log_section("GROUPS")

    group1 = test_create_group("Development Team", "Frontend and backend developers")
    group2 = test_create_group("Design Team")

    test_get_all_groups()

    if group1:
        test_get_group_by_id(group1["id"])

    # ========== MEMBERS ==========
    log_section("MEMBERS")

    if group1 and user1 and user2:
        test_add_member(group1["id"], user1["id"])
        test_add_member(group1["id"], user2["id"])
        test_get_members(group1["id"])
        test_delete_member(group1["id"], user2["id"])
        test_get_members(group1["id"])

    # ========== TASKS ==========
    log_section("TASKS")

    if group1:
        task1 = test_create_task(group1["id"], "Setup project", "Initialize repository")
        task2 = test_create_task(group1["id"], "Write tests")

        test_get_tasks_by_group(group1["id"])

        if task1:
            test_get_task_by_id(group1["id"], task1["id"])
            test_update_task(group1["id"], task1["id"], title="Setup project - Updated")
            test_complete_task(group1["id"], task1["id"])

            # Verify completion
            updated_task = test_get_task_by_id(group1["id"], task1["id"])
            if updated_task and updated_task.get("completed"):
                log_pass("Task completion verified")
            else:
                log_fail("Task completion verification")

        if task2:
            test_delete_task(group1["id"], task2["id"])

    # ========== 404 TESTS ==========
    log_section("404 ERROR HANDLING")

    test_get_user_not_found(99999)
    test_get_group_not_found(99999)
    if group1:
        test_get_task_not_found(group1["id"], 99999)

    # ========== CLEANUP ==========
    log_section("CLEANUP")
    log_info("Cleaning up test data...")

    # Delete groups (cascades to tasks and members)
    if group1:
        test_delete_group(group1["id"])
    if group2:
        test_delete_group(group2["id"])

    # Delete users
    if user1:
        test_delete_user(user1["id"])
    if user2:
        test_delete_user(user2["id"])

    # ========== SUMMARY ==========
    print(f"\n{BLUE}{'='*50}")
    print(f" TEST SUMMARY")
    print(f"{'='*50}{RESET}")
    print(f"{GREEN}Passed: {passed}{RESET}")
    print(f"{RED}Failed: {failed}{RESET}")
    print(f"Total:  {passed + failed}\n")

    if failed > 0:
        sys.exit(1)


if __name__ == "__main__":
    run_all_tests()
