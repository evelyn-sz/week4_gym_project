from db.run_sql import run_sql
from models.activity import Activity
from models.member import Member 
from models.booking import Booking 
import repositories.activity_repository as activity_repository
import repositories.member_repository as member_repository
import repositories.booking_repository as booking_repository
import pdb


def save(booking):
    if number_of_participants(booking.activity) < booking.activity.capacity:
        sql = "INSERT INTO bookings (member_id, activity_id) VALUES (%s, %s) RETURNING id"
        values = (booking.member.id, booking.activity.id)
        results = run_sql(sql, values)
        id = results[0]['id']
        booking.id = id
        return booking
    else:  
        return None
    
#below, code for finishing second extension
# def save(booking):

#     if number_of_participants(booking.activity) < booking.activity.capacity:
#         if booking.member.membership_type == "basic" and booking.activity.offpeak == False: 
#             return False
    
    
#         if (booking.member.membership_type == "pro") or (booking.member.membership_type == "basic" and booking.activity.offpeak == True):
#             sql = "INSERT INTO bookings (member_id, activity_id) VALUES (%s, %s) RETURNING id"
#             values = (booking.member.id, booking.activity.id)
#             results = run_sql(sql, values)
#             id = results[0]['id']
#             booking.id = id
#             # pdb.set_trace()
#             return booking
#     else:
#         return None

# if capacity < full
    #if membership == pro:
        #sign_up
    #elif:
        #membership == basic AND class == offpeak:
            # sign up
        #else:
            # don't sign up because unsuitable membership
# else:
    #don't sign up because class is full


def select_all():
    bookings = []

    sql = "SELECT * FROM bookings"
    results = run_sql(sql)

    for row in results:
        member = member_repository.select(row['member_id'])
        activity = activity_repository.select(row['activity_id'])
        booking = Booking(member, activity, row['id'])
        bookings.append(booking)
    return bookings

def select(id):
    sql = "SELECT * FROM bookings WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        member = member_repository.select(result["member_id"])
        activity = activity_repository.select(result["activity_id"])
        booking = Booking(member, activity, result["id"])
    return booking


def member(booking):
    sql = "SELECT * FROM members WHERE id = %s"
    values = [booking.member.id]
    results = run_sql(sql, values)[0]
    member = Member(results['first_name'], results['last_name'], results['membership_type'], results['id'])
    return member

def activity(booking):
    sql = "SELECT * FROM activities WHERE id = %s"
    values = [booking.activity.id]
    results = run_sql(sql, values)[0]
    activity = Activity(results['name'], results['venue'], results['category'], results['capacity'], results['finished'], results['offpeak'], results['id'])
    return activity

def number_of_participants(activity):
    sql = "SELECT COUNT(*) FROM bookings WHERE activity_id = %s"
    values = [activity.id]
    results = run_sql(sql, values)[0]
    return results["count"]
    
def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM bookings WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(booking):
    sql = "UPDATE bookings SET (member_id, activity_id) = (%s, %s) WHERE id = %s"
    values = [booking.member.id, booking.activity.id, booking.id]
    run_sql(sql, values)
