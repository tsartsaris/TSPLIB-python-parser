from tsplib_parser.tsp_file_parser import TSPParser, read_tsp_file_contents, check_filename_tsp


def test_on_file_selected():
    filename = "./ulysses16.tsp"
    TSPParser(filename=filename, plot_tsp=False)
    assert TSPParser.filename == filename
    assert TSPParser.should_plot is False


def test_open_tsp_file():
    filename = "./ulysses16.tsp"
    TSPParser(filename=filename, plot_tsp=False)
    assert len(TSPParser.tsp_file_contents) == 23


def test_detect_dimension():
    filename = "./ulysses16.tsp"
    TSPParser(filename=filename, plot_tsp=False)
    assert TSPParser.dimension == 16


def test_get_cities_dict():
    filename = "./ulysses16.tsp"
    TSPParser(filename=filename, plot_tsp=False)
    assert len(TSPParser.tsp_cities_dict) == 16


def test_clear_data():
    filename = "./ulysses16.tsp"
    TSPParser(filename=filename, plot_tsp=False)
    TSPParser.clear_data()
    assert TSPParser.filename == ""


def test_read_tsp_file_contents():
    filename = "./ulysses16.tsp"
    content = read_tsp_file_contents(filename)
    assert 'DIMENSION: 16' in content
    assert len(content) == 23


def test_check_filename_tsp():
    filename = "./ulysses16.tsp"
    assert check_filename_tsp(filename) is True
    filename = "whatever"
    assert check_filename_tsp(filename) is False
