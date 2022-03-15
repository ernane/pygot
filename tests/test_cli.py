from pygot.cli import cli


def test_houses(cli_runner):
    response = cli_runner.invoke(cli, ["houses"])
    assert response.exit_code == 0
    assert "House Algood" in response.output


def test_books(cli_runner):
    response = cli_runner.invoke(cli, ["books"])
    assert response.exit_code == 0
    assert "A Game of Thrones" in response.output


def test_book(cli_runner):
    response = cli_runner.invoke(cli, ["book", "--id", "2"])
    assert response.exit_code == 0
    assert "A Clash of Kings" in response.output


def test_filtering_books(cli_runner):
    response = cli_runner.invoke(
        cli, ["filtering_books", "--name", "A Game of Thrones"]
    )
    assert response.exit_code == 0
    assert "A Game of Thrones" in response.output


def test_characters(cli_runner):
    response = cli_runner.invoke(cli, ["characters"])
    assert response.exit_code == 0
    assert "Walder" in response.output
