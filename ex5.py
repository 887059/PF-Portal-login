print("_Welcome to EPFO Portal_")
print("Go to the home page and select your services")

list_service = ["for employers", "for employees", "for international workers"]
print("Available Services:", list_service)

your_choice = input("Choose your service: ")

if your_choice in list_service:
    print("Go to the next page")
else:
    print("Choose another service")

login_with = input("Login with (UAN/Adhar): ")

Actual_UAN = "1234567890"
correct_password = "Parkavi@123"

account_Number = input("Enter your UAN Number: ")
password = input("Enter your Password: ")

if account_Number==Actual_UAN and password==correct_password:
    print("Login successfully..! Welcome to the UAN portal")
else:
    print("Login failed..! Please check your credentials")

employees_service = input("Choose a service (1. View Passbook, 2. Claim Online, 3. Claim Status, others, download UAN card): ")

if employees_service=="1" or employees_service=="2" or employees_service=="3" or employees_service=="others" or employees_service == "download UAN card":
    print("Your selected service is ready.")
else:
    print("Your service is not available in the portal.")