from flask import Flask, render_template, request
import pandas as pd  # Import pandas to use findfree function

app = Flask(__name__)

# Define findfree function
def find_free(user_input):
    # Load freelancer data from CSV file
    freelancers_df = pd.read_csv('freelancers.csv')
    
    # Function to find freelancers with a given skill sorted by rating
    def find_freelancers_with_skill(skill):
        freelancers_with_skill = freelancers_df[freelancers_df['skills'].str.contains(skill, case=False)]
        sorted_freelancers = freelancers_with_skill.sort_values(by='rating', ascending=False)
        return sorted_freelancers[['freelancer_id', 'name', 'skills', 'rating']]
    
    matching_freelancers = find_freelancers_with_skill(user_input)
    
    if not matching_freelancers.empty:
        return(matching_freelancers)
    else:
        return "No freelancers found with skill '{}'.".format(user_input)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        user_input = request.form["user_input"]
        processed_output = find_free(user_input)  # Corrected the variable name
        return render_template("index.html", processed_output=processed_output.to_html())


if __name__ == "__main__":
    app.run(debug=True)
