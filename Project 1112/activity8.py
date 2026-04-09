# Shutdown Function with Conditions

def shutdown(response):
    if response == "Yes":
        print("Shutting down...")
    elif response == "No":
        print("Abort shut down.")
    else:
        print("Sorry.")

user_input = input("Do you want to shutdown? (Yes/No): ")

shutdown(user_input)