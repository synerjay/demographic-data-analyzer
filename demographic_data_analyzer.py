import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    adult_df = pd.read_csv('adult.data.csv')

    
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = adult_df['race'].value_counts()

    # What is the average age of men?
    mask1 = adult_df["sex"] == "Male"
    average_age_men = round(adult_df[mask1]["age"].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    mask2 = adult_df["education"] == "Bachelors"
    total_bachelors = adult_df[mask2]["education"].value_counts()["Bachelors"]
    total_number = adult_df.count()["education"]

    percentage_bachelors = ((total_bachelors / total_number ) * 100).round(decimals=1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    mask3 = (adult_df["education"] == "Bachelors") | (adult_df["education"] == "Masters") | (adult_df["education"] == "Doctorate")
    higher_education = adult_df[mask3]
    total_advanced = higher_education.count()["salary"]

    total_advanced_rich = higher_education[higher_education["salary"] == ">50K"].count()["salary"]

    no_edu_df = adult_df[(adult_df["education"] != "Bachelors") & (adult_df["education"] != "Masters") & (adult_df["education"] != "Doctorate")]
    total_noedu = no_edu_df.count()["salary"]
    total_richno = no_edu_df[no_edu_df["salary"] == ">50K"].count()["salary"]

    # with and without `Bachelors`, `Masters`, or `Doctorate`

    # percentage with salary >50K
    higher_education_rich = ((total_advanced_rich / total_advanced) * 100).round(decimals=1)
    lower_education_rich = ((total_richno / total_noedu) * 100).round(decimals=1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = adult_df["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    total_people = adult_df[adult_df["hours-per-week"] == 1]
    rich_lazy = total_people[total_people["salary"] == ">50K"]

    rich_percentage = (rich_lazy["salary"].count() / total_people["salary"].count()) * 100

    # What country has the highest percentage of people that earn >50K?
    high_earners = adult_df[adult_df["salary"] == ">50K"]
    high_earner_series = high_earners["native-country"].value_counts()
    general_series = adult_df["native-country"].value_counts()
    highest_percentage_list = (high_earner_series / general_series) * 100

    highest_earning_country = highest_percentage_list.idxmax()
    highest_earning_country_percentage = round(highest_percentage_list.max(), 1)

    # Identify the most popular occupation for those who earn >50K in India.
    indian_highearners = high_earners[high_earners["native-country"] == "India"]

    top_IN_occupation = indian_highearners["occupation"].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
