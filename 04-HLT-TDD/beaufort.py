def wind_check(speed):
    wind_desc = ""
    if 4 <= speed < 7:
        wind_desc = "Light breeze"
    elif 56 <= speed < 64: 
        wind_desc = "Violent storm"
    else:
        wind_desc = "proably windy"
    return(wind_desc)

print(wind_check(6))