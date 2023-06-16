from linked_list import LinkedList
from termcolor import colored

def main():
    print(colored("\n~.~ Hello, Welcome To This Program ~.~ \n", "yellow", attrs=["dark"]))
    l = LinkedList()
    while True:
        print(colored("Enter a value for the linked list (or 'done' to finish): ", color="green"), end="")
        value = input()
        if value == "done" or value == "":
            print()
            break
        l.add_node(value)
    l.print_linked_list()
    print(colored("\nThank You For Choosing Us :)\n>>> Developed By Maryam Fakhraei & Amirhossein Naseri <<<",
        "magenta", attrs=["dark"]))
    
if __name__ == "__main__":
    main()