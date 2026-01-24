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
CYAN = "\033[96m"
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
    print(f"\n{BLUE}{'='*60}")
    print(f" {title}")
    print(f"{'='*60}{RESET}\n")


def log_subsection(title):
    print(f"\n{CYAN}--- {title} ---{RESET}\n")


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
        log_fail(f"Create user: {name}", f"Status: {response.status_code}, Body: {response.text}")
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


def test_update_user(user_id, name=None, email=None):
    """Update user by ID"""
    data = {}
    if name:
        data["name"] = name
    if email:
        data["email"] = email

    response = requests.put(f"{BASE_URL}/users/{user_id}", json=data)
    if response.status_code == 200:
        log_pass(f"Updated user {user_id}")
        return response.json()
    else:
        log_fail(f"Update user {user_id}", f"Status: {response.status_code}")
        return None


def test_get_user_groups(user_id):
    """Get groups that a user belongs to"""
    response = requests.get(f"{BASE_URL}/users/{user_id}/groups")
    if response.status_code == 200:
        result = response.json()
        groups = result.get("groups", []) if result else []
        log_pass(f"Get user {user_id} groups (found {len(groups)})")
        return result
    else:
        log_fail(f"Get user {user_id} groups", f"Status: {response.status_code}")
        return None


def test_delete_user(user_id):
    """Delete user by ID"""
    response = requests.delete(f"{BASE_URL}/users/{user_id}")
    if response.status_code == 200:
        log_pass(f"Deleted user: {user_id}")
        return response.json()
    else:
        log_fail(f"Delete user: {user_id}", f"Status: {response.status_code}")
        return None


def test_get_user_not_found(user_id):
    """Test 404 for non-existent user"""
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    if response.status_code == 404:
        log_pass(f"User not found returns 404 (ID: {user_id})")
        return True
    else:
        log_fail(f"User not found should return 404", f"Got: {response.status_code}")
        return False


def test_user_exists(user_id):
    """Check if user exists (returns True/False, no logging)"""
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    return response.status_code == 200


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


def test_group_exists(group_id):
    """Check if group exists (returns True/False, no logging)"""
    response = requests.get(f"{BASE_URL}/groups/{group_id}")
    return response.status_code == 200


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


def test_update_task(group_id, task_id, title=None, description=None, completed=None):
    """Partial update task"""
    data = {}
    if title is not None:
        data["title"] = title
    if description is not None:
        data["description"] = description
    if completed is not None:
        data["completed"] = completed

    response = requests.patch(f"{BASE_URL}/groups/{group_id}/tasks/{task_id}", json=data)
    if response.status_code == 200:
        log_pass(f"Updated task {task_id}")
        return response.json()
    else:
        log_fail(f"Update task {task_id}", f"Status: {response.status_code}")
        return None


def test_complete_task(group_id, task_id):
    """Mark task as complete using PATCH /complete endpoint"""
    response = requests.patch(f"{BASE_URL}/groups/{group_id}/tasks/{task_id}/complete")
    if response.status_code == 200:
        log_pass(f"Marked task {task_id} as complete")
        return response.json()
    else:
        log_fail(f"Complete task {task_id}", f"Status: {response.status_code}")
        return None


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


def test_task_exists(group_id, task_id):
    """Check if task exists (returns True/False, no logging)"""
    response = requests.get(f"{BASE_URL}/groups/{group_id}/tasks/{task_id}")
    return response.status_code == 200


# ============================================
# MAIN TEST RUNNER
# ============================================
def run_all_tests():
    print(f"\n{BLUE}{'#'*60}")
    print(f"  TASK MANAGER API - COMPREHENSIVE TEST SUITE")
    print(f"  Server: {BASE_URL}")
    print(f"{'#'*60}{RESET}")

    # Check if server is running
    try:
        requests.get(f"{BASE_URL}/users", timeout=5)
    except requests.exceptions.ConnectionError:
        print(f"\n{RED}ERROR: Cannot connect to server at {BASE_URL}")
        print(f"Make sure the server is running with: npm run start:dev{RESET}\n")
        sys.exit(1)

    # ========== USERS CRUD ==========
    log_section("1. USERS - CRUD Operations")

    user1 = test_create_user("Alice Johnson", f"alice_{TEST_RUN_ID}@example.com")
    user2 = test_create_user("Bob Smith", f"bob_{TEST_RUN_ID}@example.com")
    user3 = test_create_user("Charlie Brown", f"charlie_{TEST_RUN_ID}@example.com")

    test_get_all_users()

    if user1:
        test_get_user_by_id(user1["id"])
        test_update_user(user1["id"], name="Alice Updated")
        test_update_user(user1["id"], email=f"alice.new_{TEST_RUN_ID}@example.com")

    # ========== GROUPS CRUD ==========
    log_section("2. GROUPS - CRUD Operations")

    group1 = test_create_group("Development Team", "Frontend and backend developers")
    group2 = test_create_group("Design Team")
    group3 = test_create_group("Solo Group", "Group with only one member")

    test_get_all_groups()

    if group1:
        test_get_group_by_id(group1["id"])

    # ========== MEMBERS ==========
    log_section("3. MEMBERS - Add/Remove Members")

    if group1 and user1 and user2:
        test_add_member(group1["id"], user1["id"])
        test_add_member(group1["id"], user2["id"])
        test_get_members(group1["id"])

    if group2 and user2:
        test_add_member(group2["id"], user2["id"])

    if group3 and user3:
        test_add_member(group3["id"], user3["id"])

    log_subsection("Get User's Groups")
    if user2:
        test_get_user_groups(user2["id"])

    log_subsection("Remove Member")
    if group1 and user2:
        test_delete_member(group1["id"], user2["id"])
        test_get_members(group1["id"])

    # ========== TASKS CRUD ==========
    log_section("4. TASKS - CRUD Operations")

    task1 = task2 = task3 = None
    if group1:
        task1 = test_create_task(group1["id"], "Setup project", "Initialize repository")
        task2 = test_create_task(group1["id"], "Write tests", "Add unit tests")
        task3 = test_create_task(group1["id"], "Deploy app")

        test_get_tasks_by_group(group1["id"])

        if task1:
            test_get_task_by_id(group1["id"], task1["id"])

    log_subsection("Update Task Fields")
    if group1 and task1:
        test_update_task(group1["id"], task1["id"], title="Setup project - UPDATED")
        test_update_task(group1["id"], task1["id"], description="New description")

    log_subsection("Complete Task via PATCH /complete")
    if group1 and task1:
        result = test_complete_task(group1["id"], task1["id"])
        if result and result.get("completed") == True:
            log_pass("Task completion verified (completed=true)")
        else:
            log_fail("Task completion verification", f"Expected completed=true, got: {result}")

    log_subsection("Complete Task via PATCH with completed field")
    if group1 and task2:
        result = test_update_task(group1["id"], task2["id"], completed=True)
        if result and result.get("completed") == True:
            log_pass("Task completed via PATCH body (completed=true)")
        else:
            log_fail("Task completion via PATCH body", f"Expected completed=true, got: {result}")

    log_subsection("Delete Task")
    if group1 and task3:
        test_delete_task(group1["id"], task3["id"])
        test_get_task_not_found(group1["id"], task3["id"])

    # ========== 404 TESTS ==========
    log_section("5. ERROR HANDLING - 404 Not Found")

    test_get_user_not_found(99999)
    test_get_group_not_found(99999)
    if group1:
        test_get_task_not_found(group1["id"], 99999)

    # ========== CASCADE DELETE: Group -> Tasks ==========
    log_section("6. CASCADE DELETE - Group Deletion")
    log_info("Deleting a group should delete all its tasks")

    cascade_group = test_create_group("Cascade Test Group")
    cascade_task1 = cascade_task2 = None
    if cascade_group:
        cascade_task1 = test_create_task(cascade_group["id"], "Cascade Task 1")
        cascade_task2 = test_create_task(cascade_group["id"], "Cascade Task 2")

        log_info(f"Created group {cascade_group['id']} with tasks {cascade_task1['id']}, {cascade_task2['id']}")

        # Delete group
        test_delete_group(cascade_group["id"])

        # Verify group is gone
        if not test_group_exists(cascade_group["id"]):
            log_pass("Group deleted successfully")
        else:
            log_fail("Group should be deleted")

        # Verify tasks are gone (cascade)
        # Note: We can't check tasks directly since group is gone,
        # but if we had a global task endpoint we could verify

    # ========== CASCADE DELETE: User -> Empty Groups ==========
    log_section("7. CASCADE DELETE - User Deletion (Empty Groups)")
    log_info("Deleting a user should remove them from groups")
    log_info("If a group becomes empty, it should be deleted along with its tasks")

    # Create isolated test data
    cascade_user = test_create_user("Cascade User", f"cascade_{TEST_RUN_ID}@example.com")
    cascade_group2 = test_create_group("User Cascade Group")
    cascade_task3 = None

    if cascade_user and cascade_group2:
        # Add user as the ONLY member
        test_add_member(cascade_group2["id"], cascade_user["id"])

        # Create a task in this group
        cascade_task3 = test_create_task(cascade_group2["id"], "Orphan Task")

        log_info(f"User {cascade_user['id']} is the only member of group {cascade_group2['id']}")
        log_info(f"Group has task {cascade_task3['id'] if cascade_task3 else 'N/A'}")

        # Delete the user
        log_info(f"Deleting user {cascade_user['id']}...")
        test_delete_user(cascade_user["id"])

        # Verify user is gone
        if not test_user_exists(cascade_user["id"]):
            log_pass("User deleted successfully")
        else:
            log_fail("User should have been deleted")

        # Verify group is gone (was empty after user removal)
        if not test_group_exists(cascade_group2["id"]):
            log_pass("Empty group was automatically deleted")
        else:
            log_fail("Empty group should have been deleted")

    # ========== USER IN MULTIPLE GROUPS ==========
    log_section("8. CASCADE DELETE - User in Multiple Groups")
    log_info("Deleting a user in multiple groups should only delete EMPTY groups")

    multi_user = test_create_user("Multi User", f"multi_{TEST_RUN_ID}@example.com")
    other_user = test_create_user("Other User", f"other_{TEST_RUN_ID}@example.com")
    shared_group = test_create_group("Shared Group")
    solo_group2 = test_create_group("Solo Group 2")

    if multi_user and other_user and shared_group and solo_group2:
        # Add multi_user to both groups
        test_add_member(shared_group["id"], multi_user["id"])
        test_add_member(solo_group2["id"], multi_user["id"])

        # Add other_user to shared_group (so it won't be empty)
        test_add_member(shared_group["id"], other_user["id"])

        log_info(f"multi_user is in: shared_group (with other_user) and solo_group2 (alone)")

        # Delete multi_user
        log_info(f"Deleting multi_user...")
        test_delete_user(multi_user["id"])

        # shared_group should still exist (has other_user)
        if test_group_exists(shared_group["id"]):
            log_pass("Shared group still exists (has remaining members)")
        else:
            log_fail("Shared group should NOT be deleted (has remaining members)")

        # solo_group2 should be deleted (was empty)
        if not test_group_exists(solo_group2["id"]):
            log_pass("Solo group was deleted (became empty)")
        else:
            log_fail("Solo group should be deleted (became empty)")

        # Cleanup remaining
        test_delete_group(shared_group["id"])
        test_delete_user(other_user["id"])

    # ========== CLEANUP ==========
    log_section("9. CLEANUP")
    log_info("Cleaning up remaining test data...")

    # Delete groups first (cascades to tasks)
    if group1:
        test_delete_group(group1["id"])
    if group2:
        test_delete_group(group2["id"])
    if group3:
        test_delete_group(group3["id"])

    # Delete users
    if user1:
        test_delete_user(user1["id"])
    if user2:
        test_delete_user(user2["id"])
    if user3:
        test_delete_user(user3["id"])

    # ========== SUMMARY ==========
    print(f"\n{BLUE}{'='*60}")
    print(f" TEST SUMMARY")
    print(f"{'='*60}{RESET}")
    print(f"{GREEN}Passed: {passed}{RESET}")
    print(f"{RED}Failed: {failed}{RESET}")
    print(f"Total:  {passed + failed}")

    if failed == 0:
        print(f"\n{GREEN}All tests passed!{RESET}\n")
    else:
        print(f"\n{RED}Some tests failed. Review output above.{RESET}\n")
        sys.exit(1)


if __name__ == "__main__":
    run_all_tests()
