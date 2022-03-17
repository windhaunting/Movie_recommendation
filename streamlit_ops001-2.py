#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 15:19:15 2022

@author: fubao
"""
import pandas as pd

import streamlit as st



def visualize ():
    
    st.set_page_config(layout="wide")

    st.markdown("""
    <style>
    .big-font {
        font-size:50px !important;
        color:Red;
    }
    
    .mid-font {
        font-size:30px !important;
        color:Blue;
    }
    
    </style>
    """, unsafe_allow_html=True)
    
    

    # initialization
    st.markdown('<p class="big-font">Daily Email Report to CEO </p>', unsafe_allow_html=True)
    
    df_ops002 = read_data()
    all_branches = df_ops002['Branch'].unique()   #.tolist()
    option_branch = st.selectbox(
        'Select A Branch:',
        all_branches)
    
    
    
    all_centers = df_ops002[df_ops002['Branch'] == option_branch]['Center'].unique()  
    option_center = st.selectbox(
        'Select A Center:',
        all_centers)
    
    all_groups = df_ops002[(df_ops002['Branch'] == option_branch)  & (df_ops002['Center'] == option_center)]['Group'].unique()  

    option_group = st.selectbox(
        'Select A Group:',
        all_groups)
    
    
    all_metrics = df_ops002.columns[5:]
    option_metric = st.selectbox(
        'Select A Metric to Display:',
        all_metrics)
    
    
    print("option_branchssssssssss: ", option_branch, option_center, option_group, option_metric)

    df_ops002 = df_ops002.rename(columns={'Date':'index'}).set_index('index')

    selected_times_rows = df_ops002[(df_ops002['Branch'] == option_branch)  & (df_ops002['Center'] == option_center) & (df_ops002['Group'] == option_group)]
    
    with st.container():
        st.markdown('<p class="mid-font"> Metric Trending by Date </p>', unsafe_allow_html=True)
    
        st.line_chart(selected_times_rows[option_metric])


    #st.title('Metric Trending by Date')



def read_data():
    
    data_ops002_path = 'data/fake_groups.csv'
    
    
    df_ops002 = pd.read_csv(data_ops002_path, index_col = None)
    return df_ops002
    
visualize()
