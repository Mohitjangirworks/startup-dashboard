import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.set_page_config(layout='wide',page_title='Startup-Funding Analysis')

df=pd.read_csv('startup_cleaned1.csv')


def load_overall_analysis():
    st.title("Overall Analysis")



    col1,col2,col3,col4=st.columns(4)
    with col1:
        # total invested amount
        total = round(df['amount'].sum())
        st.metric("Total", str(total) + " Cr")
    with col2:
        # max amount infused in a startup
        max_funding = df.groupby('startup')['amount'].max().sort_values(ascending=False).head(1).values[0]
        st.metric("Max Funding", str(max_funding) + " Cr")




def load_investor_details(investor):
    st.title(investor)
    #load the recent 5 investments of ]\[pohe investor
    last5_df=df[df['investors'].str.contains(investor)].head(5)[
        ['date','startup','city', 'vertical', 'investors', 'round', 'amount']]
    st.subheader('Most Recent Investment')
    st.dataframe(last5_df)

    col1,col2=st.columns(2)
    with col1:
        #Biggest Investments
        bif_series=df[df['investors'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(ascending=False).head(10)
        st.subheader('Biggest Investments')


        from numpy.random import default_rng as rng
        arr = rng(0).normal(1, 1, size=100)
        fig, ax = plt.subplots(figsize=(12,7))
        ax.bar(bif_series.index,bif_series.values)
        plt.xticks(rotation=45)
        st.pyplot(fig)

    with (col2):
        verical_series=df[df['investors'].str.contains(investor)].groupby('vertical')['amount'].sum()

        st.subheader('Sectors Invested In')
        arr = rng(0).normal(1, 1, size=100)
        fig1, ax1 = plt.subplots(figsize=(12,6))
        ax1.pie(verical_series,labels=verical_series.index,autopct='%0.01f')
        plt.xticks(rotation=45,ha='right')
        plt.tight_layout()
        st.pyplot(fig1)

    col1, col2 = st.columns(2)
    with col1:
        # funding rounds Rounds
        st.subheader("Funding Rounds")

        round=df[df['investors'].str.contains(investor)].groupby('round')['amount'].sum()

        arr = rng(0).normal(1, 1, size=100)
        fig2, ax2 = plt.subplots(figsize=(12, 6))
        ax2.pie(round, labels=round.index, autopct='%0.01f')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        st.pyplot(fig2)

    with col2:
        # City wise investment
        st.subheader("City Wise Investments")

        city=df[df['investors'].str.contains(investor)].groupby('city')['amount'].sum()

        arr = rng(0).normal(1, 1, size=100)
        fig3, ax3 = plt.subplots(figsize=(12, 6))
        ax3.pie(city, labels=city.index, autopct='%0.01f')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        st.pyplot(fig3)

    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df['year'] = df['date'].dt.year
    year_series=df[df['investors'].str.contains(investor)].groupby('year')['amount'].sum()
    st.subheader("YoY Investment")
    fig4,ax4=plt.subplots()
    ax4.plot(year_series.index,year_series.values)
    st.pyplot(fig4)

st.sidebar.title('Startup Funding Analysis')
option=st.sidebar.selectbox('Select One',["Overall Analysis","Startup","Investor"])

if option == 'Overall Analysis':
    btn0=st.sidebar.button("Show Overall Analysis")
    if btn0:
        load_overall_analysis()

elif option=="Startup":
    st.sidebar.selectbox('Select Startup',sorted(df['startup'].unique().tolist()))
    st.title('Startup Analysis')
    btn1=st.sidebar.button('Find Startup Details')
else:
    selected_investor=st.sidebar.selectbox('Select Investor', df['investors'].unique().tolist())
    btn2 = st.sidebar.button('Find Investor Details')
    if btn2:
        load_investor_details(selected_investor)