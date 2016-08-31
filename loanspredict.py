import pandas as pd
loans_2007 = pd.read_csv('LoanStats3a.csv', skiprows=1)
half_count = len(loans_2007) / 2
loans_2007 = loans_2007.dropna(thresh=half_count, axis=1)
loans_2007 = loans_2007.drop(['desc', 'url'],axis=1)
loans_2007.to_csv('loans_2007.csv', index=False)

loans_2007 = pd.read_csv("loans_2007.csv")
print(loans_2007.head(1))
print(loans_2007.columns)

#drop duplicated/useless columns
loans_2007 = loans_2007.drop(['id', 'member_id', "funded_amnt", "funded_amnt_inv","grade","sub_grade","emp_title","issue_d"],axis=1)

#More droping
loans_2007 = loans_2007.drop(["zip_code", "out_prncp", "out_prncp_inv", "total_pymnt", "total_pymnt_inv", "total_rec_prncp"], axis=1)

#More droping
loans_2007 = loans_2007.drop(["total_rec_int", "total_rec_late_fee", "recoveries", "collection_recovery_fee", "last_pymnt_d", "last_pymnt_amnt"], axis=1)
print(loans_2007.ix[1])
print(loans_2007.shape[1])