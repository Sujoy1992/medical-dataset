use medical_data;

create table gnrl_pay_text(
Change_Type string, 
Covered_Recipient_Type string, 
Teaching_Hospital_CCN string, 
Teaching_Hospital_ID int,
Teaching_Hospital_Name string,
Physician_Profile_ID int,
Physician_First_Name string,
Physician_Middle_Name string,
Physician_Last_Name string,
Physician_Name_Suffix string,
Recipient_Primary_Business_Street_Address_Line1 string,
Recipient_Primary_Business_Street_Address_Line2 string,
Recipient_City string,
Recipient_State string,	
Recipient_Zip_Code string,
Recipient_Country string,
Recipient_Province string,
Recipient_Postal_Code string,
Physician_Primary_Type string,
Physician_Specialty string,
Physician_License_State_code1 string,
Physician_License_State_code2 string,
Physician_License_State_code3 string,
Physician_License_State_code4 string,
Physician_License_State_code5 string,
Submitting_Applicable_Manufacturer_or_Applicable_GPO_Name string,
Applicable_Manufacturer_or_Applicable_GPO_Making_Payment_ID string,
Applicable_Manufacturer_or_Applicable_GPO_Making_Payment_Name string,
Applicable_Manufacturer_or_Applicable_GPO_Making_Payment_State string,
Applicable_Manufacturer_or_Applicable_GPO_Making_Payment_Country string,
Total_Amount_of_Payment_USDollars int,
Date_of_Payment string,
Number_of_Payments_Included_in_Total_Amount int,
Form_of_Payment_or_Transfer_of_Value string,
Nature_of_Payment_or_Transfer_of_Value string,
City_of_Travel string,
State_of_Travel string,
Country_of_Travel string,
Physician_Ownership_Indicator string,
Third_Party_Payment_Recipient_Indicator string,
Name_of_Third_Party_Entity_Receiving_Payment_or_Transfer_of_Value string,
Charity_Indicator string,
Third_Party_Equals_Covered_Recipient_Indicator string,
Contextual_Information string,
Delay_in_Publication_Indicator string,
Record_ID string,
Dispute_Status_for_Publication string,
Related_Product_Indicator string,
Covered_or_Noncovered_Indicator_1 string,
Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_1 string,
Product_Category_or_Therapeutic_Area_1 string,
Name_of_Drug_or_Biological_or_Device_or_Medical_Supply_1 string,
Associated_Drug_or_Biological_NDC_1 string,
Covered_or_Noncovered_Indicator_2 string,
Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_2 string,
Product_Category_or_Therapeutic_Area_2 string,
Name_of_Drug_or_Biological_or_Device_or_Medical_Supply_2 string,
Associated_Drug_or_Biological_NDC_2	string,
Covered_or_Noncovered_Indicator_3 string,
Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_3 string,
Product_Category_or_Therapeutic_Area_3 string,
Name_of_Drug_or_Biological_or_Device_or_Medical_Supply_3 string,
Associated_Drug_or_Biological_NDC_3 string,
Covered_or_Noncovered_Indicator_4 string,
Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_4 string,
Product_Category_or_Therapeutic_Area_4 string,
Name_of_Drug_or_Biological_or_Device_or_Medical_Supply_4 string,
Associated_Drug_or_Biological_NDC_4 string,
Covered_or_Noncovered_Indicator_5 string,
Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_5 string,
Product_Category_or_Therapeutic_Area_5 string,
Name_of_Drug_or_Biological_or_Device_or_Medical_Supply_5 string,
Associated_Drug_or_Biological_NDC_5 string,
Program_Year string,
Payment_Publication_Date string) row format delimited fields terminated by ',' stored as textfile tblproperties ("skip.header.line.count"="1");


load data local inpath '/tmp/sujoy_hive/output45.csv' into table gnrl_pay_text;
