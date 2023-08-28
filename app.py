import pandas as pd
import streamlit as st
import plotly_express as px

exam_performance_df = pd.read_csv('./student_exams.csv')

# rename columns in dataframe
exam_performance_df.rename(columns={
                            'race/ethnicity': 'ethnicity', 
                            'parental level of education': 'parent_education', 
                            'test preparation course': 'test_preparation_course',
                            'math score': 'math_score',
                            'reading score':'reading_score',
                            'writing score':'writing_score'}, inplace=True)

# create a new column for average test scores
# calculate sum of all test scores.
exam_totals = exam_performance_df['math_score'] + exam_performance_df['reading_score'] + exam_performance_df['writing_score']
# calcualte average test score. 
exam_performance_df['average_score'] = exam_totals / 3



# create a text header above the dataframe
st.header('Data viewer')
# Display the dataframe with streamlit
st.dataframe(exam_performance_df)

st.header('Number of students by ethnicity')
# create a plotly histogram figure
fig = px.histogram(exam_performance_df, x='race/ethnicity', color='gender')
st.write(fig)


# Box plot for average exam scores vs. parent education
fig = px.box(exam_performance_df, x='parent_education', y='average_score', title='Average Score by Parent Education', 
             category_orders={"parent_education": sorted(exam_performance_df['parent_education'].unique())})
fig.show()
