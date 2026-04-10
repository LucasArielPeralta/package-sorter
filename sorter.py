def sort(width, height, length, mass):
    if min(width, height, length, mass) < 0:
        raise ValueError("Dimensions and mass must be non-negative")

    volume = width * height * length

    bulky = (
        volume >= 1_000_000 or
        width >= 150 or
        height >= 150 or
        length >= 150
    )

    heavy = mass >= 20

    if bulky and heavy:
        return "REJECTED"
    if bulky or heavy:
        return "SPECIAL"
    return "STANDARD"
