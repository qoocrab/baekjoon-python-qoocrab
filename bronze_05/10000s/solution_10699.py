# Time Complexity: O(1)
# Space Complexity: O(1)
from datetime import datetime, timedelta

seoul_time = datetime.now() + timedelta(hours=9)
print(seoul_time.strftime('%Y-%m-%d'))