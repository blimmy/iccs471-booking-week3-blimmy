# Project guidance

- This project manages meeting-room bookings for one day using a Python list. Follow SPEC.md for the rules about moving bookings.
- Keep booking creation working as before. A move must use the same booking object and keep its ID, active status and list position. Failed moves must not change any records.
- For IA 3.1, prepare instructions only. For IA 3.2, work on move_booking in service.py and add two tests in test_student.py. Keep the model, function inputs, supplied tests, SPEC.md and fallback code unchanged. Use only Python’s standard library.
- Check creation with uv run --python 3.12 python -m unittest -v test_baseline. After implementation, run uv run --python 3.12 python -m unittest -v test_baseline test_move_smoke test_student.
- Explain any proposed rules.py helper change before approval. Stop after the agreed edits and checks, and show changed files, the diff and test results for review before committing.