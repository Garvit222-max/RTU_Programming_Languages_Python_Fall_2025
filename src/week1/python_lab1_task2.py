# Name: Garvit
# Student ID: 241ADB140

def greet_user(name):
    """Return a greeting message after cleaning and capitalizing the name."""
    clean_name = name.strip().capitalize()
    return f"Hello, {clean_name}! Welcome to Python!"

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    greeting = greet_user(user_name)
    print(greeting)
