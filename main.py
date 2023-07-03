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
import matplotlib.pyplot as plt
import streamlit as st
from streamlit_folium import folium_static
st.set_option('deprecation.showPyplotGlobalUse', False)
# def create_map(df_no_duplicates):
#     # Create a map centered on the first location
#     map = folium.Map(location=[df_no_duplicates['latitude'].iloc[0], df_no_duplicates['longitude'].iloc[0]],
#                      zoom_start=10)
#
#     # # Add markers to the map for each location
#     # for index, row in df_no_duplicates.iterrows():
#     #     folium.Marker([row['latitude'], row['longitude']], popup=row['Name']).add_to(map)
#
#     # Display the map
#     # map
#     for index, row in df_no_duplicates.iterrows():
#         popup_text = f"Name: {row['Name']}<br>type: {row['type']}"
#         folium.Marker([row['latitude'], row['longitude']], popup=popup_text).add_to(map)
#
#     return map
def create_map(df, selected_types):
    if 'All' in selected_types:
        filtered_df = df  # Show all locations
    else:
        filtered_df = df[df['type'].isin(selected_types)]

        # Create a map centered on the first location
    # map = folium.Map(location=[df['lat'].iloc[0], df['lon'].iloc[0]], zoom_start=10)
    #
    # Filter the DataFrame based on selected types
    # filtered_df = df[df['type'].isin(selected_types)]

    # Create a map centered on the first location
    map = folium.Map(location=[df['latitude'].iloc[0], df['longitude'].iloc[0]], zoom_start=10)

    # Add markers to the map for each location
    for index, row in filtered_df.iterrows():
        popup_text = f"Name: {row['Name']}<br>Type: {row['type']}<br>Additional Info: {row['business_status']}"
        # if row['ty'] == 'Restaurant':
        #     icon = 'cutlery'
        #     color = 'red'
        # elif row['category'] == 'Store':
        #     icon = 'shopping-cart'
        #     color = 'blue'
        # elif row['category'] == 'Cafe':
        #     icon = 'coffee'
        #     color = 'green'
        # else:
        #     icon = 'info'
        #     color = 'gray'
        folium.Marker([row['latitude'], row['longitude']], popup=popup_text).add_to(map)
        # folium.Marker([row['latitude'], row['longitude']], popup=popup_text, icon=folium.Icon(icon=icon, prefix='fa', color=color)).add_to(map)

    return map
def plot_pie_chart(df):
    type_counts = df['type'].value_counts()
    labels = type_counts.index.tolist()
    values = type_counts.values.tolist()

    plt.figure(figsize=(8, 6))
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')
    plt.title('Location Types')
    plt.show()
    st.pyplot()
def plot_pie_chart(df, selected_types):
    if 'All' in selected_types:
        filtered_df = df  # Show all locations
    else:
        filtered_df = df[df['type'].isin(selected_types)]

    type_counts = filtered_df['type'].value_counts()
    labels = type_counts.index.tolist()
    values = type_counts.values.tolist()

    plt.figure(figsize=(8, 6))
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')
    plt.title('Location Types')
    plt.show()
    st.pyplot()
# def main():
#     # Load the data
#     df = pd.read_csv('prince_sultan.csv')  # Replace 'data.csv' with your data file
#
#     # Create the map
#     map = create_map(df)
#
#     # Set the page title
#     st.set_page_config(page_title='Map App')
#
#     # Add the map to the app
#     st.markdown('<h1 style="text-align: center;">Map App</h1>', unsafe_allow_html=True)
#     folium_static(map)
#    # Display additional information from the DataFrame
#     st.subheader('Location Details')
#     st.dataframe(df)

# def main():
#     # Load the data
#     df = pd.read_csv('prince_sultan.csv')  # Replace 'data.csv' with your data file
#
#     # Get unique types from the DataFrame
#     types = df['type'].unique().tolist()
#     types.append('All')
#     # Set the page title
#     st.set_page_config(page_title='REZONE')
#
#     # Add a title and instructions to the app
#     st.title('REZONE')
#     st.markdown('Select the types of locations to display on the map.')
#
#     # Add a multiselect widget to select types
#     selected_types = st.multiselect('Select Types', types)
#
#     # Create the map with filtered data
#     map = create_map(df, selected_types)
#
#     # Display the map
#     # folium_static(map)
#     # Add a section to display the location details when a marker is clicked
#     if st.checkbox('Show Location Details'):
#         if 'All' in selected_types:
#             selected_locations = df  # Show all locations
#         else:
#             selected_locations = df[df['type'].isin(selected_types)]
#         st.subheader('Location Details')
#         st.dataframe(selected_locations)
#
#     # Add a section to display the location details when a marker is clicked
#     # if st.checkbox('Show Location Details'):
#     #     selected_locations = df[df['type'].isin(selected_types)]
#     #     st.subheader('Location Details')
#     #     st.dataframe(selected_locations)
#     # Add a section to display the pie chart
#     st.sidebar.subheader('Location Type Distribution')
#     plot_pie_chart(df,selected_types)
#     # Create two columns for the map and pie chart
#     # Create columns for the map and pie chart
#     col1, col2 = st.columns([2, 1])
#
#     # Display the map in the left column
#     with col1:
#         folium_static(map)
#
#     # Display the pie chart in the right column
#     with col2:
#         if len(selected_types) > 1:
#             st.subheader('Location Type Distribution')
#             plot_pie_chart(df, selected_types)
#
#
# if __name__ == '__main__':
#     main()

def main():
    # Load the data
    df = pd.read_csv('prince_sultan.csv')  # Replace 'data.csv' with your data file

    # Get unique types from the DataFrame
    types = df['type'].unique().tolist()
    types.append('All')  # Add 'All' as an option

    # Set the page title
    st.set_page_config(page_title='Map App')

    # Add a title and instructions to the app
    st.title('Map App')
    st.markdown('Select the types of locations to display on the map.')

    # Add a multiselect widget to select types
    selected_types = st.multiselect('Select Types', types)

    # Create the map with filtered data
    map = create_map(df, selected_types)

    # Add a section to display the location details when a marker is clicked
    if st.checkbox('Show Location Details'):
        if 'All' in selected_types:
            selected_locations = df  # Show all locations
        else:
            selected_locations = df[df['type'].isin(selected_types)]
        st.subheader('Location Details')
        st.dataframe(selected_locations)

    # Display the map and pie chart side by side
    col1, col2 = st.columns([2, 1])

    # Display the map in the left column
    with col1:
        folium_static(map)

    # Display the pie chart in the right column
    with col2:
        if len(selected_types) > 1:
            st.subheader('Location Type Distribution')
            plot_pie_chart(df, selected_types)


if __name__ == '__main__':
    main()
