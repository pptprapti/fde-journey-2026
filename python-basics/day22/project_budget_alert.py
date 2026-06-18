project_budgets = {
    "SAP Migration": 120000,
    "AI Chatbot": 85000,
    "Data Warehouse": 150000,
    "Website Upgrade": 65000
}

def high_projects_budget(project_budgets):
    higher_projects = []
    for project in project_budgets:
        if project_budgets[project] > 100000:
            higher_projects.append(project)

    return higher_projects

result = high_projects_budget(project_budgets)

print(result)