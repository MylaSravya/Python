# ###################################################################################
# Loan Management System - Caller
# ###################################################################################

# Imports
import lms_engine as lms    # With Alias
import lms_masterdata       # No Alias

# Customer Details SET 1
# ######################
cust_name = "aaa"
cust_cs = 230
cust_loan_amt = 12345

# Call the engine
result = lms.lms_engine( p_loans_master_data  = lms_masterdata.loan_rules_master_data
                        ,p_cust_name          = cust_name
                        ,p_cust_cs            = cust_cs
                        ,p_cust_req_loan_amt  = cust_loan_amt)

print(result)


# Customer Details SET 2
# ######################
cust_name = "aaa"
cust_cs = 30
cust_loan_amt = 12345

# Call the engine
result = lms.lms_engine( p_loans_master_data  = lms_masterdata.loan_rules_master_data
                        ,p_cust_name          = cust_name
                        ,p_cust_cs            = cust_cs
                        ,p_cust_req_loan_amt  = cust_loan_amt)

print(result)


# Customer Details SET 3
# ######################
cust_name = "aaa"
cust_cs = 30000
cust_loan_amt = 12345

# Call the engine
result = lms.lms_engine( p_loans_master_data  = lms_masterdata.loan_rules_master_data
                        ,p_cust_name          = cust_name
                        ,p_cust_cs            = cust_cs
                        ,p_cust_req_loan_amt  = cust_loan_amt)

print(result)

"""
for c1 in range(1000000):
    l_cs = random.randint(100,600)
    l_loan_amt=random.randint(9900,60000)
"""