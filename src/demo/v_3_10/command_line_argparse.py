import argparse


def main():

    parser = argparse.ArgumentParser(description='Example argparse application')
    parser.add_argument('filename', type=str, help='the filename to process')
    parser.add_argument('--verbose', '-v', action='store_true', help='increase output verbosity')
    parser.add_argument('--save', '-s', action='store_true', help='save the output to file')
    parser.add_argument('--iterations', '-i', type=int, default=1, help='number of iterations to run')

    args = parser.parse_args()
    print(f"Filename: {args.filename}")
    if args.verbose:
        print("Verbose mode is enabled")
    if args.save:
        print("Output will be saved")
    print(f"Iterations: {args.iterations}")


if __name__ == '__main__':
    main()
