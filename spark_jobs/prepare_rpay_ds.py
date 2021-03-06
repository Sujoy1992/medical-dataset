from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *

import sys
import csv
import datetime

conf = SparkConf().setAppName('test_med_analysis')
sc = SparkContext(conf=conf)

input_location = sys.argv[1]
output_location = sys.argv[2]

spark = SparkSession \
    .builder \
    .appName("Create_Parquet") \
    .getOrCreate()

gpay = sc.textFile(input_location)

header_str = 'Change_Type,Covered_Recipient_Type,Noncovered_Recipient_Entity_Name,Teaching_Hospital_CCN,Teaching_Hospital_ID,Teaching_Hospital_Name,Physician_Profile_ID,Physician_First_Name,Physician_Middle_Name,Physician_Last_Name,Physician_Name_Suffix,Recipient_Primary_Business_Street_Address_Line1,Recipient_Primary_Business_Street_Address_Line2,Recipient_City,Recipient_State,Recipient_Zip_Code,Recipient_Country,Recipient_Province,Recipient_Postal_Code,Physician_Primary_Type,Physician_Specialty,Physician_License_State_code1,Physician_License_State_code2,Physician_License_State_code3,Physician_License_State_code4,Physician_License_State_code5,Principal_Investigator_1_Profile_ID,Principal_Investigator_1_First_Name,Principal_Investigator_1_Middle_Name,Principal_Investigator_1_Last_Name,Principal_Investigator_1_Name_Suffix,Principal_Investigator_1_Business_Street_Address_Line1,Principal_Investigator_1_Business_Street_Address_Line2,Principal_Investigator_1_City,Principal_Investigator_1_State,Principal_Investigator_1_Zip_Code,Principal_Investigator_1_Country,Principal_Investigator_1_Province,Principal_Investigator_1_Postal_Code,Principal_Investigator_1_Primary_Type,Principal_Investigator_1_Specialty,Principal_Investigator_1_License_State_code1,Principal_Investigator_1_License_State_code2,Principal_Investigator_1_License_State_code3,Principal_Investigator_1_License_State_code4,Principal_Investigator_1_License_State_code5,Principal_Investigator_2_Profile_ID,Principal_Investigator_2_First_Name,Principal_Investigator_2_Middle_Name,Principal_Investigator_2_Last_Name,Principal_Investigator_2_Name_Suffix,Principal_Investigator_2_Business_Street_Address_Line1,Principal_Investigator_2_Business_Street_Address_Line2,Principal_Investigator_2_City,Principal_Investigator_2_State,Principal_Investigator_2_Zip_Code,Principal_Investigator_2_Country,Principal_Investigator_2_Province,Principal_Investigator_2_Postal_Code,Principal_Investigator_2_Primary_Type,Principal_Investigator_2_Specialty,Principal_Investigator_2_License_State_code1,Principal_Investigator_2_License_State_code2,Principal_Investigator_2_License_State_code3,Principal_Investigator_2_License_State_code4,Principal_Investigator_2_License_State_code5,Principal_Investigator_3_Profile_ID,Principal_Investigator_3_First_Name,Principal_Investigator_3_Middle_Name,Principal_Investigator_3_Last_Name,Principal_Investigator_3_Name_Suffix,Principal_Investigator_3_Business_Street_Address_Line1,Principal_Investigator_3_Business_Street_Address_Line2,Principal_Investigator_3_City,Principal_Investigator_3_State,Principal_Investigator_3_Zip_Code,Principal_Investigator_3_Country,Principal_Investigator_3_Province,Principal_Investigator_3_Postal_Code,Principal_Investigator_3_Primary_Type,Principal_Investigator_3_Specialty,Principal_Investigator_3_License_State_code1,Principal_Investigator_3_License_State_code2,Principal_Investigator_3_License_State_code3,Principal_Investigator_3_License_State_code4,Principal_Investigator_3_License_State_code5,Principal_Investigator_4_Profile_ID,Principal_Investigator_4_First_Name,Principal_Investigator_4_Middle_Name,Principal_Investigator_4_Last_Name,Principal_Investigator_4_Name_Suffix,Principal_Investigator_4_Business_Street_Address_Line1,Principal_Investigator_4_Business_Street_Address_Line2,Principal_Investigator_4_City,Principal_Investigator_4_State,Principal_Investigator_4_Zip_Code,Principal_Investigator_4_Country,Principal_Investigator_4_Province,Principal_Investigator_4_Postal_Code,Principal_Investigator_4_Primary_Type,Principal_Investigator_4_Specialty,Principal_Investigator_4_License_State_code1,Principal_Investigator_4_License_State_code2,Principal_Investigator_4_License_State_code3,Principal_Investigator_4_License_State_code4,Principal_Investigator_4_License_State_code5,Principal_Investigator_5_Profile_ID,Principal_Investigator_5_First_Name,Principal_Investigator_5_Middle_Name,Principal_Investigator_5_Last_Name,Principal_Investigator_5_Name_Suffix,Principal_Investigator_5_Business_Street_Address_Line1,Principal_Investigator_5_Business_Street_Address_Line2,Principal_Investigator_5_City,Principal_Investigator_5_State,Principal_Investigator_5_Zip_Code,Principal_Investigator_5_Country,Principal_Investigator_5_Province,Principal_Investigator_5_Postal_Code,Principal_Investigator_5_Primary_Type,Principal_Investigator_5_Specialty,Principal_Investigator_5_License_State_code1,Principal_Investigator_5_License_State_code2,Principal_Investigator_5_License_State_code3,Principal_Investigator_5_License_State_code4,Principal_Investigator_5_License_State_code5,Submitting_Applicable_Manufacturer_or_Applicable_GPO_Name,Applicable_Manufacturer_or_Applicable_GPO_Making_Payment_ID,Applicable_Manufacturer_or_Applicable_GPO_Making_Payment_Name,Applicable_Manufacturer_or_Applicable_GPO_Making_Payment_State,Applicable_Manufacturer_or_Applicable_GPO_Making_Payment_Country,Related_Product_Indicator,Covered_or_Noncovered_Indicator_1,Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_1,Product_Category_or_Therapeutic_Area_1,Name_of_Drug_or_Biological_or_Device_or_Medical_Supply_1,Associated_Drug_or_Biological_NDC_1,Covered_or_Noncovered_Indicator_2,Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_2,Product_Category_or_Therapeutic_Area_2,Name_of_Drug_or_Biological_or_Device_or_Medical_Supply_2,Associated_Drug_or_Biological_NDC_2,Covered_or_Noncovered_Indicator_3,Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_3,Product_Category_or_Therapeutic_Area_3,Name_of_Drug_or_Biological_or_Device_or_Medical_Supply_3,Associated_Drug_or_Biological_NDC_3,Covered_or_Noncovered_Indicator_4,Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_4,Product_Category_or_Therapeutic_Area_4,Name_of_Drug_or_Biological_or_Device_or_Medical_Supply_4,Associated_Drug_or_Biological_NDC_4,Covered_or_Noncovered_Indicator_5,Indicate_Drug_or_Biological_or_Device_or_Medical_Supply_5,Product_Category_or_Therapeutic_Area_5,Name_of_Drug_or_Biological_or_Device_or_Medical_Supply_5,Associated_Drug_or_Biological_NDC_5,Total_Amount_of_Payment_USDollars,Date_of_Payment,Form_of_Payment_or_Transfer_of_Value,Expenditure_Category1,Expenditure_Category2,Expenditure_Category3,Expenditure_Category4,Expenditure_Category5,Expenditure_Category6,Preclinical_Research_Indicator,Delay_in_Publication_Indicator,Name_of_Study,Dispute_Status_for_Publication,Record_ID,Program_Year,Payment_Publication_Date,ClinicalTrials_Gov_Identifier,Research_Information_Link,Context_of_Research'

headers = header_str.split(',')
fields = [StructField(ele, StringType(), True) for ele in headers]

for ele in [4,6,26,46,66,86,106]:
    fields[ele].dataType = IntegerType()

fields[127].dataType = LongType()
fields[157].dataType = FloatType()
fields[158].dataType = TimestampType()

schema = StructType(fields)

def split_data(istr):
    l = []
    for i, ele in enumerate(csv.reader(istr.split(','))):
        if not ele and i in [4,6,26,46,66,86,106,127,157,158]:
            ele = [None]
        elif not ele:
            ele = [str()]
        l += ele
    return l

def create_tuple(il):
     jl = ()
     for i, e in enumerate(il):
          if i in [4,6,26,46,66,86,106] and e:
              jl += (int(e.strip('"')),)
          elif i in [127] and e:
              jl += (long(e.strip('"')),)
          elif i in [157] and e:
              jl += (float(e.strip('"')),)
          elif i in [158] and e:
              if '-' in e:
                  tl = e.strip('"').split('-')
                  jl += (datetime.datetime(int(tl[2]),int(tl[1]),int(tl[0])),)
              else:
                  tl = e.strip('"').split('/')
                  jl += (datetime.datetime(int(tl[2]),int(tl[0]),int(tl[1])),)
          else:
              jl += (e,)
     return jl

final_gpay = gpay.map(split_data).map(create_tuple)

gpay_df = spark.createDataFrame(final_gpay, schema)

# Writing the df as parquet with the default partiton
gpay_df.write.parquet(output_location)
