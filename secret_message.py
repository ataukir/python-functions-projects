import os


def rename_files():
    # get the files names
    file_list = os.listdir(r"C:\Users\User\Documents\GitHub\python-functions-projects\prank")

    print(file_list)

    saved_path = os.getcwd()
    print("current working directory" + saved_path)
    os.chdir(r"C:\Users\User\Documents\GitHub\python-functions-projects\prank")
    # for each file name rename filename
    for filen in file_list:
        table = str.maketrans(dict.fromkeys("0123456789"))
        # filen.translate(table)
        os.rename(filen, filen.translate(table))

    os.chdir(saved_path)
    print(file_list)

rename_files()
