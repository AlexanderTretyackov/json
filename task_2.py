import requests
import json

urlJobsHH = 'https://api.hh.ru/vacancies?text=python&only_with_salary=true&search_field=name&page={0}&per_page=100'

# вычисляем количество страниц
responseJobsHH = requests.get(urlJobsHH.format(0))
jobsJson = json.loads(responseJobsHH.text)
countPages = jobsJson['pages']

countJobs = 0
summaryTopSalary = 0
# проходим по всем страницам
for numberPage in range(0, countPages - 1):
    responseJobsHH = requests.get(urlJobsHH.format(numberPage))
    jobsJsonOnPage = json.loads(responseJobsHH.text)
    # проходим по всем вакансиям на текущей странице
    for job in jobsJsonOnPage['items']:
        jobSalary = job['salary']
        jobTopSalary = jobSalary['to']
        if jobSalary['currency'] == 'RUR' and jobTopSalary is not None:
            summaryTopSalary += jobTopSalary
            countJobs += 1
            # print(jobTopSalary)

print('Средняя зп: {0} рублей'.format(summaryTopSalary / countJobs))
