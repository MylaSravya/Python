# LMS Non Modular

# Customer Inputs
# ###################
# Set 1
cust_name = "aaa"
cust_cs = 230
cust_loan_amt = 12345

"""
# Set 2
cust_name = "bbb"
cust_cs = 30
cust_loan_amt = 12345

# Set 3
cust_name = "bbb"
cust_cs = 400
cust_loan_amt = 19992345

"""

# LMS Master Data
# ###################
loan_rules_master_data = (
# Data Set 1
 {"cs_start":100,"cs_end":199,"loan_amt_start":10000,"loan_amt_end":19999,"interest":6.5,"duration_in_mons":72}
,{"cs_start":200,"cs_end":299,"loan_amt_start":10000,"loan_amt_end":19999,"interest":6.0,"duration_in_mons":72}
,{"cs_start":300,"cs_end":399,"loan_amt_start":10000,"loan_amt_end":19999,"interest":5.0,"duration_in_mons":72}
,{"cs_start":400,"cs_end":500,"loan_amt_start":10000,"loan_amt_end":19999,"interest":4.5,"duration_in_mons":72}
# Data Set 2
,{"cs_start":100,"cs_end":199,"loan_amt_start":20000,"loan_amt_end":29999,"interest":6.5,"duration_in_mons":72}
,{"cs_start":200,"cs_end":299,"loan_amt_start":20000,"loan_amt_end":29999,"interest":6.0,"duration_in_mons":72}
,{"cs_start":300,"cs_end":399,"loan_amt_start":20000,"loan_amt_end":29999,"interest":5.0,"duration_in_mons":72}
,{"cs_start":400,"cs_end":500,"loan_amt_start":20000,"loan_amt_end":29999,"interest":4.5,"duration_in_mons":72}
# Data Set 3
,{"cs_start":100,"cs_end":199,"loan_amt_start":30000,"loan_amt_end":39999,"interest":6.5,"duration_in_mons":72}
,{"cs_start":200,"cs_end":299,"loan_amt_start":30000,"loan_amt_end":39999,"interest":6.0,"duration_in_mons":72}
,{"cs_start":300,"cs_end":399,"loan_amt_start":30000,"loan_amt_end":39999,"interest":5.0,"duration_in_mons":72}
,{"cs_start":400,"cs_end":500,"loan_amt_start":30000,"loan_amt_end":39999,"interest":4.5,"duration_in_mons":72}
)

# output dict
application_decision = {}

# Core Algorithm
for c1 in loan_rules_master_data:
    # print(c1)
    if cust_cs >= c1["cs_start"] and cust_cs<=c1["cs_end"] and cust_loan_amt >= c1["loan_amt_start"] and cust_loan_amt<= c1["loan_amt_end"]:
        
        """
        if no_exception
         return application_decision["status"] = "Approved"
        if exception 
        return application_decision["status"] = "Denied"
        """
        # application_decision["cust_name"] = cust_name 
        application_decision["cust_name"] = cust_name
        application_decision["cust_cs"] = cust_cs
        application_decision["cust_req_loan_amt"] = cust_loan_amt
        application_decision["interest"] = c1["interest"]
        application_decision["duration_in_mons"] = c1["duration_in_mons"]

print(application_decision)