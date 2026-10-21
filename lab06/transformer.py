import argparse

def  transform_upper(text):
    return text.upper()
def transform_lower(text):
    return text.lower()
def get_word_count(text):
    return len(text.split())
def filter_short(text, min_length):
    if len(text) > min_length:
        return text
    else:
        return None


if __name__=="__main__":
    parser = argparse.ArgumentParser(
        description="Transform a list of strings."
    )

parser.add_argument(
    "--action",
    required=True,
    choices=["upper", "lower", "count", "filter"],
    help="The transformation to perform."
)

parser.add_argument(
    "--data",
    required=True,
    help="The input data to transform."
)

parser.add_argument(
    "--min_length",
    type=int,
    default=3,
    help="Minimum length for the filter action"
)

args = parser.parse_args()
data_list = args.data.split(",")

for text in data_list:
    if args.action == "upper":
        result = transform_upper(text)
    elif args.action == "lower":
        result = transform_lower(text)
    elif args.action == "count":
        result = get_word_count(text)
    elif args.action == "filter":
        result = filter_short(text, args.min_length)

    if result is not None:
        print(result)
