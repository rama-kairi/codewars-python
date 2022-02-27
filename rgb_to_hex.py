# The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

# Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

# The following are examples of expected output values:

# rgb(255, 255, 255) # returns FFFFFF
# rgb(255, 255, 300) # returns FFFFFF
# rgb(0,0,0) # returns 000000
# rgb(148, 0, 211) # returns 9400D3


def rgb_to_hex(rgb: tuple) -> str:
    return "".join(hex(x)[2:].zfill(2) for x in rgb)


def rgb_to_hex_v2(r: int, g: int, b: int) -> str:
    return "{:02x}{:02x}{:02x}".format(
        min(max(r, 0), 255),
        min(max(g, 0), 255),
        min(max(b, 0), 255),
    ).upper()


# def rgb_to_hex_v3(r: int, g: int, b: int) -> str:
#     return "".join(map(lambda x: "{:02X}".format(min(max(0, x), 255)), args))


if __name__ == "__main__":
    print(rgb_to_hex_v2(255, 255, 255))
    print(rgb_to_hex_v2(-20, 275, 125))
    print(rgb_to_hex_v2(255, 255, 300))
    print(rgb_to_hex_v2(0, 0, 0))
    print(rgb_to_hex_v2(148, 0, 211))
