from get_total_points import get_total_points, ninja_belts


def test_get_total_points_basic():
    assert get_total_points(ninja_belts) == 2675
