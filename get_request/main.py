from app.get_postcode_program import PostCode
from app.get_postcode_program import get_columns

def __main__():
    pass


def querypostcodes(postcode_list, column_list):
    list_output = []
    for postcode in postcode_list:
        postcode_instance = PostCode(postcode, column_list)
        list_output.append(postcode_instance.select_values())
    return list_output


print([print(i) for i in querypostcodes(["HP22 6DB", "UB4 0PZ"],['postcode', 'country', 'longitude', 'latitude'])])



