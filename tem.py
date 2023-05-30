import sys

if __name__ == "__main__":
    # Accessing the command-line arguments
    models = sys.argv[1]
    context = sys.argv[2]
    versions = sys.argv[3]
    uids = sys.argv[4]
    username = sys.argv[5]
    password = sys.argv[6]
    
    # Printing the values for demonstration
    print("Models:", models)
    print("Context:", context)
    print("Versions:", versions)
    print("UIDs:", uids)
    print("Username:", username)
    print("Password:", password)
