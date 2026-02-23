
def phone_book_users():

    users_data= {
        "0568323222": "Amal",
        "0522222232": "Mohammed",
        "0532335983": "Khadijah",
        "0545341144": "Abdullah",
        "0545534556": "Rawan",
        "0560664566": "Faisal",
        "0567917077": "Layla",
}
    
    check_number = input(("Enter your phone number: "))
    
    for n in check_number:
        
        if len(check_number) !=10:
            print("Invalid number")
            
        is_valid = True 
    for n in check_number:
        if n < '0' or n > '9':
            is_valid = False
            break 

    if is_valid == True:
        if check_number in users_data:
           
            print(f"The owner name is: {users_data[check_number]}") 

        else:
            print("Sorry number is not found")  

phone_book_users()
