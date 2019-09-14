import argparse

def get():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_name", help="The specified file name", type=str)
    parser.add_argument("--name", help="The vscode snippet name", nargs="*", default=["Snippet Name"]) 
    parser.add_argument("--prefix", help="The prefix. e.g. \"for for-const\"", nargs="*", default=["unspecified"])
    parser.add_argument("--desc", help="The description", nargs="*", default=["description"])
    return parser
