from gym_customer import GymCustomer
from gym_management import GymManagement
from gym_management import Regimen


def customer_functionalities():
    while True:
        mobile_number = input('Enter Your mobile Number: ')
        gym_management = GymManagement()
        customer = gym_management.get_customer_by_mobile_number(mobile_number)

        if customer is None:
            print("No customer details found for given mobile number.")
            continue
        break

    while True:

        print('Please select option from below to proceed, \n1.My Regimen\n2. My Profile\n0. Exit')

        cust_choice = int(input("Your selection: "))
        print('--------------------')

        if cust_choice == 1:
            customer = gym_management.get_customer_by_mobile_number(mobile_number)
            customer.get_display_obj()
            regimen = customer.get_regimen()
            regimen.get_display_obj()

        elif cust_choice == 2:
            customer = gym_management.get_customer_by_mobile_number(mobile_number)
            customer.get_display_obj()
        elif cust_choice == 0:
            break


def super_admin_functionalities():

    while True:
        print('Please select option from below to proceed, \n1. Create Member\n2. View Member\n3. Delete Member\n4. '
              'Update Member\n5. Create Regimen\n6. View Regimen\n7. Delete Regimen\n8.Update Regimen\n0. Exit')

        admin_choice = int(input("Your selection: "))

        print('--------------------')
        gym_management = GymManagement()

        if admin_choice == 1:  # Create member

            name = input("Customer's Name: ")
            age = int(input("Customer's age: "))
            gender = input("Customer's Gender(M/F): ")
            mobile_number = input("Customer's Mobile Number: ")
            email_id = input("Customer's Email Id: ")
            bmi = int(input("Customer's BMI: "))
            membership_duration = input("MemberShip Duration in months: ")
            regimen = {}
            if bmi < 18.5:
                regimen = Regimen('Chest', 'Biceps', 'Rest', 'Back', 'Triceps', 'Rest', 'Rest')
            elif bmi < 25:
                regimen = Regimen('Chest', 'Biceps', 'Cardio/Abs', 'Back', 'Triceps', 'Legs', 'Rest')
            elif bmi <= 30:
                regimen = Regimen('Chest', 'Biceps', 'Abs/Cardio', 'Back', 'Triceps', 'Legs', 'Cardio')
            elif bmi > 30:
                regimen = Regimen('Chest', 'Biceps', 'Cardio', 'Back', 'Triceps', 'Cardio', 'Cardio')

            customer = GymCustomer(name, age, gender, mobile_number, email_id, bmi, membership_duration, regimen)
            gym_management.add_customer(customer)

        elif admin_choice == 2:   # View member
            mobile_number = input("Customer's Mobile Number: ")

            customer = gym_management.get_customer_by_mobile_number(mobile_number)

            if customer is None:
                print('No customer exist for given mobile number!!')
            else:
                customer.get_display_obj()
        elif admin_choice == 3:  # Delete member
            mobile_number = input("Customer's Mobile Number: ")
            gym_management.delete_customer(mobile_number)
        elif admin_choice == 4:   # Update member
            mobile_number = input("Customer's Mobile Number: ")
            customer = gym_management.get_customer_by_mobile_number(mobile_number)

            if customer is None:
                print("No customer found for given mobile number!!")
                continue
            choice = input("Do you want to revoke or extend membership?(revoke/extend): ")

            if choice == 'extend':
                membership_duration = int(input("New MemberShip Duration in months: "))

                if membership_duration == 0:
                    selection = input("Membership will be revoked. Do you want to continue?(y/n)")
                    if selection == 'n':
                        continue
                else:
                    mem = customer.get_membership_duration()
                    membership_duration = int(mem) + membership_duration
            elif choice == 'revoke':
                membership_duration = 0
            else:
                print("Invalid choice!!")
                continue

            customer = customer.set_membership_duration(membership_duration)

            gym_management.add_customer(customer)

        elif admin_choice == 5:  # Create regimen
            regiment_name = input("Enter the name for regimen: ")
            mon = input("Workout for Monday: ")
            tue = input("Workout for Tuesday: ")
            wed = input("Workout for Wednesday: ")
            thus = input("Workout for Thursday: ")
            fri = input("Workout for Friday: ")
            sat = input("Workout for Saturday: ")
            sun = input("Workout for Sunday: ")

            regimen = Regimen(mon, tue, wed, thus, fri, sat, sun)
            regimen.add_regimen(regiment_name)

        elif admin_choice == 6:  # View regimen
            regimen_name = input("Enter the name of regimen: ")
            regimen = Regimen()
            regimen = regimen.get_regimen_by_name(regimen_name)

            if regimen is None:
                print("No regiment found for given name !!")
                continue
            regimen.get_display_obj()
        elif admin_choice == 7:  # Delete regimen
            regimen_name = input("Enter the name of regimen: ")
            regimen = Regimen()
            regimen = regimen.get_regimen_by_name(regimen_name)
            regimen.delete_regimen(regimen_name)
        elif admin_choice == 8:  # Update regimen
            regimen_name = input("Enter the name of regimen: ")
            regimen = Regimen()
            regimen = regimen.get_regimen_by_name(regimen_name)
            if regimen is None:
                print("Invalid regimen name!!")
                continue
            mon = input("Workout for Monday")
            tue = input("Workout for Tuesday")
            wed = input("Workout for Wednesday")
            thus = input("Workout for Thursday")
            fri = input("Workout for Friday")
            sat = input("Workout for Saturday")
            sun = input("Workout for Sunday")

            regimen = Regimen(mon, tue, wed, thus, fri, sat, sun)
            regimen.add_regimen(regiment_name)

        elif admin_choice == 0:
            break


print("Welcome to Gym cli")

while True:

    print("Please select option from below to proceed,\n1. Admin\n2. Customer\n0. Exit")
    user_choice = int(input("Your selection: "))

    if user_choice == 1:
        super_admin_functionalities()
    elif user_choice == 2:
        customer_functionalities()
    if user_choice == 0:
        break

