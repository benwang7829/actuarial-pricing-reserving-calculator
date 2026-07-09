# Actuarial Pricing & Reserving Calculator

A Python calculator for actuarial pricing and reserving calculations using the **SOA Standard Ultimate Life Table (SULT)**.

This calculator computes actuarial present values (APVs), level net premiums, gross premiums, expense loadings, and policy reserves for several common life insurance and annuity products.

---

## Skills Demonstrated

- Python
- Financial mathematics
- Actuarial mathematics
- Life insurance pricing
- Prospective reserving
- Software design

---

## Features

The calculator currently supports pricing and reserving for the following products.

### Insurance Products

- Whole Life Insurance
- Term Life Insurance
- Pure Endowment
- Endowment Insurance
- Whole Life Annuity
- Temporary Life Annuity
- Certain and Life Annuity

---

## Assumptions

The calculator uses the following assumptions:

- Mortality follows the SOA Standard Ultimate Life Table (SULT).
- Benefits and premiums are paid annually.
- The interest rate is specified by the user.
- Expense assumptions (initial expenses, renewal expenses, first-year commissions, and renewal commissions) are specified by the user.
- Policies may be either deferred or non-deferred.
- **If a policy is deferred, premiums are assumed to be paid only during the deferral period.**
- **If a policy is not deferred:**
  - Whole Life Insurance, Whole Life Annuity, and Certain and Life Annuity premiums are paid for life.
  - Term Life Insurance, Pure Endowment, Endowment Insurance, and Temporary Life Annuity premiums are paid for the duration of the term.
- Gross reserves, net reserves, and expense reserves are calculated prospectively.

---

## Inputs

Depending on the selected product, the calculator requests:

- Product type
- Issue age
- Interest rate
- Benefit amount
- Term (if applicable)
- Deferral period
- Initial expenses
- Renewal expenses
- First-year commission
- Renewal commission
- Reserve time

---

## Outputs

The calculator reports:

- Actuarial Present Value (APV)
- Level Net Premium
- Gross Premium
- Expense Loading
- Gross Reserve
- Net Reserve
- Expense Reserve

---

## Validation

The calculator was manually validated using **21 test cases** based on the SOA Standard Ultimate Life Table (SULT).

The validation includes:

- All seven supported products
- Deferred contracts
- Non-deferred contracts
- Reserves during deferral
- Reserves during coverage

Each test verifies:

- APV
- Level Net Premium
- Gross Premium
- Expense Loading
- Gross Reserve
- Net Reserve
- Expense Reserve

A total of **147 expected outputs** were compared against the calculator.

---

## Technologies

- Python 3
- Standard Library

---

## Example

```
Product:
Whole Life Insurance

Age:
35

Interest rate:
0.05

Benefit:
100000

Deferral period:
10

First year commissions:
0.6

Renewal commissions:
0.03

Initial expenses:
500

Renewal expenses:
50

Reserve time:
5
```

Output

```
The actuarial present value is $9258.59
The level net premium is $1144.08
The gross premium is $1389.21
The annual expense loading is $245.13
The gross reserve at time 5 is $5950.38
The net reserve at time 5 is $6647.23
The expense reserve at time 5 is $-696.85
```

---

## Repository Structure

```
actuarial-pricing-reserving-calculator/
│
├── .gitignore
├── interest.py       # Interest and discount factor functions
├── main.py           # User interface and program execution
├── mortality.py      # SULT mortality table and survival functions
├── pricing.py        # Pricing, premium, and reserve calculations
└── README.md         # Project documentation
```

---

## Future Improvements

Potential additions include:

- Monthly premium calculations under uniform death distribution (UDD) and constant force of morality
- Fractional year reserves
- Continuous insurance benefits
- Select mortality tables
- Automated unit tests
- Modern life insurance contracts

---

## Author

Benjamin Wang

Mathematics Major, Philosophy Minor

Northeastern University
