
from chromebrowser import ChromeBrowser


def main():
    webpage_url = "http://www.python.org"
    actions = {}
    browser = ChromeBrowser(webpage_url, actions)
    browser.example_routine()
    return 0


if __name__ == "__main__":
    main()
