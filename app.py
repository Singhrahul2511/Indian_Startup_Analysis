
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout='wide', page_title='StartUp Analysis')

df = pd.read_csv('startup_cleaned_updated.csv')
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year

# Normalize startup names
df['startup'] = df['startup'].str.strip().str.title()

def load_overall_analysis():
    st.title('Overall Analysis')

    total = round(df['amount'].sum())
    max_funding = df.groupby('startup')['amount'].max().sort_values(ascending=False).head(1).values[0]
    avg_funding = df.groupby('startup')['amount'].sum().mean()
    num_startups = df['startup'].nunique()

    col1, col2, col3, col4 = st.columns(4)
    col1.metric('Total', str(total) + ' Cr')
    col2.metric('Max', str(max_funding) + ' Cr')
    col3.metric('Avg', str(round(avg_funding)) + ' Cr')
    col4.metric('Funded Startups', num_startups)

    st.header('MoM graph')
    selected_option = st.selectbox('Select Type', ['Total', 'Count'])
    if selected_option == 'Total':
        temp_df = df.groupby(['year', 'month'])['amount'].sum().reset_index()
    else:
        temp_df = df.groupby(['year', 'month'])['amount'].count().reset_index()

    temp_df['x_axis'] = temp_df['month'].astype('str') + '-' + temp_df['year'].astype('str')
    fig3, ax3 = plt.subplots()
    ax3.plot(temp_df['x_axis'], temp_df['amount'])
    st.pyplot(fig3)

    st.header('Sector-wise Funding (Sum + Count)')
    sector_df = df.groupby('vertical')['amount'].agg(['sum', 'count']).sort_values(by='sum', ascending=False).head(10)
    st.dataframe(sector_df)

    st.header('Funding Type Distribution')
    round_df = df['round'].value_counts()
    fig4, ax4 = plt.subplots()
    ax4.pie(round_df, labels=round_df.index, autopct="%0.01f%%")
    st.pyplot(fig4)

    st.header('City-wise Funding')
    city_df = df.groupby('city')['amount'].sum().sort_values(ascending=False).head(10)
    fig5, ax5 = plt.subplots()
    ax5.bar(city_df.index, city_df.values)
    st.pyplot(fig5)

    st.header('Funding Heatmap')
    heatmap_df = df.pivot_table(index='month', columns='year', values='amount', aggfunc='sum', fill_value=0)
    fig6, ax6 = plt.subplots(figsize=(10, 5))
    sns.heatmap(heatmap_df, annot=True, fmt=".0f", cmap='YlGnBu', ax=ax6)
    st.pyplot(fig6)

def load_company_details(company):
    st.title(company)
    company = company.strip().title()
    temp_df = df[df['startup'].str.strip().str.title() == company]

    if temp_df.empty:
        st.warning("Company data not found.")
        return

    st.subheader('Basic Information')
    # st.write(f"**Founded by:** {', '.join(temp_df['founder'].dropna().unique())}")
    st.write(f"**Industry:** {', '.join(temp_df['vertical'].dropna().unique())}")
    st.write(f"**Subindustry:** {', '.join(temp_df['subvertical'].dropna().unique())}")
    st.write(f"**City:** {', '.join(temp_df['city'].dropna().unique())}")
    st.write(f"**Funding Rounds:** {temp_df.shape[0]}")
    st.write(f"**Investors:** {', '.join(temp_df['investors'].dropna().unique())}")

    st.subheader('Funding Timeline')
    fig, ax = plt.subplots()
    ax.plot(temp_df['date'], temp_df['amount'])
    ax.set_ylabel("Amount")
    st.pyplot(fig)

def load_top_startups():
    st.title('Top Funded Startups Year-wise')
    years = sorted(df['year'].dropna().unique().tolist())
    for y in years:
        temp_df = df[df['year'] == y].groupby('startup')['amount'].sum().sort_values(ascending=False).head(5)
        st.subheader(f'Top Startups in {int(y)}')
        st.dataframe(temp_df)

def load_investor_details(investor):
    st.title(investor)
    last5_df = df[df['investors'].str.contains(investor, na=False)].head()[['date', 'startup', 'vertical', 'city', 'round', 'amount']]
    st.subheader('Most Recent Investments')
    st.dataframe(last5_df)

    col1, col2 = st.columns(2)
    with col1:
        big_series = df[df['investors'].str.contains(investor, na=False)].groupby('startup')['amount'].sum().sort_values(ascending=False).head()
        st.subheader('Biggest Investments')
        fig, ax = plt.subplots()
        ax.bar(big_series.index, big_series.values)
        st.pyplot(fig)

    with col2:
        vertical_series = df[df['investors'].str.contains(investor, na=False)].groupby('vertical')['amount'].sum()
        st.subheader('Sectors invested in')
        fig1, ax1 = plt.subplots()
        ax1.pie(vertical_series, labels=vertical_series.index, autopct="%0.01f%%")
        st.pyplot(fig1)

    year_series = df[df['investors'].str.contains(investor, na=False)].groupby('year')['amount'].sum()
    st.subheader('YoY Investment')
    fig2, ax2 = plt.subplots()
    ax2.plot(year_series.index, year_series.values)
    st.pyplot(fig2)

# Sidebar Navigation
st.sidebar.title('Startup Funding Analysis')
option = st.sidebar.selectbox('Select One', ['Overall Analysis', 'StartUp', 'Investor', 'Company', 'Top Startups'])

if option == 'Overall Analysis':
    load_overall_analysis()

elif option == 'StartUp':
    selected_startup = st.sidebar.selectbox('Select StartUp', sorted(df['startup'].unique()))
    btn1 = st.sidebar.button('Find StartUp Details')
    if btn1:
        load_company_details(selected_startup)

elif option == 'Investor':
    selected_investor = st.sidebar.selectbox('Select Investor', sorted(set(df['investors'].dropna().str.split(',').sum())))
    btn2 = st.sidebar.button('Find Investor Details')
    if btn2:
        load_investor_details(selected_investor)

elif option == 'Company':
    selected_company = st.sidebar.selectbox('Select Company', sorted(df['startup'].unique()))
    btn3 = st.sidebar.button('View Company POV')
    if btn3:
        load_company_details(selected_company)

elif option == 'Top Startups':
    load_top_startups()
