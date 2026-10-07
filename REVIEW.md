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
    raise ValueError("Booking conflict")```

I decided to keep this change because the booking is not included in the conflict check. This means it will not conflict with its own old time when it moves in the same room. I also checked that the system validates the input and checks for conflicts before changing the booking. So, if the move is rejected, the booking data will stay the same.

# Check

## from A : Baseline command

```uv run --python 3.12 python -m unittest -v test_baseline```

## baseline result 

Baseline result:
Ran 6 tests
OK

Baseline commit ID:
b8be7d459e2912a8c37f6cd20a679c96a6e59a4b

Final suite command:
```uv run --python 3.12 python -m unittest -v test_baseline test_move_smoke test_student```

Final result:
Ran 11 tests in 0.000s
OK

The final suite included the six baseline creation tests, three supplied move smoke tests, and two tests in test_student.py.

## Remaining uncertainty

The tests do not check whether the room name is a real room. They only check that the room name is valid text.