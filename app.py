import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly_express as px


exam_performance_df = pd.read_csv('./student_exams.csv')

# Rename columns in dataframe
exam_performance_df.rename(columns={
                            'race/ethnicity': 'ethnicity', 
                            'parental level of education': 'parent_education', 
                            'test preparation course': 'test_preparation_course',
                            'math score': 'math_score',
                            'reading score':'reading_score',
                            'writing score':'writing_score'}, inplace=True)

# Create a new column for average test scores
# Calculate sum of all test scores.
exam_totals = exam_performance_df['math_score'] + exam_performance_df['reading_score'] + exam_performance_df['writing_score']
# Calcualte average test score. 
exam_performance_df['average_score'] = exam_totals / 3



# Create a text header above the dataframe
st.header('Data viewer')
# Display the dataframe with streamlit
st.dataframe(exam_performance_df)

st.header('Number of students by ethnicity')
# Create a plotly histogram figure
fig = px.histogram(exam_performance_df, x='ethnicity', color='gender')
st.write(fig)

# Create a histogram to show the distribution of math, reading, and writing scores
def test_scores_histograms():
    # Create a 1x3 grid of subplots
    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(15, 5))

    
    axes[0].hist(exam_performance_df['math_score'], bins=10, alpha=0.5, label='math scores', edgecolor='black', color='orange')
    axes[0].set_title('Distribution of Math Scores')
    axes[0].set_xlabel('Score')
    axes[0].set_ylabel('Frequency')

    axes[1].hist(exam_performance_df['reading_score'], bins=10, alpha=0.5, label='reading scores', edgecolor='black', color='blue')
    axes[1].set_title('Distribution of Reading Scores')
    axes[1].set_xlabel('Score')
    axes[1].set_ylabel('Frequency')

    axes[2].hist(exam_performance_df['writing_score'], bins=10, alpha=0.5, label='writing scores', edgecolor='black', color='green')
    axes[2].set_title('Distribution of Writing Scores')
    axes[2].set_xlabel('Score')
    axes[2].set_ylabel('Frequency')

    plt.tight_layout()
    return fig

# Create title and description for the test scores histrogram 
st.title('Student Performance Histograms')
# Display the figure to Streamlit 
st.pyplot(test_scores_histograms())




# Box plot for average exam scores vs. parent education
st.title('Average Score by Parent Education')
fig = px.box(exam_performance_df, x='parent_education', y='average_score', 
             category_orders={"parent_education": sorted(exam_performance_df['parent_education'].unique())})
st.write(fig)

# Box plot for average exam scores vs. lunch type
st.title('Average Score by Lunch Type')
fig = px.box(exam_performance_df, x='lunch', y='average_score', 
             category_orders={"lunch": sorted(exam_performance_df['lunch'].unique())})
st.write(fig)

# Box plot for average exam scores vs. Test Preparation Course
st.title('Average Score by Test Preparation Course')
fig = px.box(exam_performance_df, x='test_preparation_course', y='average_score', 
             category_orders={"test_preparation_course": sorted(exam_performance_df['test_preparation_course'].unique())})
st.write(fig)

# Create a scatter matrix (pair plot)
fig = px.scatter_matrix(exam_performance_df, 
                        dimensions=['math_score', 'reading_score', 'writing_score'], 
)
st.title('Pair Plot of Exam Scores')
st.write(fig)