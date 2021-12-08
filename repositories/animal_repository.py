from db.run_sql import run_sql
from models.staff import Staff
from models.animal import Animal

import repositories.staff_repository as staff_repository



def save(animal):
    sql = "INSERT INTO animals (name, type, staff_id) VALUES (%s, %s, %s) RETURNING *"
    values = [animal.name, animal.type, animal.staff.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    animal.id = id
    return animal


def select_all():
    animals = []

    sql = "SELECT * FROM animals"
    results = run_sql(sql)

    for row in results:
        staff = staff_repository.select(row['staff_id'])
        animal = Animal(row['name'], row['type'], staff, row['id'] )
        animals.append(animal)
    return animals


def select(id):
    animal = None
    sql = "SELECT * FROM animals WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        staff = staff_repository.select(result['staff_id'])
        animal = Animal(result['name'], result['type'], staff, result['id'] )
    return animal


def delete_all():
    sql = "DELETE  FROM animals"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM animals WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(animal):
    sql = "UPDATE animals SET (name, type, staff_id) VALUES (%s, %s, %s) WHERE id = %s"
    values = [animal.name, animal.type, animal.staff.id]
    run_sql(sql, values)

