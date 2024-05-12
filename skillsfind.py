from browser import document  # Import document for DOM manipulation
from browser import window  # Import window for fetch API

import micropip
import pandas as pd
import io

async def install_pandas():
    await micropip.install("pandas")

# Load CSV data from provided URLs
async def load_csv_data():
    # Fetch CSV data using fetch API
    freelancers_response = await window.fetch('freelancers.csv')
    projects_response = await window.fetch('projects.csv')

    # Read CSV data into pandas DataFrames
    freelancers_text = await freelancers_response.text()
    projects_text = await projects_response.text()
    
    freelancers_df = pd.read_csv(io.StringIO(freelancers_text))
    projects_df = pd.read_csv(io.StringIO(projects_text))

    return freelancers_df, projects_df

# Function to find freelancers with a given skill sorted by rating
def find_freelancers_with_skill(df, skill):
    freelancers_with_skill = df[df['skills'].str.contains(skill, case=False)]
    sorted_freelancers = freelancers_with_skill.sort_values(by='rating', ascending=False)
    return sorted_freelancers[['freelancer_id', 'name', 'skills', 'rating']]

# Main program
async def main(event):
    # Install pandas
    await install_pandas()

    # Load CSV data
    freelancers_df, projects_df = await load_csv_data()

    # Get user input for skill
    skill_input = document['skilll'].value

    # Find freelancers with the given skill
    matching_freelancers = find_freelancers_with_skill(freelancers_df, skill_input)
    
    output_div = document['output']  # Get reference to output div
    
    if not matching_freelancers.empty:
        output_div.text = str(matching_freelancers)  # Display matching freelancers
    else:
        output_div.text = "No freelancers found with skill '{}'.".format(skill_input)

# Call main function when the page loads
document.bind('DOMContentLoaded', main)
