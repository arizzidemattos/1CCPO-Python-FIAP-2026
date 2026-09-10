from datetime import date
def model_lead(name, email, company, stage):
 #estrutura e modela
    return {
        "name": name,
        "email": email,
        "company": company,
        "stage": stage,
        "created": date.today().isoformat()
    }
