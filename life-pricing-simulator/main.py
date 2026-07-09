from pricing import whole_life, term_life, nex, endowment, whole_life_annuity, temporary_life_annuity, certain_and_life_annuity

def main():
    print("========================================")
    print("   Actuarial Pricing & Reserving Calculator")
    print("========================================")

    print("\nChoose a product:")
    print("1. Whole Life Insurance")
    print("2. Term Life Insurance")
    print("3. Pure Endowment")
    print("4. Endowment Insurance")
    print("5. Whole Life Annuity")
    print("6. Temporary Life Annuity")
    print("7. Certain and Life Annuity")

    choice = input("\nChoice: ").strip().lower()

    print()

    if choice in ["1", "whole life", "whole life insurance"]:
        product = "Whole Life Insurance"

    elif choice in ["2", "term life", "term life insurance"]:
        product = "Term Life Insurance"

    elif choice in ["3", "pure endowment"]:
        product = "Pure Endowment"

    elif choice in ["4", "endowment", "endowment insurance"]:
        product = "Endowment Insurance"

    elif choice in ["5", "whole life annuity"]:
        product = "Whole Life Annuity"

    elif choice in ["6", "temporary life annuity", "temporary annuity"]:
        product = "Temporary Life Annuity"

    elif choice in ["7", "certain and life annuity", "certain-life annuity"]:
        product = "Certain and Life Annuity"

    else:
        print("Invalid product selection.")
        return

    print(f"You selected: {product}")

    age = int(input("\nAge at issue (in years): ").strip().lower())
    i = float(input("\nAnnual effective interest rate (e.g. 0.05): ").strip().lower())
    benefit = float(input("\nBenefit amount: ").strip().lower())
    deferral_period = int(input("\nDeferral period (in years): ").strip().lower())

    if product in [
        "Term Life Insurance",
        "Pure Endowment",
        "Endowment Insurance",
        "Temporary Life Annuity",
        "Certain and Life Annuity",
    ]:
        t = int(input("Term (in years): "))

    # First year commissions is expressed as a percentage of the gross premium
    # Renewal commissions is expressed as a percentage of the gross premium and is paid for each premium after the first year
    # Initial expenses is expressed in dollars and is incurred at the time of policy issue
    # Renewal expenses is expressed in dollars and is incurred for each premium after the first year
    first_year_commissions = float(input("\nFirst year commissions (as a percentage of premium): ").strip().lower())
    renewal_commissions = float(input("\nRenewal commissions (as a percentage of premium): ").strip().lower())
    initial_expenses = float(input("\nInitial expenses (in dollars): ").strip().lower())
    renewal_expenses = float(input("\nRenewal expenses (in dollars): ").strip().lower())
    time_of_reserve = int(input("\nCalculate reserve at time: ").strip().lower())

    deferral_factor = nex(age, deferral_period, i)

    # If deferred, assume premiums and expenses are paid only during the deferral period
    if product == "Whole Life Insurance":
        apv = whole_life(age + deferral_period, i) * benefit * deferral_factor
        if deferral_period > 0:
            premium_payment = temporary_life_annuity(age, deferral_period, i)
        else:
            premium_payment = whole_life_annuity(age, i)

            if deferral_period > time_of_reserve:
                reserve_apv_benefit = whole_life(age + deferral_period, i) * benefit * nex(age, time_of_reserve, i)
                reserve_apv_expenses = temporary_life_annuity(age, deferral_period - time_of_reserve, i)
        
    elif product == "Term Life Insurance":
        apv = term_life(age + deferral_period, t, i) * benefit * deferral_factor
        if deferral_period > 0:
            premium_payment = temporary_life_annuity(age, deferral_period, i)
        else:
            premium_payment = temporary_life_annuity(age, t, i)

    elif product == "Pure Endowment":
        apv = nex(age + deferral_period, t, i) * benefit * deferral_factor
        if deferral_period > 0:
            premium_payment = temporary_life_annuity(age, deferral_period, i)
        else:
            premium_payment = temporary_life_annuity(age, t, i)

    elif product == "Endowment Insurance":
        apv = endowment(age + deferral_period, t, i) * benefit * deferral_factor
        if deferral_period > 0:
            premium_payment = temporary_life_annuity(age, deferral_period, i)
        else:
            premium_payment = temporary_life_annuity(age, t, i)

    elif product == "Whole Life Annuity":
        apv = whole_life_annuity(age + deferral_period, i) * benefit * deferral_factor
        if deferral_period > 0:
            premium_payment = temporary_life_annuity(age, deferral_period, i)
        else:
            premium_payment = whole_life_annuity(age, i)

    elif product == "Temporary Life Annuity":
        apv = temporary_life_annuity(age + deferral_period, t, i) * benefit * deferral_factor
        if deferral_period > 0:
            premium_payment = temporary_life_annuity(age, deferral_period, i)
        else:
            premium_payment = temporary_life_annuity(age, t, i)

    elif product == "Certain and Life Annuity":
        apv = certain_and_life_annuity(age + deferral_period, t, i) * benefit * deferral_factor
        if deferral_period > 0:
            premium_payment = temporary_life_annuity(age, deferral_period, i)
        else:
            premium_payment = whole_life_annuity(age, i)

    if deferral_period > 0:
        premium_payment = temporary_life_annuity(age, deferral_period, i)

    # Level net premium calculation under the equivalence principle
    level_net_premium = apv / premium_payment

    # Gross premium calculation considering commissions and expenses under the equivalence principle
    gross_premium = (apv + initial_expenses + renewal_expenses * (premium_payment - 1)) / (premium_payment * (1 - renewal_commissions) - (first_year_commissions - renewal_commissions))

    if product == "Whole Life Insurance":
        if deferral_period > 0:
            if deferral_period > time_of_reserve:
                reserve_apv_benefit = whole_life(age + deferral_period, i) * benefit * nex(age + time_of_reserve, deferral_period - time_of_reserve, i)
                premium_payment_reserve = temporary_life_annuity(age + time_of_reserve, deferral_period - time_of_reserve, i)
                gross_reserve_apv_premium = premium_payment_reserve * gross_premium
                net_reserve_apv_premium = premium_payment_reserve * level_net_premium
                reserve_apv_expenses = premium_payment_reserve * (renewal_expenses + renewal_commissions * gross_premium)
                gross_reserve = reserve_apv_benefit + reserve_apv_expenses - gross_reserve_apv_premium
                net_reserve = reserve_apv_benefit - net_reserve_apv_premium
            else:
                reserve_apv_benefit = whole_life(age + time_of_reserve, i) * benefit
                premium_payment_reserve = 0
                gross_reserve_apv_premium = 0
                net_reserve_apv_premium = 0
                reserve_apv_expenses = 0
                gross_reserve = reserve_apv_benefit + reserve_apv_expenses - gross_reserve_apv_premium
                net_reserve = reserve_apv_benefit - net_reserve_apv_premium
        else:
            reserve_apv_benefit = whole_life(age + time_of_reserve, i) * benefit
            premium_payment_reserve = whole_life_annuity(age + time_of_reserve, i)
            gross_reserve_apv_premium = premium_payment_reserve * gross_premium
            net_reserve_apv_premium = premium_payment_reserve * level_net_premium
            reserve_apv_expenses = premium_payment_reserve * (renewal_expenses + renewal_commissions * gross_premium)
            gross_reserve = reserve_apv_benefit + reserve_apv_expenses - gross_reserve_apv_premium
            net_reserve = reserve_apv_benefit - net_reserve_apv_premium

    elif product == "Term Life Insurance":
        if deferral_period > 0:
            if deferral_period > time_of_reserve:
                reserve_apv_benefit = term_life(age + deferral_period, t, i) * benefit * nex(age + time_of_reserve, deferral_period - time_of_reserve, i)
                premium_payment_reserve = temporary_life_annuity(age + time_of_reserve, deferral_period - time_of_reserve, i)
                gross_reserve_apv_premium = premium_payment_reserve * gross_premium
                net_reserve_apv_premium = premium_payment_reserve * level_net_premium
                reserve_apv_expenses = premium_payment_reserve * (renewal_expenses + renewal_commissions * gross_premium)
                gross_reserve = reserve_apv_benefit + reserve_apv_expenses - gross_reserve_apv_premium
                net_reserve = reserve_apv_benefit - net_reserve_apv_premium
            else:
                reserve_apv_benefit = term_life(age + time_of_reserve, t - time_of_reserve + deferral_period, i) * benefit
                premium_payment_reserve = 0
                gross_reserve_apv_premium = 0
                net_reserve_apv_premium = 0
                reserve_apv_expenses = 0
                gross_reserve = reserve_apv_benefit + reserve_apv_expenses - gross_reserve_apv_premium
                net_reserve = reserve_apv_benefit - net_reserve_apv_premium
        else:
            reserve_apv_benefit = term_life(age + time_of_reserve, t - time_of_reserve, i) * benefit
            premium_payment_reserve = temporary_life_annuity(age + time_of_reserve, t - time_of_reserve, i)
            gross_reserve_apv_premium = premium_payment_reserve * gross_premium
            net_reserve_apv_premium = premium_payment_reserve * level_net_premium
            reserve_apv_expenses = premium_payment_reserve * (renewal_expenses + renewal_commissions * gross_premium)
            gross_reserve = reserve_apv_benefit + reserve_apv_expenses - gross_reserve_apv_premium
            net_reserve = reserve_apv_benefit - net_reserve_apv_premium

    elif product == "Pure Endowment":
        if deferral_period > 0:
            
            # APV formula remains constant for pure endowment regardless of deferral period
            reserve_apv_benefit = nex(age + time_of_reserve, deferral_period + t - time_of_reserve, i) * benefit

            if deferral_period > time_of_reserve:
                premium_payment_reserve = temporary_life_annuity(age + time_of_reserve, deferral_period - time_of_reserve, i)
                gross_reserve_apv_premium = premium_payment_reserve * gross_premium
                net_reserve_apv_premium = premium_payment_reserve * level_net_premium
                reserve_apv_expenses = premium_payment_reserve * (renewal_expenses + renewal_commissions * gross_premium)
                gross_reserve = reserve_apv_benefit + reserve_apv_expenses - gross_reserve_apv_premium
                net_reserve = reserve_apv_benefit - net_reserve_apv_premium
            else:
                premium_payment_reserve = 0
                gross_reserve_apv_premium = 0
                net_reserve_apv_premium = 0
                reserve_apv_expenses = 0
                gross_reserve = reserve_apv_benefit + reserve_apv_expenses - gross_reserve_apv_premium
                net_reserve = reserve_apv_benefit - net_reserve_apv_premium
        else:
            reserve_apv_benefit = nex(age + time_of_reserve, t - time_of_reserve, i) * benefit
            premium_payment_reserve = temporary_life_annuity(age + time_of_reserve, t - time_of_reserve, i)
            gross_reserve_apv_premium = premium_payment_reserve * gross_premium
            net_reserve_apv_premium = premium_payment_reserve * level_net_premium
            reserve_apv_expenses = premium_payment_reserve * (renewal_expenses + renewal_commissions * gross_premium)
            gross_reserve = reserve_apv_benefit + reserve_apv_expenses - gross_reserve_apv_premium
            net_reserve = reserve_apv_benefit - net_reserve_apv_premium

    elif product == "Endowment Insurance":
        if deferral_period > 0:
            if deferral_period > time_of_reserve:
                reserve_apv_benefit = endowment(age + deferral_period, t, i) * benefit * nex(age + time_of_reserve, deferral_period - time_of_reserve, i)
                premium_payment_reserve = temporary_life_annuity(age + time_of_reserve, deferral_period - time_of_reserve, i)
                gross_reserve_apv_premium = premium_payment_reserve * gross_premium
                net_reserve_apv_premium = premium_payment_reserve * level_net_premium
                reserve_apv_expenses = premium_payment_reserve * (renewal_expenses + renewal_commissions * gross_premium)
                gross_reserve = reserve_apv_benefit + reserve_apv_expenses - gross_reserve_apv_premium
                net_reserve = reserve_apv_benefit - net_reserve_apv_premium
            else:
                reserve_apv_benefit = endowment(age + time_of_reserve, t - time_of_reserve + deferral_period, i) * benefit
                premium_payment_reserve = 0
                gross_reserve_apv_premium = 0
                net_reserve_apv_premium = 0
                reserve_apv_expenses = 0
                gross_reserve = reserve_apv_benefit + reserve_apv_expenses - gross_reserve_apv_premium
                net_reserve = reserve_apv_benefit - net_reserve_apv_premium
        else:
            reserve_apv_benefit = endowment(age + time_of_reserve, t - time_of_reserve, i) * benefit
            premium_payment_reserve = temporary_life_annuity(age + time_of_reserve, t - time_of_reserve, i)
            gross_reserve_apv_premium = premium_payment_reserve * gross_premium
            net_reserve_apv_premium = premium_payment_reserve * level_net_premium
            reserve_apv_expenses = premium_payment_reserve * (renewal_expenses + renewal_commissions * gross_premium)
            gross_reserve = reserve_apv_benefit + reserve_apv_expenses - gross_reserve_apv_premium
            net_reserve = reserve_apv_benefit - net_reserve_apv_premium

    elif product == "Whole Life Annuity":
        if deferral_period > 0:
            if deferral_period > time_of_reserve:
                reserve_apv_benefit = whole_life_annuity(age + deferral_period, i) * benefit * nex(age + time_of_reserve, deferral_period - time_of_reserve, i)
                premium_payment_reserve = temporary_life_annuity(age + time_of_reserve, deferral_period - time_of_reserve, i)
                gross_reserve_apv_premium = premium_payment_reserve * gross_premium
                net_reserve_apv_premium = premium_payment_reserve * level_net_premium
                reserve_apv_expenses = premium_payment_reserve * (renewal_expenses + renewal_commissions * gross_premium)
                gross_reserve = reserve_apv_benefit + reserve_apv_expenses - gross_reserve_apv_premium
                net_reserve = reserve_apv_benefit - net_reserve_apv_premium
            else:
                reserve_apv_benefit = whole_life_annuity(age + time_of_reserve, i) * benefit
                premium_payment_reserve = 0
                gross_reserve_apv_premium = 0
                net_reserve_apv_premium = 0
                reserve_apv_expenses = 0
                gross_reserve = reserve_apv_benefit + reserve_apv_expenses - gross_reserve_apv_premium
                net_reserve = reserve_apv_benefit - net_reserve_apv_premium
        else:
            reserve_apv_benefit = whole_life_annuity(age + time_of_reserve, i) * benefit
            premium_payment_reserve = whole_life_annuity(age + time_of_reserve, i)
            gross_reserve_apv_premium = premium_payment_reserve * gross_premium
            net_reserve_apv_premium = premium_payment_reserve * level_net_premium
            reserve_apv_expenses = premium_payment_reserve * (renewal_expenses + renewal_commissions * gross_premium)
            gross_reserve = reserve_apv_benefit + reserve_apv_expenses - gross_reserve_apv_premium
            net_reserve = reserve_apv_benefit - net_reserve_apv_premium

    elif product == "Temporary Life Annuity":
        if deferral_period > 0:
            if deferral_period > time_of_reserve:
                reserve_apv_benefit = temporary_life_annuity(age + deferral_period, t, i) * benefit * nex(age + time_of_reserve, deferral_period - time_of_reserve, i)
                premium_payment_reserve = temporary_life_annuity(age + time_of_reserve, deferral_period - time_of_reserve, i)
                gross_reserve_apv_premium = premium_payment_reserve * gross_premium
                net_reserve_apv_premium = premium_payment_reserve * level_net_premium
                reserve_apv_expenses = premium_payment_reserve * (renewal_expenses + renewal_commissions * gross_premium)
                gross_reserve = reserve_apv_benefit + reserve_apv_expenses - gross_reserve_apv_premium
                net_reserve = reserve_apv_benefit - net_reserve_apv_premium
            else:
                reserve_apv_benefit = temporary_life_annuity(age + time_of_reserve, t - time_of_reserve + deferral_period, i) * benefit
                premium_payment_reserve = 0
                gross_reserve_apv_premium = 0
                net_reserve_apv_premium = 0
                reserve_apv_expenses = 0
                gross_reserve = reserve_apv_benefit + reserve_apv_expenses - gross_reserve_apv_premium
                net_reserve = reserve_apv_benefit - net_reserve_apv_premium
        else:
            reserve_apv_benefit = temporary_life_annuity(age + time_of_reserve, t - time_of_reserve, i) * benefit
            premium_payment_reserve = temporary_life_annuity(age + time_of_reserve, t - time_of_reserve, i)
            gross_reserve_apv_premium = premium_payment_reserve * gross_premium
            net_reserve_apv_premium = premium_payment_reserve * level_net_premium
            reserve_apv_expenses = premium_payment_reserve * (renewal_expenses + renewal_commissions * gross_premium)
            gross_reserve = reserve_apv_benefit + reserve_apv_expenses - gross_reserve_apv_premium
            net_reserve = reserve_apv_benefit - net_reserve_apv_premium

    elif product == "Certain and Life Annuity":
        if deferral_period > 0:
            if deferral_period > time_of_reserve:
                reserve_apv_benefit = certain_and_life_annuity(age + deferral_period, t, i) * benefit * nex(age + time_of_reserve, deferral_period - time_of_reserve, i)
                premium_payment_reserve = temporary_life_annuity(age + time_of_reserve, deferral_period - time_of_reserve, i)
                gross_reserve_apv_premium = premium_payment_reserve * gross_premium
                net_reserve_apv_premium = premium_payment_reserve * level_net_premium
                reserve_apv_expenses = premium_payment_reserve * (renewal_expenses + renewal_commissions * gross_premium)
                gross_reserve = reserve_apv_benefit + reserve_apv_expenses - gross_reserve_apv_premium
                net_reserve = reserve_apv_benefit - net_reserve_apv_premium
            else:
                reserve_apv_benefit = certain_and_life_annuity(age + time_of_reserve, t - time_of_reserve + deferral_period, i) * benefit
                premium_payment_reserve = 0
                gross_reserve_apv_premium = 0
                net_reserve_apv_premium = 0
                reserve_apv_expenses = 0
                gross_reserve = reserve_apv_benefit + reserve_apv_expenses - gross_reserve_apv_premium
                net_reserve = reserve_apv_benefit - net_reserve_apv_premium
        else:
            # If there is no deferral period, premiums are paid for life
            reserve_apv_benefit = certain_and_life_annuity(age + time_of_reserve, t - time_of_reserve, i) * benefit
            premium_payment_reserve = whole_life_annuity(age + time_of_reserve, i)
            gross_reserve_apv_premium = premium_payment_reserve * gross_premium
            net_reserve_apv_premium = premium_payment_reserve * level_net_premium
            reserve_apv_expenses = premium_payment_reserve * (renewal_expenses + renewal_commissions * gross_premium)
            gross_reserve = reserve_apv_benefit + reserve_apv_expenses - gross_reserve_apv_premium
            net_reserve = reserve_apv_benefit - net_reserve_apv_premium

    if time_of_reserve == 0:
            gross_reserve = 0
            net_reserve = 0

    if product in [
        "Term Life Insurance",
        "Pure Endowment",
        "Endowment Insurance",
        "Temporary Life Annuity",
        "Certain and Life Annuity",
    ]:
        if time_of_reserve >= t + deferral_period:
            gross_reserve = 0
            net_reserve = 0

    expense_reserve = gross_reserve - net_reserve
    expense_loading = gross_premium - level_net_premium

    print(f"The actuarial present value is ${apv:.2f}")
    print(f"The level net premium is ${level_net_premium:.2f}")
    print(f"The gross premium is ${gross_premium:.2f}")
    print(f"The annual expense loading is ${expense_loading:.2f}")
    print(f"The gross reserve at time {time_of_reserve} is ${gross_reserve:.2f}")
    print(f"The net reserve at time {time_of_reserve} is ${net_reserve:.2f}")
    print(f"The expense reserve at time {time_of_reserve} is ${expense_reserve:.2f}")

if __name__ == "__main__":
    main()