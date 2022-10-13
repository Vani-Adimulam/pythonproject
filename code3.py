employees = [{
  "name": "Tina",
  "age": 30,
  "birthday": "1990-03-10",
  "job": "DevOps Engineer",
  "address": {
    "city": "New York",
    "country": "USA"
  }
},
{
  "name": "Tim",
  "age": 35,
  "birthday": "1985-02-21",
  "job": "Developer",
  "address": {
    "city": "Sydney",
    "country": "Australia"
  }
}]
n=int(input("Enter list number:"))
for i in range(0,n):
  for i in employees:
    print ("name:",i['name'])
    print ("job:",i["age"])
    print("city:",i["address"]["city"])
    print("\n")

print(employees[1]['address']['country'])

output:
Enter list number:2
name: Tina
job: 30
city: New York


name: Tim
job: 35
city: Sydney
Australia

Process finished with exit code 0

