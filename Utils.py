SCORES_FILE_NAME = "/Score.txt"
BAD_RETURN_CODE=100
def Screen_cleaner():
    import os
    os.system('cls')  # on Windows System
    for i in range(1, 30):
        print(" " * i)

