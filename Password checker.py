#Code has been left with comments throughout to show understanding, majority of
#comments were made during development rather than post development

#uses top 50 most common passwords from nordvpn:
#https://nordpass.com/most-common-passwords-list/
COMMON_PASSWORDS = {
    "123456", "admin", "12345678", "123456789",
    "12345", "password", "Aa123456", "1234567890",
    "Pass@123", "admin123", "1234567", "123123", "111111",
    "12345678910", "P@assw0rd", "Password", "Aa@123456",
    "admintelecom", "Admin@123", "112233", "102030", "654321",
    "abcd1234", "abc123", "qwerty123", "Abcd@1234", "Pass@1234",
    "11223344", "admin@123", "887654321", "987654321", "qwerty",
    "123123123", "1q2w3e4r", "Aa112233", "12341234", "qwertyuiop",
    "11111111", "Admin", "Password@123", "asd123", "Aboy1234",
    "123321", "Admin1", "Admin123", "Demo@123", "1q2w3e4r5t",
    "admin1234", "aa123456", "121212"
}
#special characters
SPECIALS = "!@#$%^&*()-_=+[]{};:'\",.<>/?\\|`~"

def sequential(pw):
    seq = "abcdefghijklmnopqrstuvwxyz"
    nums = "0123456789"
    pw_lower = pw.lower()

#whole password is a pure sequence
    if pw_lower in seq or pw_lower in nums:
        return True

#3+ sequential substring
    for i in range(len(seq) - 2):
        if seq[i:i+3] in pw_lower:
            return True

    for i in range(len(nums) - 2):
        if nums[i:i+3] in pw_lower:
            return True

    return False

#score system
def pass_strength(password):
    score = 0
    feedback = []

    print("\n--- Running checks ---")

#auto fail if common password
    if password.lower() in COMMON_PASSWORDS:
        print("✗ Common password detected (0 points)")
        return None, ["Too common — choose a different password."], 0

    print("✓ Not a common password (+1 point)")
    score += 1

#length
    if len(password) < 8:
        print("✗ Too short (< 8) (0 points)")
        feedback.append("Use at least 8 characters.")
    elif len(password) < 12:
        print("✓ Length OK (8–11) (+1 point)")
        score += 1
    else:
        print("✓ Good length (12+) (+2 points)")
        score += 2

#lowercase
    if any(c.islower() for c in password):
        print("✓ Contains lowercase letters (+1 point)")
        score += 1
    else:
        print("✗ No lowercase letters (0 points)")
        feedback.append("Add lowercase letters.")

#uppercase
    if any(c.isupper() for c in password):
        print("✓ Contains uppercase letters (+1 point)")
        score += 1
    else:
        print("✗ No uppercase letters (0 points)")
        feedback.append("Add uppercase letters.")

#digits
    if any(c.isdigit() for c in password):
        print("✓ Contains numbers (+1 point)")
        score += 1
    else:
        print("✗ No numbers (0 points)")
        feedback.append("Add numbers.")

#special characters
    if any(c in SPECIALS for c in password):
        print("✓ Contains special characters (+1 point)")
        score += 1
    else:
        print("✗ No special characters (0 points)")
        feedback.append("Add special characters.")

#sequential
    if sequential(password):
        print("✗ Contains sequential characters like abc or 123 (0 points)")
        feedback.append("Avoid sequential characters.")
    else:
        print("✓ No obvious sequences (+1 point)")
        score += 1

#repetition
    if len(set(password)) < len(password) / 2:
        print("✗ Too many repeated characters (0 points)")
        feedback.append("Avoid repeating characters too much.")
    else:
        print("✓ Not overly repetitive (+1 point)")
        score += 1

#rating
    if score >= 9:
        strength = "Very strong"
    elif score >= 7:
        strength = "Strong"
    elif score >= 5:
        strength = "Medium"
    else:
        strength = "Weak"

    return strength, feedback, score

#intro
def non_empty_password(show_intro=True):
    if show_intro:
        print("\nWelcome to the password checker!")
        print("Check out my GitHub to see more projects like this:")
        print("https://github.com/RA-DevProjects")
        print(r"""
     ^---^
    ( . . )
    (___'_)
     /   \
    ( | | )___
   (__m_m__)__}
        """)

    while True:
        pwd = input("\nEnter a password to check: ")

        if pwd == "":
            print("[ERROR] Password cannot be empty. Type at least one character.")
        else:
            return pwd


#after checking password
def retry():
    while True:
        print("\nWould you like to:")
        print("1) Check another password")
        print("2) Exit")

        choice = input("> ").strip()

        if choice == "1":
            return True
        elif choice == "2":
            return False
        else:
            print("Invalid choice — please enter 1 or 2.")

def main():
    first_time = True
    while True:
        password = non_empty_password(show_intro=first_time)
        first_time = False

        strength, feedback, score = pass_strength(password)
#auto fail
        if strength is None:
            print("\nPassword invalid due to common password.")
            if not retry():
                break
            continue
#conclusion display
        print("\n=== Result ===")
        print(f"Total score: {score}")
        print(f"Overall strength: {strength}")

        if feedback:
            print("\nSuggestions:")
            for item in feedback:
                print("-", item)
        else:
            print("Great password! ")

        if not retry():
            break

    print("\nGoodbye!")


if __name__ == "__main__":
    main()

