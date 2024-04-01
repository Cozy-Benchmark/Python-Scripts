import subprocess
from datetime import date

def main():
    today = date.today()
    title = today.strftime("%Y-%m-%d")

    file_name = f"{title}.txt"
    path = f"D:\\Bench\\Reports\\{file_name}"
    with open(path, "w") as file:
        file.write(f'Date: {title}')
        file.write(f'\nTasked Accomplished:')
        file.write(f'\nRemarks:')
        
    subprocess.Popen(['notepad' ,path])

if __name__ == "__main__":
    main()
