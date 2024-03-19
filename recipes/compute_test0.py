# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
crm_last_month = dataiku.Dataset("crm_last_month")
crm_last_month_df = crm_last_month.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

test0_df = crm_last_month_df # For this sample code, simply copy input to output


# Write recipe outputs
test0 = dataiku.Dataset("test0")
test0.write_with_schema(test0_df)
