import requests
print("--------Preferred Country ----------")
print("1.United States of America -- us\n2.Canada -- ca\n3.United Arab Emirates -- ae\n")

Country = input("Select a country( abbrevation ): ")

Job = input("Enter your job title:")

print("\n... Loading ...\n ")

url = "https://jsearch.p.rapidapi.com/search"
method ="GET"
querystring = {
    "query": Job,
    "page":"1",
    "num_pages":"1",
    "country":Country,
}

headers = {
	"x-rapidapi-key": "Type key",
	"x-rapidapi-host": "jsearch.p.rapidapi.com"
}

response = requests.request(method, url, params=querystring, headers=headers)
data = response.json()
print("------- JOB LISIT --------")
for job in data.get('data',[])[:5]:
    i=0
    print(f"Job Title: {job["job_title"]}")
    print(f"Company Name: {job["employer_name"]}")
    print(f"Job Location:{job["job_city"],job["job_country"]}")
    print(f"Employment Type: {job["job_employment_type"]}")
    print(f"Job Description: {job["job_description"]}")
    print(f"Apply: {job["job_apply_link"]}\n")
    print("-"*70)
