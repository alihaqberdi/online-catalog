from main import x


def compare_to_jinja_syntax(string):
    """Converts a string to a jinja syntax string

    Args:
        string (str): string to be converted

    Returns:
        str: converted string
    """
    string = string.replace('"assets/', """"{% static 'assets/""")
    string = string.replace('.jpg"', '''.jpg' %}"''')
    string = string.replace('.png"', '''.png' %}"''')
    string = string.replace('.svg"', '''.svg' %}"''')
    string = string.replace('.jpeg"', '''.jpeg' %}"''')
    string = string.replace('.css"', '''.css' %}"''')
    string = string.replace('.js"', '''.js' %}"''')
    return string


print(compare_to_jinja_syntax(x))

a = [
    {
        "title": "Elektronika",
        "children": [
            {
                "title": "Telefony i akcesoria",
                "children": [
                    {"title": "Iphone", "children": None},
                    {
                        "title": "Samsung",
                        "children": [{"title": "S10", "children": None}, {"title": "S20", "children": None}],
                    },
                    {"title": "Xiaomi", "children": None},
                ],
            },
            {
                "title": "Komputery i akcesoria",
                "children": [
                    {"title": "Laptopy", "children": None},
                    {"title": "Komputery stacjonarne", "children": None},
                    {"title": "Monitory", "children": None},
                ],
            },
        ],
    },
    {
        "title": "cars",
        "children": [
            {"title": "Audi", "children": None},
            {"title": "BMW", "children": None},
            {"title": "Mercedes", "children": None},
        ],
    },
]
