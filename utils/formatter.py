def format_temp(celsius):
    fahrenheit = celsius * 9 / 5 + 32

    return f"{celsius}°C ({round(fahrenheit, 1)}°F)"