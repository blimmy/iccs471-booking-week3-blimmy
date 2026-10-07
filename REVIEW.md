# REVIEW.md

## Identity

Name: Siriphanaphorn Sirikun  
Student ID: 6680085  
AI tool used: GitHub Copilot  
Discussion partners: Worked independently.

## Review decision

I inspected `service.py / move_booking`, especially this conflict check:

```python
other_bookings = [candidate for candidate in bookings if candidate is not booking]
if has_conflict(other_bookings, new_room, new_start, new_end):
    raise ValueError("Booking conflict")


## Remaining uncertainty

One thing I am still unsure about is whether the room name actually exists. The current code only checks that the room name is valid text, so the tests cannot confirm that the room is a real room.