# Taken From
# Iterating Over Data
# Problem-Set While Loops #11
def silly_sum():
    """ reads numbers from the user (use input_int) 
        summing as we go until either
        the user enters 0, or
        the sum reaches or exceeds 1000
    """
    sum_of_user_data = 0
    while user_data > 0 and user_data < 10:
        user_data= input("Guess a letter: ")
        user_data += sum_of_user_data
    return sum_of_user_data


if __name__ == "__main__":
    print(f"Answer = {silly_sum()}")
