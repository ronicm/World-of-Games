# test_scores_service - it’s purpose is to test our web service. It will get the application
# URL as an input, open a browser to that URL, select the score element in our web page,
# check that it is a number between 1 to 1000 and return a boolean value if it’s true or not.
import sys


def test_scores_service(app_url):
    from selenium import webdriver
    my_chrom = webdriver.Chrome(executable_path='C:\Drivers\chromedriver_win32\chromedriver.exe')
    my_chrom.get(app_url)
    text: int
    try:
        score_value = (my_chrom.find_element_by_id("scor"))

        if int(score_value.text) in range(1, 100):
            # print( "between 1 to 100")
            return True
        else:
            # print("not between 1 to 100")
            return False
    except Exception as e:
        print("exception-failed to get the score - ", e)
        return False


# main_function to call our tests function. The main function will return -1 as an OS exit
# code if the tests failed and 0 if they passed.
#
#
def main_function(URL):
    import sys
    if test_scores_service(URL):
        print("success")
        sys.exit(0)
    else:
        print("failed")
        sys.exit(-1)


#
#
#
#
#


# main_function("http://127.0.0.1:5000/")
