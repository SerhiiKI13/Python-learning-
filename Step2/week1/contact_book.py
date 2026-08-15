def main():
    contacts = []
    while True:
        num = int(input(
    """
    1.Add contact 
    2.Show contact
    3.Find contact
    4.Delete contact
    5.Exit
    """
        ))
        if num == 1:
            name = input("Enter name: ")
            phone = int(input("Enter the phone: "))
            add_contact(contacts,name,phone)
        elif num == 2:
            print(show_contacts(contacts))
        elif num == 3:
            name = input("Enter the name of the contact you want to find: ")
            print(find_contact(contacts,name))
        elif num == 4:
            name = input("Enter the name: ")
            print(delete_contact(contacts,name))
            
        else:
            print("End")
            break
        
def add_contact(contacts,name,phone):
    c = {"name": name,"phone": phone}
    contacts.append(c)
    return contacts

def show_contacts(contacts):
    if len(contacts) >= 1:
        return contacts
    else:
        return "Нету контактов"
    
def find_contact(contacts,name):
    for n in contacts:
        if n['name'] == name:
         return n  
    else:
     return "Contact not found"   
        
        
def delete_contact(contacts,name):
   for contact in contacts:
       if contact['name'] == name:
         contacts.remove(contact)
         return "Контакт удален"
   else:
        return "Contact not found"
    
main()