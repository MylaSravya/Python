# ###################################################################################
# Loan Management System - Engine
# ###################################################################################

#  LMS Engine
# ####################
def lms_engine(p_loans_master_data, p_cust_name, p_cust_cs, p_cust_req_loan_amt):

    # Variables
    application_decision = {}
    
    # Core Algo
    for c1 in p_loans_master_data:
        # print(c1)
        if p_cust_cs >= c1["cs_start"] and p_cust_cs<=c1["cs_end"] and p_cust_req_loan_amt >= c1["loan_amt_start"] and p_cust_req_loan_amt<= c1["loan_amt_end"]:
            
            application_decision["cust_name"] = p_cust_name
            application_decision["cust_cs"] = p_cust_cs
            application_decision["cust_req_loan_amt"] = p_cust_req_loan_amt
            application_decision["interest"] = c1["interest"]
            application_decision["duration_in_mons"] = c1["duration_in_mons"]

    # Return / Output
    return application_decision