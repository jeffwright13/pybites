from game_stats import print_game_stats

games_won = dict(sara=0, bob=1, tim=5, julian=3, jim=1)

dict0 = {}
output0 = ""

dict1 = dict(sara=0, bob=1, andrew=2, jordan=100)
output1 = """sara has won 0 games
bob has won 1 game
andrew has won 2 games
jordan has won 100 games"""

dict2 = dict(bob=1, andrew=2, jordan=100)
output2 = """bob has won 1 game
andrew has won 2 games
jordan has won 100 games"""

dict3 = dict(andrew=2, jordan=100)
output3 = """andrew has won 2 games
jordan has won 100 games"""

def test_print_game_stats_0(capfd):
    print_game_stats(dict0)
    output = capfd.readouterr()[0].strip()
    assert output == output0


def test_print_game_stats_1(capfd):
    print_game_stats(dict1)
    output = capfd.readouterr()[0].strip()
    assert output == output1


def test_print_game_stats_2(capfd):
    print_game_stats(dict2)
    output = capfd.readouterr()[0].strip()
    print(output, type(output))
    assert output == output2


def test_print_game_stats_3(capfd):
    print_game_stats(dict3)
    output = capfd.readouterr()[0].strip()
    assert output == output3

