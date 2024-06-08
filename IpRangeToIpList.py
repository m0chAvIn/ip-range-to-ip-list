import os
import platform
import ipaddress

def clear_terminal():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def ip_range_to_list(ip_range):
    ip_list = []
    network = ipaddress.ip_network(ip_range, strict=False)
    for ip in network:
        ip_list.append(str(ip))
    return ip_list

def input_from_file(file_path):
    with open(file_path, "r") as file:
        ip_range = file.readline().strip()
    return ip_range

if __name__ == "__main__":
    clear_terminal()

    # ASCII art logo with color
    logo = """
    \033[38;2;216;4;4m
    ███████╗██╗     ███████╗██████╗ ██████╗ ██╗   ██╗
    ██╔════╝██║     ██╔════╝╚════██╗██╔══██╗╚██╗ ██╔╝
    ███████╗██║     █████╗   █████╔╝██████╔╝ ╚████╔╝ 
    ╚════██║██║     ██╔══╝   ╚═══██╗██╔═══╝   ╚██╔╝  
    ███████║███████╗███████╗██████╔╝██║        ██║   
    ╚══════╝╚══════╝╚══════╝╚═════╝ ╚═╝        ╚═╝   
    \033[0m
    """
    print(logo)

    user_input = input("Enter The IP Range File: ")

    # Checking if the input is a file path
    if os.path.isfile(user_input):
        ip_range = input_from_file(user_input)
    else:
        ip_range = user_input

    ip_list = ip_range_to_list(ip_range)
    output_filename = input("Enter the name of the output file (without extension): ")
    output_file = output_filename + ".txt"
    with open(output_file, "w") as file:
        for ip in ip_list:
            file.write(ip + "\n")
    print("IP addresses within the range saved to", output_file)
