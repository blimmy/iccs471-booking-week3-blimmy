"""Add your two tests here. Keep the supplied baseline and smoke tests intact."""
import unittest

from models import Booking
from service import move_booking


class StudentMoveTests(unittest.TestCase):

    # Given: an active booking with no other booking blocking it.
    # When: it is moved in the same room to a time overlapping its own old interval.
    # Expect: the move succeeds on the same object with the requested new times.
    def test_self_overlap_is_allowed_and_preserves_booking(self):
        target = Booking(17, "Room 201", 600, 660)
        bookings = [target]

        result = move_booking(bookings, 17, "Room 201", 630, 690)

        self.assertIs(result, target)
        self.assertIs(bookings[0], target)
        self.assertEqual(target.id, 17)
        self.assertEqual(target.status, "active")
        self.assertEqual(target.room, "Room 201")
        self.assertEqual(target.start, 630)
        self.assertEqual(target.end, 690)
        self.assertEqual(len(bookings), 1)

    # Given: an active booking and another booking that should remain unchanged.
    # When: the booking's current room, start time, and end time are requested again.
    # Expect: the request succeeds on the same object and all booking data stays unchanged.
    def test_unchanged_request_succeeds_without_change(self):
        target = Booking(17, "Room 201", 600, 660)
        other = Booking(18, "Room 202", 700, 760)
        bookings = [target, other]

        result = move_booking(bookings, 17, "Room 201", 600, 660)

        self.assertIs(result, target)
        self.assertIs(bookings[0], target)
        self.assertIs(bookings[1], other)
        self.assertEqual(target, Booking(17, "Room 201", 600, 660))
        self.assertEqual(other, Booking(18, "Room 202", 700, 760))
        self.assertEqual(len(bookings), 2)


if __name__ == "__main__":
    unittest.main()