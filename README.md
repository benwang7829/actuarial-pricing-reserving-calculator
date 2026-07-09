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

The calculator was manually validated using **21 actuarial test cases** based on the SOA Standard Ultimate Life Table (SULT).

The validation includes:

- All seven supported products
- Deferred contracts
- Non-deferred contracts
- Reserves before deferral
- Reserves after deferral
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

Reserve time:
15
```

Output

```
Actuarial Present Value: $9,258.66
Level Net Premium: $1,144.09
Gross Premium: $1,389.22
Expense Loading: $245.13
Gross Reserve: $18,931.00
Net Reserve: $18,931.00
Expense Reserve: $0.00
```

---

## Repository Structure

```
Actuarial Calculator/
│
├── actuarial_calculator.py
├── README.md
```

---

## Future Improvements

Potential additions include:

- Monthly premium calculations
- Continuous insurance benefits
- Select mortality tables
- Multiple reserve methods
- Graphical user interface (GUI)
- Automated unit tests
- Modern life insurance contracts

---

## Author

Benjamin Wang

Mathematics Major, Philosophy Minor

Northeastern University
