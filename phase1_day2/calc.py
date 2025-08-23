import argparse

def main():
    p = argparse.ArgumentParser(description="Tiny calculator")
    p.add_argument("--a", type=float, required=True, help="first number")
    p.add_argument("--b", type=float, required=True, help="second number")
    p.add_argument("--op", choices=["add","sub","mul","div"], required=True, help="operation")
    args = p.parse_args()

    if args.op == "add":
        res = args.a + args.b
    elif args.op == "sub":
        res = args.a - args.b
    elif args.op == "mul":
        res = args.a * args.b
    else:
        if args.b == 0:
            raise SystemExit("Error: divide by zero")
        res = args.a / args.b

    # always print a clean result
    print(f"{res:.2f}")

if __name__ == "__main__":
    main()
