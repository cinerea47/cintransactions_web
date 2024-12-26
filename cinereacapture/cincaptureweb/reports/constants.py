#ownership choices
Active = 'active'
Suspended = 'suspended'
transaction_status = [
    (Active, "Active"),
    (Suspended, "Suspend"),
]

WITHDRAW_REP = "WITHDRAW"
DEPOSIT_REP = "DEPOSIT"
BILL_REP = "BILL"
TRANSACTION_TYPE_REP = [
    (WITHDRAW_REP, "Withdraw"),
    (DEPOSIT_REP, "Deposit"),
    (BILL_REP, "Bill"),
]

LOGGED_IN = 'logged_in'
LOGGED_OUT = 'logged_out'
CANCELLED = 'suspended'
LOGIN_STATUS = [
    (LOGGED_IN, "Logged In"),
    (LOGGED_OUT, "Logged Out"),
    (CANCELLED, "Cancelled"),
]

NUMBER_OF_ROWS_PAGE_REP = 25
