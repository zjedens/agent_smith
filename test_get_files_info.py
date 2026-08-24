
from functions.get_files_info import get_files_info

if __name__ == "__main__":
    print(get_files_info("calculdator", "."))
    print(get_files_info("calculdator", "/bin"))
    print(get_files_info("calculdator", "../"))
    print(get_files_info("calculdator", "main.py"))
    
