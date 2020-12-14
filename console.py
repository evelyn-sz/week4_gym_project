import pdb
from models.member import Member 
from models.activity import Activity 
from models.booking import Booking  
import repositories.member_repository as member_repository
import repositories.activity_repository as activity_repository
import repositories.booking_repository as booking_repository

booking_repository.delete_all()
activity_repository.delete_all()
member_repository.delete_all()

geralt = Member("Geralt", "of Rivia")
ciri = Member("Ciri", "of Cintra")
yennefer = Member("Yennefer", "of Vengerberg")
tris = Member("Tris", "Merigold")
renfri = Member("Renfri", "of Creyden")
striga = Member("Striga", "the Monster")

member_repository.save(geralt)
member_repository.save(ciri)
member_repository.save(yennefer)
member_repository.save(tris)
member_repository.save(renfri)
member_repository.save(striga)

emotions = Activity("Emotions Yoga", "Djinn's Bottle", "hollistic", False)
sword = Activity("Sword Fighting", "Kaer Morhen", "essentials", False)
spells = Activity("Spells", "Aretuza", "magic", False)
claws = Activity("Claws Shredding", "Vizima", "monstery arts", False)

activity_repository.save(emotions)
activity_repository.save(sword)
activity_repository.save(spells)
activity_repository.save(claws)

booking_1 = Booking(geralt, emotions)
booking_2 = Booking(ciri, sword)
booking_3 = Booking(yennefer, spells)
booking_4 = Booking(tris, spells)
booking_5 = Booking(ciri, spells)
booking_6 = Booking(striga, claws)
booking_7 = Booking(renfri, sword)


booking_repository.save(booking_1)
booking_repository.save(booking_2)
booking_repository.save(booking_3)
booking_repository.save(booking_4)
booking_repository.save(booking_5)
booking_repository.save(booking_6)
booking_repository.save(booking_7)

for member in member_repository.select_all():
    print(member.__dict__)
for activity in activity_repository.select_all():
    print(activity.__dict__)
for booking in booking_repository.select_all():
    print(booking.__dict__)
    