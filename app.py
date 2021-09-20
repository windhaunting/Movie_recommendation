import numpy as np
import streamlit as st
import os
from collections import Counter
import random
import boto3
from boto3.dynamodb.conditions import Key, Attr
import pandas as pd
import plotly.express as px

db = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')

# Get and wait until the table exists.
course_plan_table = db.Table('CoursePlan')
course_plan_table.meta.client.get_waiter('table_exists').wait(TableName='CoursePlan')

# Query / Scan
response = course_plan_table.scan(
    FilterExpression=Attr('Age').eq(4)
)
course_plans_age_4 = response['Items']


c = Counter()
l = []
for course_plan in course_plans_age_4:
    c.update(course_plan['Activities'])
    l.extend(course_plan['Activities'])

# chart_data = pd.DataFrame(np.array(list(dict(c).items())), columns=["a"])

# chart_data = pd.DataFrame(np.array(l)[:, np.newaxis], columns=["a"])

df = pd.DataFrame(np.array(l)[:, np.newaxis], columns=["student activities in age 4 group"])
fig = px.histogram(df, x="student activities in age 4 group", category_orders={"student activities in age 4 group": sorted(l)})

# Designing the interface
st.title("Streamlit + DynamoDB + Visualization")

# For newline
st.sidebar.write('\n')
# st.write(f'{c}')

st.plotly_chart(fig, use_container_width=True)
# st.bar_chart(chart_data)

