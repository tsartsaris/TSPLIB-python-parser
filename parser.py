import argparse

from tsplib_parser.tsp_file_parser import TSPParser


def parse_boolean(value):
    value = value.lower()

    if value in ["true", "yes", "y", "1", "t"]:
        return True
    elif value in ["false", "no", "n", "0", "f"]:
        return False

    return False


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="tsp file to parse.", type=str)
    parser.add_argument("--plot", help="plot the file.", default=False, type=parse_boolean)
    args = parser.parse_args()
    f = args.file
    p = args.plot
    if f is not None:
        TSPParser(filename=f, plot_tsp=p)
    else:
        f = "ulysses16.tsp"
        TSPParser(filename=f, plot_tsp=p)



# d57b652c-7f1b-4713-9ae1-4cac5f06874b