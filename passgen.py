import string, random
from argparse import ArgumentParser


def generate_password(args):
    password = []
    for i in range(args.length):
        password.append("")
    def get_index(): return random.randint(0, args.length-1)
    index = get_index()

    for i in range(args.special):
        while password[index] != "":
            index = get_index()
        password[index] = random.choice(string.punctuation)

    for i in range(args.numbers):
        while password[index] != "":
            index = get_index()
        password[index] = random.choice(string.digits)

    for i in range(args.capital):
        while password[index] != "":
            index = get_index()
        password[index] = random.choice(string.ascii_uppercase)

    for i in range(args.lower):
        while password[index] != "":
            index = get_index()
        password[index] = random.choice(string.ascii_lowercase)

    # fill the rest of the password with valid random characters (charatcers not set to a value of 0)

    choices = []
    if args.special > 0:
        choices.append(string.punctuation)
    if args.numbers > 0:
        choices.append(string.digits)
    if args.capital > 0:
        choices.append(string.ascii_uppercase)
    if args.lower > 0:
        choices.append(string.ascii_lowercase)

    for i in range(args.length):
        if password[i] == "":
            password[i] = random.choice(random.choice(choices))

    return "".join(password)


def main():
    parser = ArgumentParser(description="Generate a random password")
    parser.add_argument("-L", "--length", type=int, help="Length of the password", default=12)
    parser.add_argument("-s", "--special", type=int, help="Number of special characters (punctuation) in the password", default=2)
    parser.add_argument("-n", "--numbers", type=int, help="Number of numbers in the password", default=2)
    parser.add_argument("-c", "--capital", type=int, help="Number of capital letters in the password", default=2)
    parser.add_argument("-l", "--lower", type=int, help="Number of lowercase letters in the password", default=2)
    parser.add_argument("-f", "--file", type=str, help="File path to save the password to")
    args = parser.parse_args()
    if args.length < 8:
        print("Error: The length of the password must be at least 8 characters")
        exit()
    elif args.length > 128:
        print("Error: The length of the password must be at most 128 characters")
        exit()
    if args.special + args.numbers + args.capital + args.lower > args.length:
        print("Error: The sum of special, numbers, capital and lower must be less than or equal to length (%d)" % args.length)
        exit()
    password = generate_password(args)
    if args.file:
        with open(args.file, "w") as f:
            f.write(password)
    else:
        print(password)


if __name__ == "__main__":
    main()
