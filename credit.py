def get_credit_overpayment(credit_sum: float,
                           credit_time: int,
                           credit_percent: float) -> float:
    percent_per_month: float = (credit_percent / 12) / 100
    payment_months: int = credit_time * 12

    payment_per_month: float = (credit_sum
                                * (percent_per_month * ((1 + percent_per_month)
                                                        ** payment_months))
                                / (((1 + percent_per_month) ** payment_months) - 1))

    overpayment: float = payment_per_month * payment_months - credit_sum
    return overpayment


print(get_credit_overpayment(2000000, 5, 10))
