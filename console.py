import pdb
from models.staff import Staff
from models.animal import Animal

import repositories.animal_repository as animal_repository
import repositories.staff_repository as staff_repository

# staff_repository.delete_all()
# animal_repository.delete_all()

staff1 = Staff("Jack", "03.03.2020", 1)
staff2 = Staff("Tom", "04.03.2020", 2)
staff3 = Staff("Joe", "05.03.2020", 3)
staff4 = Staff("Kev", "06.03.2020", 4)
staff7 = Staff("Charlie", "06.03.2020", 4, 35)
# staff_repository.save(staff1)
# staff_repository.save(staff2)
# staff_repository.save(staff3)
# staff_repository.save(staff4)
# staff_repository.save(staff7)
# staff_repository.update(staff7)

result = staff_repository.select_all()
for staff in result:
    print(staff.__dict__)
print("_________________________")
animal1 = Animal("Maksiss", "Cat", staff1)
animal2 = Animal("Lucia", "Dog", staff1)
animal3 = Animal("Missi", "Dog", staff2)
# animal_repository.save(animal1)
# animal_repository.save(animal2)
# animal_repository.save(animal3)

# result = animal_repository.select(3)
# print(result.__dict__)

result = animal_repository.select_all()

for animal in result:
    print(animal.__dict__)

# animal_single = animal_repository.select



# find_staff = staff_repository.select(25)
# print(find_staff.__dict__)


# pdb.set_trace()