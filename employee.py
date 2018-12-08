from peewee import *
try:
    db = PostgresqlDatabase('de1nt7vbfksmog', user='ublxupfpivllrm', password="66d14b11f59bced90818c7b6227af8ae10378a6200f2c9ec620477fff033633f", host="ec2-54-235-156-60.compute-1.amazonaws.com")
    print("Successfully connected!")
except:
    print("Didn't connect!")


class Employee(Model):
    full_name = CharField()
    kra_pin_number = CharField()
    department = CharField()
    position = CharField()
    basic_salary = FloatField()
    house_allowance = FloatField()

    class Meta:
        database = db # This model uses the "people.db" database.
        table_name = "employees"


Employee.create_table(fail_silently=True)