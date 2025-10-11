from bankAccount import Money
def test_default():
    m1 = Money()
    print(f'Action: Invoking the Money class constructor using Money().')
    print("Output:")
    print(f"Amount: {m1.amount}")
    print(f"Denomination: {m1.denomination}")
    print()

def test_amount():
    m2 = Money(100)
    print(f'Action: Invoking the Money class constructor using Money({m2.amount}).')
    print("Output:")
    print(f"Amount: {m2.amount}")
    print(f"Denomination: {m2.denomination}")
    print()

def test_amount_denomination():
    m3 = Money(100, "USD")
    print(f'Action: Invoking the Money class constructor using Money({m3.amount}, "{m3.denomination}").')
    print("Output:")
    print(f"Amount: {m3.amount}")
    print(f"Denomination: {m3.denomination}")
if __name__ == "__main__":
    test_default()
    test_amount()
    test_amount_denomination()