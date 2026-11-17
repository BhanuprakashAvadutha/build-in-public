jobs = [
    {"title": "AI Engineer", "city": "Hyderabad", "salary": 12},
    {"title": "Data Analyst", "city": "Pune", "salary": 7},
    {"title": "Agent Engineer", "city": "Hyderabad", "salary": 16},
    {"title": "ML Intern", "city": "Hyderabad", "salary": 4},
]

# 1. The titles of jobs with salary 10 or more
a = [job["title"] for job in jobs if job["salary"] >= 10]

# 2. Every job's city in uppercase
b = [job["city"].upper() for job in jobs]

# 3. The number of Hyderabad jobs with salary over 5
c = len([job for job in jobs if job["city"] == "Hyderabad" and job["salary"] > 5])

print("high pay:", a)
print("cities:", b)
print("hyd over 5:", c)
