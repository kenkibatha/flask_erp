from peewee import *
try:
    db = PostgresqlDatabase('dadkndlg1rgv8a', user='tofkydlqohcxro', password="f24a573fa1f2b245e98fee28d6b9ab65235c8683ff2c97fd4ac17e40893a33c5", host="ec2-50-17-203-51.compute-1.amazonaws.com")
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