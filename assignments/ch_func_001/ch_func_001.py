# SI 506 Week 06 Bonus Challenge


def calculate_sugar_content(serving_size_gm, sugar_gm, precision=2, format_pct=False):
    if format_pct:
        return f"{sugar_gm / serving_size_gm * 100:.{precision}f}%"  # trailing % sign
    else:
        return round(sugar_gm / serving_size_gm, precision)


def get_cereal_attribute(cereal, headers, header="brand"):
    return cereal[headers.index(header)]


def get_lowest_sugar_content(cereals, headers):
    min_sugar_content = []
    min_sugar_gm = float("inf")
    for cereal in cereals:
        brand = get_cereal_attribute(cereal, headers, "brand")
        serving_size_gm = get_cereal_attribute(cereal, headers, "serving_size_gm")
        sugar_gm = get_cereal_attribute(cereal, headers, "sugar_gm")
        sugar_content = calculate_sugar_content(serving_size_gm, sugar_gm)

        if sugar_content < min_sugar_gm:
            min_sugar_gm = sugar_content
            min_sugar_content.clear()  # reset
            min_sugar_content.append(brand)  # name only
        elif sugar_content == min_sugar_gm:
            min_sugar_content.append(brand)  # name only
        else:
            continue  # explicit but optional

    return min_sugar_content


def main():
    # fmt: off
    data = [
        ["manufacturer", "brand", "slogan", "serving_size_gm", "sugar_gm"],
        ["Post Consumer Brands", "Honey Bunches of Oats", "Taste the joy in every spoonful.", 30, 6],
        ["General Mills", "Cocoa Puffs", "I'm cuckoo for Cocoa Puffs!", 36, 13.4],
        ["Kellogg Company", "Frosted Flakes", "They're Gr-r-reat!", 41, 14.5],
        ["General Mills", "Honey Nut Cheerios", "Have a Change of Heart", 28, 9],
        ["Post Consumer Brands", "Grape-nuts", "Ever eat a pine tree? Many parts are edible.", 29, 4.4],
        ["Kellogg Company", "Raisin Bran", "Two scoops of raisins in every box.", 59, 18],
        ["General Mills", "Cheerios", "Go with the Goodness of Cheerios.", 28, 1.3],
        ["Kellogg Company", "Fruit Loops", "Follow my nose. It always knows.", 39, 12],
        ["Post Consumer Brands", "Shredded Wheat", "Bet you can't eat three.", 50, 0.46],
        ["UMSI Kitchens", "Data morsels", "Information changes everything.", 50, 0.46],
        ["Three Wishes Foods", "Honey grain free cereal", "So Good It Should Be Forbidden.", 35, 3],
        ["General Mills", "Lucky Charms", "They're magically delicious.", 36, 13],
        ["Quaker Oats Company", "Cap'n Crunch", "It's got corn for crunch, oats for punch, and it stays crunchy, even in milk.", 27, 12,],
        ["Post Consumer Brands", "Fruity Pebbles", "They're Yabba-Dabba-Delicious!", 27, 9.3],
        ["Kellogg Company", "Corn Flakes", "Wake up, up, up to Kellogg's Cornflakes!", 29, 10],
        ["Kellogg Company", "Apple Jacks", "We eat what we like.", 28, 8],
        ["General Mills", "Wheaties", "The Breakfast of Champions", 27, 4.1],
    ]
    # fmt: on

    min_sugar_cereals = get_lowest_sugar_content(headers=data[0], cereals=data[1:])

    print(f"\nCereals min sugar content = {min_sugar_cereals}")

    assert min_sugar_cereals == ["Shredded Wheat", "Data morsels"]


if __name__ == "__main__":
    main()
