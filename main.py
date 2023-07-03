# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
import pandas as pd
import folium
import streamlit as st
from streamlit_folium import folium_static

def create_map(df_no_duplicates):
    # Create a map centered on the first location
    map = folium.Map(location=[df_no_duplicates['latitude'].iloc[0], df_no_duplicates['longitude'].iloc[0]],
                     zoom_start=10)

    # # Add markers to the map for each location
    # for index, row in df_no_duplicates.iterrows():
    #     folium.Marker([row['latitude'], row['longitude']], popup=row['Name']).add_to(map)

    # Display the map
    # map
    for index, row in df_no_duplicates.iterrows():
        popup_text = f"Name: {row['Name']}<br>type: {row['type']}"
        folium.Marker([row['latitude'], row['longitude']], popup=popup_text).add_to(map)

    return map

def main():
    # Load the data
    df = pd.read_csv('prince_sultan.csv')  # Replace 'data.csv' with your data file

    # Create the map
    map = create_map(df)

    # Set the page title
    st.set_page_config(page_title='Map App')

    # Add the map to the app
    st.markdown('<h1 style="text-align: center;">Map App</h1>', unsafe_allow_html=True)
    folium_static(map)
   # Display additional information from the DataFrame
    st.subheader('Location Details')
    st.dataframe(df)


if __name__ == '__main__':
    main()


