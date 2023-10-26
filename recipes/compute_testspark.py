# -*- coding: utf-8 -*-
import dataiku
from dataiku import spark as dkuspark
from pyspark import SparkContext
from pyspark.sql import SQLContext

sc = SparkContext.getOrCreate()
sqlContext = SQLContext(sc)

# Read recipe inputs
web_new_customers = dataiku.Dataset("web_new_customers")
web_new_customers_df = dkuspark.get_dataframe(sqlContext, web_new_customers)

# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a SparkSQL dataframe
testspark_df = web_new_customers_df # For this sample code, simply copy input to output

# Write recipe outputs
testspark = dataiku.Dataset("testspark")
dkuspark.write_with_schema(testspark, testspark_df)
