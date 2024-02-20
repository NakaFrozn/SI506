# SI 506 Week 07

from typing import Any, Optional

# fmt: off
# 30%+ sugar content per serving
CEREALS: list[tuple] = [
    ('manufacturer', 'brand', 'slogan', 'serving_size_gm', 'sugar_gm'),
    ('General Mills', 'Cocoa Puffs', "I'm cuckoo for Cocoa Puffs!", 36, 13.4),
    ('Kellogg Company', 'Frosted Flakes', "They're Gr-r-reat!", 41, 14.5),
    ('General Mills', 'Honey Nut Cheerios', 'Have a Change of Heart', 28, 9),
    ('Kellogg Company', 'Raisin Bran', 'Two scoops of raisins in every box.', 59, 18),
    ('Kellogg Company', 'Fruit Loops', 'Follow my nose. It always knows.', 39, 12),
    ('General Mills', 'Lucky Charms', "They're magically delicious.", 36, 13),
    ('Quaker Oats Company', "Cap'n Crunch", "It's got corn for crunch, oats for punch, and it stays crunchy, even in milk.", 27, 12),
    ('Post Consumer Brands', 'Fruity Pebbles', "They're Yabba-Dabba-Delicious!", 27, 9.3),
    ('Kellogg Company', 'Corn Flakes', "Wake up, up, up to Kellogg's Cornflakes!", 29, 10)
]
# fmt: on


def calculate_sugar_content(serving_size_gm: int, sugar_gm: float, precision: int = 2) -> float:
    """Return the sugar content of a cereal as a percentage of the serving size.

    Parameters:
        serving_size_gm (int): The serving size of the cereal in grams.
        sugar_gm (float): The amount of sugar in the cereal in grams.
        precision (int): The number of decimal places to round the return value.

    Returns:
        float: The sugar content of the cereal as a percentage of the serving size.
    """

    return round(sugar_gm / serving_size_gm, precision)


def get_cereal(cereal_brands: list[tuple], cereal_name: str) -> tuple:
    """Return the nested "cereal" tuple matching the < cereal_name > parameter.

    Parameters:
        cereal_brands (list): A list of cereal tuples.
        cereal_name (str): The name of the cereal to locate.

    Returns:
        tuple: The tuple whose name item matches the < cereal_name > parameter. If no
               match is obtained, return < None >.
    """

    for cereal in cereal_brands:
        if cereal_name.lower() in cereal[1].lower():
            return cereal  # match obtained, exit loop and function immediately
    return ()  # empty tuple


def get_cereal_attribute(cereal: tuple, headers: tuple, header: str = "brand") -> Any:
    """Return the value of a < cereal > attribute employing the < headers > tuple to
    look up the index of the target < cereal > attribute.

    Parameters:
        cereal (tuple): A tuple containing cereal data.
        headers (tuple): A tuple containing cereal attribute names.
        header (str): The name of the cereal attribute to return.

    Returns:
        str | int | float: The value of the cereal attribute.
    """

    return cereal[headers.index(header)]


def main() -> None:
    """The < while > loop below is designed to continue looping indefinitely as long as the
    < brand_name > value remains falsy. The loop is terminated when the caller provides a brand name
    that matches on one of the cereal brand names in the < CEREALS > list (partial matches
    accepted).

    The < while > loop will continue to iterate so long as the loop expression < not brand_name >
    evaluates to < True > (i.e., while None is falsy; while not None is truthy). To achieve this,
    the logical operator < not > is employed to reverse the expression (e.g., not brand_name
    evaluates to < True > when the provided input fails to match a sugary cereal). When
    < brand_name > is truthy (e.g, matches a cereal brand name in < CEREALS >) the expression
    < not brand_name > evaluates to < False > and the < while > loop terminates.

    Parameters:
        None

    Returns:
        None
    """

    prompt: str = "\nPlease name a cereal high in sugar: "
    brand_name: Optional[str] = None
    headers: tuple = CEREALS[0]

    while not brand_name:
        name = input(prompt)
        if get_cereal(CEREALS[1:], name):
            cereal: tuple = get_cereal(CEREALS[1:], name)
            brand_name = get_cereal_attribute(cereal, headers)
            serving_size_gm: int = get_cereal_attribute(cereal, headers, "serving_size_gm")
            sugar_gm: float = get_cereal_attribute(cereal, headers, "sugar_gm")
            sugar_content: float = calculate_sugar_content(serving_size_gm, sugar_gm)

            print(
                f"\nOne {serving_size_gm} gm serving of {brand_name}",
                f"contains {sugar_gm} gm of sugar ({sugar_content:.1%}).\n",
            )
        else:
            prompt = "\nCereal not located. Please provide another cereal name: "


if __name__ == "__main__":
    main()
