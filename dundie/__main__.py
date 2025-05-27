import argparse

def load(filepath):
    """Load da a file to Database"""
    try:
        with open(filepath, 'r') as file:
            for line in file:
                print(line)
    except FileNotFoundError as e:
        print(f"File not found: {e}")



def main():
    parser = argparse.ArgumentParser(
    description="Dundie Mifflin Rewards CLI",
    epilog="Use 'dundie <command> --help' for more information on a command.",
)
    parser.add_argument(
       "subcommand",
       type=str,
       help="The subcommand to execute",
       choices=["load", "show", "add", "send"],
       default=help
    )
    parser.add_argument(
        "filepath",
        type=str,
        help="The path to the file to load or show",
        default=None
    )

    args = parser.parse_args()
    try:
        globals()[args.subcommand](args.filepath)
    except KeyError:
        print(f"Unknown subcommand: {args.subcommand}")
        parser.print_help()

if __name__ == "__main__":
    main()