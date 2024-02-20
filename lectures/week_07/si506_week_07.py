# SI 506: Functions

import math
import pprint


def calculate_favorable_rating_pct(cereal):
    ratings = None  # TODO Call function
    fav_pct = (0 / 1) * 100  # TODO Replace with correct aritmetic expression
    return fav_pct


def calculate_sugar_content(cereal_brand, precision=2):
    return round(cereal_brand[-1] / cereal_brand[-2], precision)


def calculate_sugar_content_v2(cereal_brand, precision=2, format_pct=False):
    if format_pct:
        return f"{cereal_brand[-1] / cereal_brand[-2] * 100:.{precision}f}%"  # trailing % sign
    else:
        return round(cereal_brand[-1] / cereal_brand[-2], precision)


def calculate_sugar_content_v3(serving_size_gm, sugar_gm, precision=2, format_pct=False):
    if format_pct:
        return f"{sugar_gm / serving_size_gm * 100:.{precision}f}%"  # trailing % sign
    else:
        return round(sugar_gm / serving_size_gm, precision)


def count_ratings(ratings):
    count = 0
    for rating in ratings:
        pass # TODO Increment
    return count


def format_slogan(name, slogan):
    return f"{name}: {slogan}"


def get_cereal(cereal_brands, cereal_name):
    for cereal in cereal_brands:
        if cereal_name.lower() in cereal[1].lower():
            return cereal  # match, exit loop immediately


def get_cereal_attribute(cereal, headers, header="brand"):
    pass  # TODO Implement


def get_cereals_by_company(cereal_brands, company):
    brands = []
    for cereal in cereal_brands:
        pass  # TODO add if statement block
    return brands


def get_cereals_by_ingredient(cereals, ingredient):
    results = []
    for cereal in cereals:
        if has_ingredient(cereal[-1], ingredient):
            results.append(cereal)
    return results


def get_lowest_sugar_content(cereals, headers):
    min_sugar_content = []
    min_sugar_gm = None  # Add start value
    for cereal in cereals:
        brand = None  # TODO Call function
        serving_size_gm = None  # TODO Call function
        sugar_gm = None  # TODO Call function
        sugar_content = None  # TODO call function (return number not percent)

        # TODO Uncomment and fix
        # if sugar_content ??? min_sugar_gm:
        #     min_sugar_gm = None # Assign value
        #     min_sugar_content.clear() # reset
        #     min_sugar_content.append(brand) # cereal name only
        # elif sugar_content ??? min_sugar_gm:
        #     min_sugar_content.append(brand) # cereal name only

    return min_sugar_content


def get_ratings(cereal):
    pass  # TODO return rating numbers as a list


def get_slogan(cereal):
    return cereal[2]


def get_truth_value(val):
    return bool(val)  # check's the object's truth value


def has_cereal(cereals, cereal_brand):
    if get_cereal(cereals, cereal_brand):
        return True
    else:
        return False

    # Alternative
    # if get_cereal(cereals, cereal_brand):
    #     return True
    # return False


def has_ingredient(ingredients, ingredient):
    for item in ingredients:
        if ingredient.lower() in item.lower():
            return True  # exit function; terminates loop
    return False


# 2.1 TODO define function print_slogan()


def main():

    # Instantiate a custom PrettyPrinter object
    pp = pprint.PrettyPrinter(indent=1, width=100, compact=True)

    # fmt: off
    cereals = [
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
        ["Quaker Oats Company", "Cap'n Crunch", "It's got corn for crunch, oats for punch, and it stays crunchy, even in milk.", 27, 12],
        ["Post Consumer Brands", "Fruity Pebbles", "They're Yabba-Dabba-Delicious!", 27, 9.3],
        ["Kellogg Company", "Corn Flakes", "Wake up, up, up to Kellogg's Cornflakes!", 29, 10],
        ["Kellogg Company", "Apple Jacks", "We eat what we like.", 28, 8],
        ["General Mills", "Wheaties", "The Breakfast of Champions", 27, 4.1],
    ]
    # fmt: on

    # 2.1 DEFINING A FUNCTION

    # TODO Define function print_slogan() outside of main()

    # print("\n2.1 Print slogan")
    frosted_flakes = cereals[3]
    # TODO # Call function and pass argument

    # 2.2 RETURN VALUE

    raisin_bran = cereals[6]
    raisin_bran_slogan = None  # TODO Call function
    # print(f"\n2.2 Slogan = {raisin_bran_slogan}")

    # 2.3 MULTIPLE PARAMETERS

    # Positional arguments (order correct)
    wheaties_slogan = None  # TODO Call function
    # print(f"\n2.3 {wheaties_slogan}")

    # 2.4 ARGUMENT ORDER MATTERS (PASSED POSITIONALLY)

    # Postional arguments (order incorrect)
    apple_jacks_slogan = format_slogan(cereals[-2][2], cereals[-2][1])  # Oops! string reversed
    # print(f"\n2.4 {apple_jacks_slogan}")

    # 2.5 CHALLENGE 01

    post_cereals = None  # TODO Call function
    kellogg_cereals = None  # TODO Call function

    # print(f"\n2.5.1 Post cereals = {post_cereals}")
    # print(f"\n2.5.2 Kellogg's cereals = {kellogg_cereals}")

    # 3.1 KEYWORD ARGUMENTS (ANY ORDER ACCEPTABLE)

    general_mills_cereals = get_cereals_by_company(
        company="general mills", cereal_brands=cereals[1:]
    )

    # print(f"\n3.1 General Mills cereals = {general_mills_cereals}")

    # 3.2 OPTIONAL PARAMETERS

    # Retrieve cereal
    cocoa_puffs = get_cereal(cereals[1:], "Cocoa Puffs")

    # Accept precision default value
    cocoa_puffs_sugar = calculate_sugar_content(cocoa_puffs)
    # print(f"\n3.2.1 Cocoa Puffs sugar content = {cocoa_puffs_sugar}")

    # Override precision default value
    cocoa_puffs_sugar = calculate_sugar_content(cocoa_puffs, 3)  # override
    # print(f"\n3.2.2 Cocoa Puffs sugar content = {cocoa_puffs_sugar}")

    # 3.3 Skipping optional parameters

    raisin_bran = get_cereal(cereals[1:], "raisin bran")

    # The boolean True (numerical value 1) binds to wrong parameter; returns string
    raisin_bran_sugar = calculate_sugar_content_v2(raisin_bran, True)
    # print(
    #     f"\n3.3.1 Raisin Bran sugar content (type={type(raisin_bran_sugar)}) = {raisin_bran_sugar}"
    # )

    # Keyword argument binds 3 correctly, returns float
    raisin_bran_sugar = calculate_sugar_content_v2(raisin_bran, precision=3)
    # print(
    #     f"\n3.3.2 Raisin Bran sugar content (type={type(raisin_bran_sugar)}) = {raisin_bran_sugar}"
    # )

    # Returns formatted string
    raisin_bran_sugar = calculate_sugar_content_v2(raisin_bran, format_pct=True, precision=3)
    # raisin_bran_sugar = calculate_sugar_content_v2(raisin_bran, True, 3) # Alternative
    # print(
    #     f"\n3.3.3 Raisin Bran sugar content (type={type(raisin_bran_sugar)}) = {raisin_bran_sugar}"
    # )

    # 3.4 CHALLENGE 02

    headers = cereals[0]  # extract headers
    corn_flakes = None  # TODO Call function
    corn_flakes_serving_size_gm = None  # TODO Call function


    # print(f"\n3.4 Corn Flakes serving size = {corn_flakes_serving_size_gm} gm")

    # 4.0 PASSING FUNCTIONS CALLS AS ARGUMENTS

    cereal = get_cereal(cereals[1:], "Grape-nuts")
    serve_size_gm = get_cereal_attribute(cereal, headers, "serving_size_gm")
    sugar_gm = get_cereal_attribute(cereal, headers, "sugar_gm")
    sugar_content = None  # TODO call calculate_sugar_content_v3()
    # print(f"\n4.0.1 Sugar content = {sugar_content}")


    # 5.0 VARIABLE SCOPE

    # print(f"\n5.0.1 Globally-scoped variable cereals = {cereals[:2]}")

    # TODO Uncomment. Triggers a NameError runtime exception.
    # print(f"\n5.0.2 Locally-scoped variable brands = {brands}")

    # 6.0 FUNCTIONS CAN CALL OTHER FUNCTIONS

    # fmt: off
    cereal_ingredients = [
        ["manufacturer", "brand", "ingredients"],
        ["Kellogg Company", "Frosted Flakes", ("Milled Corn", "Sugar", "Malt Flavoring", "High Fructose Corn Syrup", "Salt")],
        ["Kellogg Company", "Raisin Bran", ("Whole Grain Wheat", "Raisins", "Wheat Bran", "Sugar", "High Fructose Corn Syrup")],
        ["General Mills", "Cheerios", ("Whole Grain Oats", "Modified Corn Starch", "Sugar", "Salt")],
        ["General Mills", "Cocoa Puffs", ("Whole Grain Corn", "Sugar", "Corn Syrup", "Cornmeal", "Canola and or Rice Bran Oil")],
        ["General Mills", "Lucky Charms", ("Oats", "Marshmallows", "Sugar", "Corn Syrup", "Corn Starch")],
        ["Post Consumer Brands", "Shredded Wheat (original spoon size)", ("Whole Grain Wheat",)],
        ["Post Consumer Brands", "Grape-nuts", ("Whole Grain Wheat", "Flour", "Malted Barley Flour", "Salt", "Dried Yeast")]
        ]
    # fmt: on

    corn_syrup = get_cereals_by_ingredient(cereal_ingredients[1:], "corn syrup")
    # print(f"\n6.0 Cereals w/corn syrup = {corn_syrup}")

    # 6.1 CHALLENGE 03

    min_sugar_cereals = get_lowest_sugar_content(cereals[1:], headers)
    # print(f"\n6.1 Cereal min sugar content = {min_sugar_cereals}")

    # 7.0 TRUTH VALUES

    fruity_pebbles = None
    truth_value = get_truth_value(fruity_pebbles)  # falsy

    # print(f"\n7.0.1 None truth value = {truth_value}")

    fruity_pebbles = []
    truth_value = get_truth_value(fruity_pebbles)  # falsy

    # print(f"\n7.0.2 Empty list truth value (length={len(fruity_pebbles)}) = {truth_value}")

    fruity_pebbles = ["Post Consumer Brands", "Fruity Pebbles", 27, 9.3]
    truth_value = get_truth_value(fruity_pebbles)  # truthy

    # print(f"\n7.0.3 List truth value (length={len(fruity_pebbles)}) = {truth_value}")

    has_golden_grahams = has_cereal(cereals, "Golden Grahams")
    # print(f"\n7.0.4 Has Golden Grahams = {has_golden_grahams}")

    # 8.0 ITERABLE PACKING AND UNPACKING

    # Packing
    shredded_wheat = ["Post Consumer Brands", "Shredded Wheat", "Bet you can’t eat three.", 49, 0.4]
    # Equivalent
    # shredded_wheat = get_cereal(cereals[1:], "shredded wheat")

    # Unpacking
    manufacturer, cereal_brand, slogan, serving_size_gm, sugar_gm = shredded_wheat

    # print(
    #     f"\n8.0 Shredded Wheat unpacked:",
    #     f"\nmanufacturer = {manufacturer}",
    #     f"\ncereal_brand = {cereal_brand}",
    #     f"\nslogan = {slogan}",
    #     f"\nserving_size_gm = {serving_size_gm}",
    #     f"\nsugar_gm = {sugar_gm}",
    # )

    # ValueError runtime exceptions triggered

    # Triggers ValueError: too many values to unpack (expected 4)
    # TODO Uncomment
    # manufacturer, cereal_brand, slogan, sugar_gm = shredded_wheat

    # Triggers ValueError: not enough values to unpack (expected 6, got 5)
    # TODO Uncomment
    # manufacturer, cereal_brand, slogan, serving_size_gm, sugar_gm, rating = shredded_wheat

    # Variables ordered incorrectly
    # TODO Uncomment
    # slogan, cereal_brand, manufacturer, sugar_gm, serving_size_gm = shredded_wheat

    # print(f"\n8.1 Shredded Wheat unpacked into wrong variables:",
    #     f"\nmanufacturer = {manufacturer}",
    #     f"\ncereal_brand = {cereal_brand}",
    #     f"\nslogan = {slogan}",
    #     f"\nserving_size_gm = {serving_size_gm}",
    #     f"\nsugar_gm = {sugar_gm}")

    # 8.2 UNPACKING IN A FOR LOOP

    # Conventional unpacking
    # print("\n8.2.1 for loop unpacking")
    for cereal in cereals[1:5]:
        manufacturer, brand, slogan, serving_size_gm, sugar_gm = cereal
        # print(
        #     f"\nmanufacturer: {manufacturer}",
        #     f"\nBrand: {brand}",
        #     f"\nSlogan: {slogan}",
        #     f"\nSugar content: {calculate_sugar_content_v3(serving_size_gm, sugar_gm)}",
        # )

    # Also an option
    # print("\n8.2.2 for loop unpacking")
    for manufacturer, brand, slogan, serving_size_gm, sugar_gm in cereals[-4:]:
        pass  # TODO Remove and uncomment print()
        # print(
        #     f"\nmanufacturer: {manufacturer}",
        #     f"\nBrand: {brand}",
        #     f"\nSlogan: {slogan}",
        #     f"\nSugar content: {calculate_sugar_content_v3(serving_size_gm, sugar_gm)}",
        # )

    # 9.0 ADDITIONAL CHALLENGES

    # fmt: off
    cereal_ratings_data = [
        ["manufacturer", "brand", "five_stars", "four_stars", "three_stars", "two_stars", "one_star"],
        ["Kellogg Company", "Apple Jacks", 185, 21, 10, 4, 2],
        ["Quaker Oats Company", "Cap'n Crunch", 49, 5, 3, 1, 1],
        ["Quaker Oats Company", "Cap'n Crunch's Crunch Berries", 196, 15, 6, 2, 4],
        ["General Mills", "Cheerios", 1310, 95, 14, 11, 28],
        ["General Mills", "Cinnamon Toast Crunch", 577, 46, 10, 5, 19],
        ["General Mills", "Cocoa Puffs", 147, 9, 1, 2, 5],
        ["Kellogg Company", "Corn Flakes", 467, 45, 9, 3, 10],
        ["Kellog Company", "Frosted Flakes", 1465, 116, 37, 11, 35],
        ["Kellogg Company", "Frosted Mini-Wheats", 883, 95, 18, 6, 26],
        ["Kellogg Company", "Fruit Loops", 750, 84, 14, 6, 8],
        ["Post Consumer Brands", "Fruity Pebbles", 170, 23, 8, 2, 7],
        ["Post Consumer Brands", "Grape-Nuts", 322, 25, 3, 1, 15],
        ["Post Consumer Brands", "Honey Bunches of Oats", 95, 7, 3, 1, 2],
        ["General Mills", "Honey Nut Cheerios", 814, 64, 22, 8, 22],
        ["General Mills", "Lucky Charms", 388, 38, 12, 3, 7],
        ["Kellogg Company", "Raisin Bran", 946, 79, 21, 14, 30],
        ["General Mills", "Reese's Puffs", 184, 14, 10, 4, 3],
        ["Kellogg Company", "Rice Krispies", 429, 31, 11, 5, 13],
        ["Post Consumer Brands", "Shredded Wheat", 208, 13, 6, 5, 11],
        ["General Mills", "Wheaties", 215, 18, 5, 2, 12],
    ]
    # fmt: on

    cereal_ratings_headers = cereal_ratings_data[0]
    cereal_ratings = cereal_ratings_data[1:]

    # 9.1 CHALLENGE 04

    raisin_bran = None # TODO Call function, pass keyword arguments in reverse order
    raisin_bran_ratings = None  # TODO Call function

    # TODO Uncomment
    # brand = {get_cereal_attribute(raisin_bran, cereal_ratings_headers, "brand")}
    # print(f"\n9.1 {brand} ratings = {raisin_bran_ratings}")

    # 9.2 CHALLENGE 05

    rating_groups = []
    for cereal in cereal_ratings:
        # TODO Call function; unpack ratings into five variables

        # Group ratings
        favorable = None  # TODO Add rating values
        neutral = None  # TODO Add rating values
        unfavorable = None  # TODO Add rating values

        # Build string
        brand = get_cereal_attribute(cereal, cereal_ratings_headers, "brand")

        # TODO Add variables
        string = (
            f"{None} ratings: favorable={None}, neutral={None}, unfavorable={None}"
        )
        rating_groups.append(string)

    # print(f"\n9.2 Rating groups (n={len(rating_groups)})")
    # pp.pprint(rating_groups)

    # 9.3 CHALLENGE 06

    honey_nut_cheerios = get_cereal(cereal_ratings, "honey nut cheerios")
    honey_nut_cheerios_fav_pct = calculate_favorable_rating_pct(honey_nut_cheerios)

    # Print
    brand = get_cereal_attribute(honey_nut_cheerios, cereal_ratings_headers, "brand")
    # print(f"\n9.3 {brand} favorability rating = {honey_nut_cheerios_fav_pct:.2f}%")


if __name__ == "__main__":
    main()