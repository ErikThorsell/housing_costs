"""Main module."""
import argparse


def _parse_args():
    parser = argparse.ArgumentParser(description="Get an amortization plan.")
    parser.add_argument("--monthly-income", type=int, help="The household's total monthly income.")
    parser.add_argument("--house-price", type=int, help="Total cost of the house.")
    parser.add_argument("--down-payment", type=int, help="Available downpayment.")
    parser.add_argument("--interest", type=float, help="Interest to use in the calculation.")
    parser.add_argument(
        "--stop-amortizing",
        action="store_true",
        help="Use if you want to stop amortizing when your debt quota is <4.5 and your loan is <50% of the house's value.",
    )
    parser.add_argument("--minimum-amortization", type=int, help="If specified, the minimum amortization per month.")
    parser.add_argument("--years", type=int, default=60, help="Number of years to calculate for.")
    return parser.parse_args()


def main() -> None:

    args = _parse_args()

    monthly_income = args.monthly_income
    yearly_income = monthly_income * 12

    house_price = args.house_price
    down_payment = args.down_payment
    interest = args.interest

    loan = house_price - down_payment

    tot_interest_payment = 0

    month_counter = 0
    while month_counter / 12 < args.years:

        interest_payment = (loan * (interest / 100)) / 12
        tot_interest_payment += interest_payment

        if month_counter % 12 == 0:
            if loan / house_price > 0.7:
                amortization_percentage = 2
            elif loan / house_price > 0.5:
                amortization_percentage = 1
            else:
                amortization_percentage = 0

            print(f"New year ({month_counter/12:.0f}), recalculating amortization percentage. ", end="")
            debt_quota = loan / yearly_income
            print(f"Debt quota is: {debt_quota:.2f}. ", end="")

            if debt_quota > 4.5:
                amortization_percentage += 1
                print(f"Amortization percentage increased by 1% to {amortization_percentage}%.", end="")
            else:
                print(f"Amortization percentage is {amortization_percentage}%.", end="")
            print()

            if amortization_percentage == 0:
                if args.stop_amortizing:
                    print(
                        "Your loan is down to 50% of the house's value and your debt quota is <4.5. You have opted to stop amortizing!"
                    )
                    break

        loan_payment = (loan * (amortization_percentage / 100)) / 12
        loan_payment = max(loan_payment, args.minimum_amortization) if args.minimum_amortization else loan_payment

        if loan_payment == 0:
            print(
                "\n",
                "From here on your amortization will be 0 SEK.",
                "Try changing some input parameters if you want to test other scenarios!",
            )
            break

        loan -= loan_payment
        print(
            f"Month: {month_counter:3} | Interest: {interest_payment:5.0f}, Amortization ({amortization_percentage}%): {loan_payment:5.0f} | Monthly payment: {interest_payment + loan_payment:7.0f} | Remaining debt: {loan:7.0f}, Total interest: {tot_interest_payment:7.0f}"
        )

        if loan < 0:
            print(f"You have payed of your debt!")
            break

        month_counter += 1


if __name__ == "__main__":
    main()