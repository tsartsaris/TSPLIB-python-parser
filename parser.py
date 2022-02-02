import argparse

from tsplib_parser.tsp_file_parser import TSPParser


def parse_boolean(value: str) -> bool:
    value = value.lower()

    if value in ["true", "yes", "y", "1", "t"]:
        return True
    elif value in ["false", "no", "n", "0", "file_name"]:
        return False

    return False


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="tsp file to parse.", type=str)
    parser.add_argument("--plot", help="plot the file.", default=False, type=parse_boolean)
    args = parser.parse_args()
    file_name: str = args.file
    should_plot: bool = args.plot
    if file_name is not None:
        TSPParser(filename=file_name, plot_tsp=should_plot)
    else:
        file_name = "ulysses16.tsp"
        TSPParser(filename=file_name, plot_tsp=should_plot)

# d57b652c-7f1b-4713-9ae1-4cac5f06874b
