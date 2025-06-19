#!python

"""
Create a query to create a table to store pets information into a database for a veterinarian
Each record needs to have the following information:
id unique integer identifier
pet name
pet species (dog, cat)
pet breed (collie, beagle, persian, etc)
pet age
pet gender
pet neutered or spayed
owner ID

choose appropriate variable types for each field
create the database and add the following information. Make sure you commit the information to save it:
name            species         breed           age  gender     spayed/neutered?    ownerID
Fluffy          dog             Pomeraniam      5    m          true                101
Benjamin        cat             Siberian        8    m          true                103
Casey           cat             Siberian        8    m          true                103
Friend          cat             Domestic        4    m          false               102
Copper          dog             Beagle          12   m          true                104
"""

import sqlite3

dbase = 'dbase.db'
connection = sqlite3.connect(dbase)
print(connection)

cursor = connection.cursor()
query ="""
CREATE TABLE if not exists vet_pets (
    id integer primary key autoincrement,
    name tinytext,
    species tinytext,
    breed tinytext,
    age int,
    gender char(1),
    spayed_neutered boolean,
    owner_id int);
"""
cursor.execute(query)
connection.commit()

vet_pets = [
    ("Fluffy", "dog", "Pomeranian", 5, "m", True, 101),
    ("Benjamin", "cat", "Siberian", 8, "m", True, 103),
    ("Casey", "cat", "Siberian", 8, "m", True, 103),
    ("Friend", "cat", "Domestic", 4, "m", False, 102),
    ("Copper", "dog", "Beagle", 12, "m", True, 104)
]

for pet in vet_pets:
    query = f"""
    INSERT INTO vet_pets (name, species, breed, age, gender, spayed_neutered, owner_id)
    VALUES ('{pet[0]}', '{pet[1]}', '{pet[2]}', {pet[3]}, '{pet[4]}', {pet[5]}, {pet[6]});
    """
    cursor.execute(query)

connection.commit()