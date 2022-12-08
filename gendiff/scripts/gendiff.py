from gendiff.generate_diff import generate_diff
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("first_file")
parser.add_argument("second_file")
parser.add_argument("-f", "--format", help="set format for output")
args = parser.parse_args()


diff = generate_diff(args.first_file, args.second_file)


def main():
    print(diff)


if __name__ == "__main__":
    main()
