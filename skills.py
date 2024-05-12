import pandas as pd

# Load freelancer and project data from CSV files
freelancers_df = pd.read_csv('freelancers.csv')
projects_df = pd.read_csv('projects.csv')

# Function to find freelancers with a given skill sorted by rating
def find_freelancers_with_skill(skill):
    freelancers_with_skill = freelancers_df[freelancers_df['skills'].str.contains(skill, case=False)]
    sorted_freelancers = freelancers_with_skill.sort_values(by='rating', ascending=False)
    return sorted_freelancers[['freelancer_id', 'name', 'skills', 'rating']]

# Main program
def findfree(user_input):
    
    matching_freelancers = find_freelancers_with_skill(user_input)
    
    if not matching_freelancers.empty:
        #print("Freelancers with skill '{}' sorted by rating are:".format(skill))
        return matching_freelancers
    else:
        #print("No freelancers found with skill '{}'.".format(skill))
        return "No freelancers found with skill '{}'.".format(user_input)

# Test the function
print(findfree("Python"))  # Replace "Python" with the skill you want to search for
