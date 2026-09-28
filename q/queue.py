import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Simple command-line interface.")
    parser.add_argument(
        "command",
        type=str,
        help="Command.",
    )
    args = parser.parse_args()

    return args

def main():
    args = parse_args()

if __name__ == "__main__":
    main()
