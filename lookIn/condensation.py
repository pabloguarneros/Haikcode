def condensation(water_particle, inside, outside):
    dewpoint_22_celsius = { "0": -22, "10": -11, "20": 2, "30": 4, "40": 8, "50": 11,
                            "60": 14, "70": 17, "80": 19, "90": 20, "100": 22 }
    
    temp_diff = inside.temp - outside.temp
    relative_humidity = outside.humidity
    
    if temp_diff > 0:
        water_particle.temp -= temp_diff * 2
        if water_particle.temp <= dewpoint_22_celsius[f"{relative_humidity}"]:
            water_particle.isLiquid = True