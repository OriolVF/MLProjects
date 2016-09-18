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

#check for null counts
loans = pd.read_csv("filtered_loans_2007.csv")
null_counts=[]
null_counts = loans.isnull().sum()
print(null_counts)

#drop null rows and null columns
loans = loans.drop("pub_rec_bankruptcies", axis=1)
loans = loans.dropna(axis=0)
print(loans.dtypes.value_counts())

#get object columns
object_columns_df = loans.select_dtypes(include=["object"])
print(object_columns_df.iloc[0])

#check unique values
cols = ['home_ownership', 'verification_status', 'emp_length', 'term', 'addr_state']
for col in cols:
    print(loans[col].value_counts())
    

#check unique values in columns purpose and title
print(loans["purpose"].value_counts())
print(loans["title"].value_counts())
    
    mapping_dict = {
    "emp_length": {
        "10+ years": 10,
        "9 years": 9,
        "8 years": 8,
        "7 years": 7,
        "6 years": 6,
        "5 years": 5,
        "4 years": 4,
        "3 years": 3,
        "2 years": 2,
        "1 year": 1,
        "< 1 year": 0,
        "n/a": 0
    }
}


#Remove columns that would require too much processing. Convert columns to floats
loans = loans.drop(["last_credit_pull_d", "earliest_cr_line", "addr_state", "title"], axis=1)
loans["int_rate"] = loans["int_rate"].str.rstrip("%").astype("float")
loans["revol_util"] = loans["revol_util"].str.rstrip("%").astype("float")
loans = loans.replace(mapping_dict)

#Get dummy columns for categorical columns
cat_columns = ["home_ownership", "verification_status", "purpose", "term"]
dummy_df = pd.get_dummies(loans[cat_columns])
loans = pd.concat([loans, dummy_df], axis=1)
loans = loans.drop(cat_columns, axis=1)