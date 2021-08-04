from beaufort import wind_check

def test_speed():
    assert wind_check(6) == 'Light breeze'
    assert wind_check(59) == 'Violent storm'
    assert wind_check(60) == 'Light breeze'

