
from collections import deque
#temperatures = [34,34,47,47,34,34,34,47,34,47,47,47,34,34,34,47,47,34,47,47,34,34,34,34,47,34,34,47,34,34,34,47,47,47,47,47,47,34,34,34,47,34,34,47,34,47,47,47,34,47,47,34,47,34,47,47,34,47,47,34,34,47,47,47,34,34,47,47,47,34,34,47,34,34,34,47,47,34,34,47,47,47,47,47,34,34,34,47,47,34,47,34,47,34,34,47,34,47,47,47,47,47,47,34,34,34,47,34,47,34,47,34,34,34,34,47,34,34,34,34,34,34,34,47,34,34,47,47,34,47,47,47,47,47,47,47,34,34,47,34,47,34,47,34,34,34,47,34,34,47,34,47,47,34,47,47,47,47,34,34,34,34,47,47,34,34,34,47,34,34,47,34,34,47,34,34,34,34,47,34,34,34,47,34,34,47,47,34,47,47,34,34,34,34,34,34,47,47,34,47,34,47,34,47,47,47,34,47,34,34,34,34,34,47,47,47,47,47,47,34,47,34,47,34,34,34,47,47,47,34,47,47,34,47,47,47,34,47,47,34,47,47,34,47,34,34,47,47,34,34,34,34,47,34,34,47,47,34,47,47,34,34,34,34,47,47,34,34,47,47,34,47,34,47,34,47,47,47,47,34,34,47,47,34,34,34,47,34,47,47,47,34,47,47,34,34,34,34,34,47,47,34,47,47,34,34,47,34,47,47,34,47,47,47,47,47,47,47,34,34,34,34,47,47,34,47,34,47,47,34,47,47,34,34,34,47,47,47,34,47,34,47,47,47,34,34,34,34,34,34,34,47,34,34,34,34,47,47,34,34,47,34,47,47,34,47,34,34,47,47,47,47,47,47,34,34,47,34,34,47,34,47,47,47,47,47,34,34,34,47,47,34,47,34,34,47,47,47,34,34,47,47,47,34,34,47,47,34,34,47,47,47,47,34,34,34,47,34,34,47,47,34,34,34,47,34,34,47,34,34,34,34,47,34,47,34,47,47,47,34,34,47,47,47,47,47,34,47,34,34,34,34,34,47,47,34,34,47,47,34,34,47,34,47,34,47,34,47,47,47,47,47,47,47,47,47,34,47,47,47,34,47,47,34,34,47,34,47,34,34,47,47,47,47,34,47,34,34,34,47,47,47,34,34,47,47,34,34,34,34,47,47,34,47,34,34,47,47,34,47,34,47,34,47,34,34,47,34,47,34,47,34,47,47,47,47,47,34,34,47,47,34,34,34,47,34,34,34,34,34,47,47,47,34,47,47,47,47,47,47,47,47,34,34,34,34,47,34,47,34,47,47,47,34,34,34,34,47,34,47,34,47,34,47,34,34,34,47,34,47,34,34,47,34,34,47,34,34,47,47,47,34,47,47,47,34,34,34,34,34,34,34,47,34,34,47,34,47,34,47,34,34,34,34,47,47,47,47,34,47,34,34,34,47,34,47,47,47,34,34,47,34,47,47,34,47,34,34,34,47,34,34,34,47,34,34,34,34,34,34,47,47,47,47,34,47,47,34,47,34,47,34,47,34,47,34,34,47,34,47,34,47,34,34,34,34,34,47,47,47,47,47,47,47,47,47,34,47,47,34,34,34,47,34,34,47,47,34,47,47,47,47,47,47,47,34,47,34,47,47,47,47,47,47,34,47,47,34,34,34,47,47,47,47,34,34,47,47,34,34,34,34,34,47,34,34,34,34,47,47,34,47,47,47,47,47,47,47,34,34,47,34,47,34,47,47,47,47,34,47,47,47,34,34,34,34,34,34,47,47,47,34,34,34,47,47,34,47,34,47,47,47,34,47,47,47,47,47,47,47,34,47,47,47,34,34,47,47,34,47,47,34,34,34,47,34,47,34,34,47,34,47,34,34,34,34,47,47,47,34,47,34,47,47,34,47,34,47,34,47,34,47,47,47,34,34,47,34,47,34,47,47,47,47,47,34,47,34,47,34,47,34,34,47,47,47,47,47,34,47,34,47,47,47,47,47,47,47,34,47,47,47,34,34,34,47,34,47,47,47,47,34,47,47,34,47,34,34,47,47,34,34,47,34,47,47,47,47,34,47,47,34,34,34,47,47,34,34,47,34,47,34,47,34,47,47,47,47,34,47,47,34,34,34,47,34,47,34,47,34,34,34,47,34,34,34,34,34,34,47,47,47,34,47,47,47,34,34,34,34,47,34,34,47,34,34,47,47,34,34,47,34,34,47,34,34,47,34,47,47,34,47,47,34,34,47,47,34,34,47,34,34,47,47,34,47,34,34,47,47,47,34,34,47,47,34,34,34,47,47,34,47,34,47,47,34,34,34,47,47,47,47,34,47,47,34,47,47,34,47,34,47,34,47,47,34,34,47,47,47,34,47,47,47,34,34,34,47,47,47,47,34,47,47,34,34,34,34,34,34,34,34,47,34,47,47,34,47,47,34,47,47,47,47,47,34,47,34,34,34,34,47,47,47,47,34,34,34,47,34,34,34,47,47,34,47,47,34,47,34,34,34,47,34,47,47,47,34,34,34,34,47,47,47,34,47,47,47,34,47,34,47,34,34,47,47,47,47,34,47,34,47,34,47,34,34,34,47,34,34,34,47,34,34,47,34,47,34,47,47,34,34,47,34,47,47,47,34,47,34,47,34,47,47,47,47,34,34,34,34,34,34,34,47,47,47,47,34,47,34,34,47,34,47,34,34,34,47,47,34,34,34,47,34,47,47,47,34,34,47,47,47,47,34,34,34,47,47,34,47,34,34,34,34,34,47,47,47,47,47,34,34,34,34,47,47,34,47,47,47,34,34,47,34,34,34,34,34,34,34,47,47,34,47,34,47,47,34,47,47,47,34,34,47,47,34,34,34,47,47,47,34,34,34,34,47,34,47,34,34,47,47,47,47,34,47,34,47,47,47,47,34,34,47,47,47,34,47,34,47,34,34,47,34,47,47,47,34,34,34,34,47,47,47,34,34,47,47,47,34,34,47,34,47,34,47,34,47,34,34,47,47,47,34,47,34,47,47,47,34,34,34,34,34,47,34,47,47,47,47,34,47,47,47,47,34,34,47,47,47,34,34,34,34,34,47,34,47,47,34,47,47,47,34,47,34,47,47,34,47,34,47,34,34,47,34,34,47,34,34,34,34,34,47,34,47,34,47,47,34,47,47,34,34,47,34,34,47,34,34,47,47,34,47,34,34,47,47,47,47,47,34,47,47,47,47,34,34,34,47,47,34,34,34,47,34,34,47,47,34,34,47,34,34,34,47,47,47,34,34,34,47,47,47,34,47,47,34,47,34,34,47,47,47,34,47,34,47,34,34,47,34,34,47,47,34,34,47,47,34,34,47,47,47,34,34,47,34,34,47,47,47,34,34,47,34,34,34,47,47,47,34,34,47,47,34,34,47,47,34,34,47,47,47,47,47,34,47,47,47,34,47,47,34,34,47,34,47,34,34,34,47,47,47,47,47,47,34,34,47,47,47,34,34,34,34,34,34,34,34,47,34,34,34,34,34,47,34,34,34,47,47,34,34,34,47,34,47,47,34,47,34,34,34,47,47,34,47,34,47,34,34,47,34,47,34,34,47,47,34,34,34,47,34,34,34,34,47,34,47,47,34,34,34,47,47,34,34,34,47,47,47,34,34,47,34,47,34,47,34,34,34,47,34,47,34,34,34,47,47,34,34,47,34,47,34,34,34,34,47,47,47,47,47,34,47,47,34,47,34,34,34,34,34,34,34,47,47,34,34,47,47,47,34,34,34,47,34,34,34,34,34,47,34,47,47,34,47,47,34,34,34,34,47,34,34,47,47,34,34,34,34,47,47,47,47,34,47,34,47,47,34,34,47,34,47,47,34,34,34,34,34,34,34,47,34,34,34,47,34,34,34,34,34,47,47,47,47,34,47,47,34,34,47,34,47,47,34,34,34,47,47,34,47,47,47,47,47,34,47,34,34,47,47,34,34,34,47,47,34,34,47,34,34,34,47,34,34,47,47,34,47,34,34,47,47,47,47,34,34,34,34,34,34,34,47,47,47,34,34,47,47,47,34,47,34,47,34,34,47,47,47,47,34,47,34,47,47,34,34,34,34,47,47,47,47,34,34,47,34,34,47,34,34,47,34,47,34,34,47,34,34,34,47,34,34,34,47,47,47,34,47,34,34,47,47,47,34,34,47,34,47,47,34,47,47,47,47,47,34,34,34,47,34,34,34,34,47,34,34,47,34,34,34,34,47,47,34,47,47,34,47,34,34,47,34,47,47,47,34,47,34,34,34,47,47,47,47,34,47,47,34,34,47,47,34,47,47,34,47,34,34,47,34,34,34,34,34,34,47,47,47,34,47,34,34,34,47,47,34,47,34,47,34,47,34,34,47,34,34,34,47,34,34,47,34,34,47,47,47,34,47,47,34,34,47,47,34,34,34,34,34,34,47,47,34,34,47,34,34,47,34,47,47,34,47,47,34,47,34,34,34,47,34,34,47,34,34,34,34,47,47,34,47,34,34,34,47,47,47,34,34,34,47,34,47,34,34,34,34,47,34,34,34,34,34,47,34,34,34,47,47,34,34,34,47,34,34,47,34,34,34,34,47,34,47,34,34,47,34,34,47,47,47,47,47,34,47,34,47,47,47,47,47,47,47,47,47,34,34,34,34,47,47,47,34,47,47,34,47,47,47,47,34,47,34,34,34,47,34,34,47,47,34,47,47,34,34,34,47,34,34,47,47,47,47,47,34,47,34,34,34,47,47,47,47,47,47,34,47,47,47,47,34,47,34,34,34,34,34,34,47,47,34,34,34,34,47,34,47,47,47,34,34,47,47,47,34,47,34,47,47,34,47,47,34,47,47,34,34,47,47,47,47,34,47,47,47,34,47,47,34,34,34,34,34,34,47,34,47,47,47,47,34,34,34,34,47,47,34,47,34,47,47,34,47,34,34,34,47,34,34,47,47,47,47,47,34,34,34,47,34,47,47,34,34,47,34,34,34,47,34,47,34,47,34,47,47,47,34,34,34,34,34,34,47,47,47,47,34,34,47,47,34,34,47,47,47,34,34,34,47,34,34,34,34,34,47,34,34,34,34,34,34,47,34,47,34,34,47,47,47,47,34,34,34,34,47,47,34,47,34,47,34,34,47,34,47,47,47,34,34,34,34,47,34,47,34,47,47,47,34,34,47,47,47,47,34,34,34,47,34,47,47,34,47,34,47,34,47,47,47,47,34,34,47,47,47,47,47,47,47,34,47,34,34,47,47,47,34,47,34,34,47,34,47,47,34,47,47,34,34,34,34,34,47,34,34,34,34,47,34,47,34,34,47,47,47,47,47,34,34,34,47,34,34,47,47,47,47,34,34,34,47,34,34,47,34,47,34,34,47,47,47,34,34,34,47,34,47,47,47,47,34,47,34,47,34,47,34,47,34,34,47,34,47,34,47,47,47,34,34,47,47,34,34,34,47,47,34,34,34,34,34,34,47,34,34,34,47,34,34,34,47,47,34,34,47,47,34,47,47,34,47,34,47,47,47,47,34,34,47,34,34,47,34,34,47,47,34,47,34,34,34,34,34,34,34,47,34,34,47,47,34,47,34,34,34,47,34,34,34,47,47,47,47,47,47,47,47,47,47,34,47,47,47,34,47,34,34,47,34,47,34,47,47,47,34,34,47,34,34,34,47,34,47,34,34,34,47,34,34,47,34,34,34,34,47,47,34,47,34,47,34,47,47,47,34,34,47,34,34,34,47,47,34,34,34,47,47,47,47,34,34,47,47,47,47,34,34,47,47,47,34,34,47,34,47,34,34,34,47,34,34,34,47,34,47,47,34,47,34,34,34,34,47,34,47,34,47,47,47,47,47,34,34,34,47,47,34,34,34,47,47,34,34,34,47,47,47,47,47,34,34,47,47,34,34,47,34,47,47,47,47,47,34,34,47,47,34,34,47,34,34,47,34,34,47,47,47,47,34,34,47,34,34,34,34,34,47,34,47,47,47,47,47,47,34,34,47,34,34,34,47,47,34,47,34,34,34,34,47,34,47,47,34,34,34,34,34,34,47,47,47,47,34,34,47,34,47,34,47,47,34,34,34,34,34,47,34,47,34,34,47,34,47,47,47,34,34,34,34,47,34,47,34,47,47,34,34,47,34,34,34,34,34,47,47,34,47,47,34,47,47,34,34,47,47,47,47,34,47,47,34,34,34,34,34,34,47,34,47,34,47,34,47,34,47,34,47,34,34,47,47,47,47,34,47,34,47,34,34,34,34,47,47,34,34,47,34,34,47,47,34,34,47,47,34,34,34,34,47,47,47,34,47,47,34,47,34,47,47,47,34,47,47,34,47,34,34,34,34,34,34,34,34,47,47,34,34,34,34,47,34,47,47,47,47,47,34,47,47,47,34,47,47,47,47,47,34,47,34,34,47,47,34,47,34,34,34,47,47,34,34,47,47,47,47,34,47,34,47,47,34,34,34,47,47,47,47,34,34,34,47,47,34,34,34,47,34,47,47,47,34,47,34,34,47,34,47,47,34,34,34,34,47,47,47,34,34,34,34,47,47,34,47,47,47,34,34,34,47,47,34,47,34,47,34,47,34,47,47,47,34,34,34,34,34,47,34,47,47,47,47,34,47,34,34,47,34,34,34,47,34,47,34,34,47,47,47,47,34,34,47,34,47,34,34,34,34,34,34,34,47,47,47,34,47,47,34,47,47,34,34,34,34,47,34,47,47,34,34,47,34,47,34,34,34,47,34,47,34,34,34,47,34,34,47,34,47,34,47,34,47,47,34,34,34,34,47,47,34,34,34,34,34,34,34,47,47,34,34,47,47,47,47,34,34,47,34,34,47,34,47,34,34,47,47,47,34,34,47,34,34,34,47,47,47,34,34,47,34,34,34,47,34,34,34,47,34,34,47,34,34,47,34,47,34,34,34,34,47,34,34,34,34,47,34,47,47,47,34,34,34,34,34,47,47,47,47,34,34,47,47,34,47,47,34,34,34,47,34,47,34,47,47,34,34,34,47,47,47,34,47,34,47,34,47,47,47,34,34,47,34,34,47,34,34,47,34,47,34,47,34,34,47,34,34,34,47,34,34,34,47,34,34,47,34,47,34,47,34,34,34,34,47,34,34,47,47,47,47,47,47,34,47,47,34,47,34,34,34,47,34,34,47,47,47,34,34,34,47,34,47,47,47,47,47,47,47,34,34,47,34,47,34,34,47,34,34,47,47,34,34,47,47,47,34,34,34,47,47,34,47,47,34,34,34,47,34,47,47,47,47,47,47,47,47,34,47,34,34,47,47,34,34,34,34,47,34,47,47,34,47,34,47,47,47,34,34,47,34,47,47,47,47,34,34,47,34,34,47,47,34,47,47,47,47,34,47,47,47,47,47,47,47,34,34,47,47,47,34,47,47,34,34,47,47,34,47,34,47,47,47,34,47,47,47,47,47,34,47,47,47,47,34,47,34,34,47,34,47,34,34,34,34,34,34,34,34,34,47,47,34,47,34,47,47,47,34,34,47,34,47,34,47,47,47,47,47,34,34,34,34,34,34,47,47,47,34,34,34,47,47,34,34,47,47,34,47,34,34,47,34,34,34,47,47,34,34,34,47,47,34,47,34,47,47,34,47,34,34,34,34,47,47,47,34,47,47,47,47,47,47,47,47,47,34,47,34,47,34,47,47,34,34,34,34,34,47,47,47,34,34,47,34,47,34,47,34,34,47,34,47,47,47,34,47,34,47,34,34,34,34,47,34,47,47,34,34,34,34,47,34,47,47,47,34,47,47,34,34,47,34,34,34,47,47,47,34,47,47,34,34,34,47,34,47,34,47,47,47,34,34,47,34,34,47,34,34,34,47,34,47,47,47,47,47,47,34,34,34,47,47,47,34,47,47,47,34,47,34,34,34,34,47,47,47,47,34,34,34,34,34,47,47,34,47,34,34,47,34,34,47,34,47,47,34,47,34,34,47,34,34,34,47,47,34,47,34,34,47,47,47,34,47,34,47,47,34,34,47,47,47,47,47,47,47,34,34,47,34,34,47,47,47,47,47,47,47,34,47,47,47,34,34,47,34,47,47,34,34,34,34,47,47,34,34,34,34,34,34,34,34,34,34,47,34,47,47,34,34,34,47,47,47,34,34,34,34,47,34,47,47,34,47,47,47,34,34,34,34,34,47,34,47,47,34,34,34,47,34,34,47,47,47,47,47,34,34,47,47,34,47,34,34,47,34,47,34,47,34,47,47,34,34,34,34,34,47,34,34,34,47,47,47,34,34,47,47,47,47,34,34,34,34,47,47,47,34,34,34,47,47,34,47,34,47,34,47,47,47,47,34,34,47,47,34,34,47,34,47,47,34,47,34,47,47,47,47,34,34,47,47,34,34,47,34,47,34,34,34,47,47,47,47,34,34,47,47,47,34,47,34,34,47,47,34,34,34,47,34,34,47,47,34,47,47,34,34,47,34,47,34,47,34,47,34,47,47,34,47,47,34,47,34,34,34,34,47,47,47,34,47,47,47,47,47,34,47,34,34,47,34,47,34,34,34,34,47,47,47,47,34,47,34,34,34,34,34,47,47,34,34,47,47,34,34,34,34,47,34,34,47,47,34,47,34,47,34,34,47,47,47,47,34,47,34,34,34,34,34,34,34,34,47,47,34,47,34,47,47,47,34,47,34,47,47,34,34,34,47,34,47,34,34,34,34,47,47,34,34,34,47,34,34,34,34,34,47,34,47,47,47,47,34,34,47,47,34,34,47,47,34,47,47,47,34,34,47,34,47,34,47,34,34,47,47,47,47,34,34,34,47,34,47,34,34,47,47,47,34,47,47,47,47,47,47,34,47,47,47,47,47,34,47,34,47,34,34,34,34,47,34,47,34,34,47,34,34,34,34,47,47,47,47,47,47,47,47,34,47,34,34,47,34,47,34,47,47,47,34,47,34,47,34,34,47,47,47,47,47,47,34,34,34,47,47,47,47,34,34,47,34,34,34,34,47,34,34,34,34,34,47,47,47,47,47,47,47,47,47,47,34,47,47,34,47,47,47,34,34,34,47,47,47,47,47,34,47,47,47,47,34,34,34,47,34,34,47,47,34,47,34,34,47,47,47,34,47,47,47,34,34,34,34,34,47,47,47,47,34,47,34,47,47,34,34,34,34,34,47,34,47,34,47,34,34,47,47,47,47,47,34,34,47,47,47,34,47,34,34,47,47,47,47,34,34,34,34,34,34,47,47,34,34,34,34,34,34,47,47,34,47,47,34,34,47,34,47,34,47,34,47,47,34,34,47,47,34,47,34,47,34,47,34,34,34,34,34,34,47,47,34,34,34,47,47,34,34,34,34,47,34,34,34,47,47,34,47,34,34,34,47,47,47,34,47,34,34,47,34,34,47,47,47,47,47,34,34,34,34,47,34,47,34,47,34,34,47,34,47,34,47,34,34,47,47,47,47,34,47,47,47,47,47,47,47,34,47,47,34,47,47,47,34,47,47,47,34,34,47,47,34,47,34,47,47,34,47,47,47,47,34,47,47,47,34,34,47,47,47,34,34,34,34,47,34,47,34,47,34,47,47,34,47,47,34,34,34,47,34,34,34,47,34,34,34,47,34,47,47,34,34,34,47,34,47,47,34,34,47,34,34,47,47,34,34,34,34,47,34,47,34,47,47,34,47,34,34,47,47,47,34,47,47,34,34,47,47,47,34,34,47,34,47,47,47,47,47,34,47,47,34,47,47,47,47,47,47,47,34,34,47,47,47,47,34,34,47,47,47,47,34,47,47,34,34,34,47,34,34,34,34,34,47,34,47,34,34,47,34,47,47,34,34,34,47,34,47,34,47,34,47,34,47,34,47,47,47,34,47,47,34,34,34,34,47,34,34,47,47,34,47,34,34,47,47,34,47,47,34,34,47,34,34,34,47,34,47,47,47,34,47,34,47,47,34,47,34,47,34,47,47,47,34,47,47,47,47,47,34,34,47,47,34,34,34,47,47,47,34,47,34,47,34,47,47,47,34,47,34,47,34,47,34,34,47,47,34,34,47,47,47,34,34,34,47,34,47,34,34,34,47,34,34,47,34,47,47,34,34,34,34,47,47,47,47,47,47,34,47,34,34,47,47,47,34,47,47,47,34,34,34,34,34,47,47,47,47,34,34,47,47,47,47,47,34,34,47,34,47,47,47,34,34,34,34,47,47,34,47,34,47,34,34,34,47,34,47,47,47,34,34,34,47,47,34,34,34,34,47,47,47,47,47,34,34,47,47,34,34,34,34,47,47,47,34,34,34,34,34,34,34,34,47,34,47,34,34,34,47,47,34,34,47,34,47,47,34,34,47,47,47,34,47,34,47,34,34,34,47,47,47,47,47,34,34,34,47,47,47,34,34,34,47,34,34,47,34,34,47,47,34,34,34,34,34,47,47,47,34,47,47,47,34,34,47,34,47,34,34,34,47,34,47,47,34,47,47,47,47,47,47,47,47,47,47,34,34,47,47,47,47,34,47,47,34,47,34,34,47,47,34,47,47,34,47,34,34,34,34,47,47,34,47,34,47,34,47,47,34,47,34,47,34,47,34,47,47,34,47,47,47,47,47,47,34,47,47,34,34,34,34,47,34,47,47,47,34,34,47,34,47,34,34,47,34,34,34,34,34,34,34,47,47,47,47,47,34,34,47,47,47,47,34,34,47,34,34,34,47,47,34,47,47,34,34,47,47,34,47,34,47,34,47,47,47,47,34,34,34,47,34,47,34,34,47,47,34,47,34,34,34,34,47,47,47,34,47,47,47,47,47,47,47,34,34,34,34,34,34,34,34,47,34,34,47,34,47,34,47,34,34,47,47,47,34,47,47,34,47,47,34,47,34,34,47,34,47,34,34,47,34,34,34,34,34,47,47,47,47,47,47,47,34,34,47,47,47,34,47,47,34,47,34,34,34,47,34,34,47,34,47,47,34,47,47,47,47,47,34,34,47,34,34,34,34,47,47,47,47,34,34,34,34,34,34,47,34,34,34,47,34,47,47,34,34,34,47,34,34,34,47,34,47,34,47,34,47,47,34,47,47,34,47,47,47,47,34,34,47,47,47,34,34,47,34,34,34,47,34,34,34,47,47,34,47,47,34,34,34,34,47,47,47,47,47,47,34,34,34,47,34,34,34,34,34,47,34,34,47,34,34,34,47,47,34,47,47,47,47,34,34,47,34,34,47,47,34,47,34,34,47,34,47,34,47,34,47,34,34,34,34,34,34,47,34,34,47,47,34,34,34,47,34,34,34,34,47,34,34,47,47,47,47,34,34,34,47,34,47,34,34,47,47,34,47,47,34,47,47,34,34,34,34,47,47,47,34,34,47,47,47,34,34,47,47,34,47,34,34,34,47,47,47,34,34,34,34,34,34,47,34,47,34,34,34,34,47,47,47,34,47,47,34,47,34,47,47,34,34,47,47,47,34,47,47,34,34,34,34,34,47,34,47,34,47,47,34,34,47,47,34,47,47,34,47,47,34,47,47,47,34,47,34,47,34,34,47,47,47,34,47,34,47,47,47,47,47,47,47,34,34,34,47,47,47,34,47,47,34,47,34,47,47,47,34,47,47,34,47,47,47,47,47,34,34,47,47,34,47,47,34,47,34,34,47,34,34,34,34,34,47,34,34,47,34,34,47,34,47,47,47,34,34,34,47,34,47,34,34,47,47,34,34,34,34,34,34,34,34,47,34,47,47,34,47,34,47,34,34,34,47,34,47,34,47,47,34,47,47,47,47,47,34,34,34,47,34,34,34,47,34,47,47,34,34,34,34,34,34,34,47,47,47,34,34,47,34,34,47,47,47,47,34,47,34,47,34,47,34,47,47,47,47,47,47,47,47,47,47,47,34,47,34,34,34,47,34,34,47,47,47,34,34,47,34,34,34,34,34,47,34,47,47,34,34,34,47,47,47,47,47,47,34,47,34,34,47,47,34,47,47,34,47,34,34,34,34,34,47,34,34,47,34,34,34,34,47,34,34,34,34,47,34,47,34,34,47,47,47,47,47,34,47,34,47,34,34,34,47,34,47,47,47,34,47,34,34,47,34,34,47,47,47,34,34,34,47,34,47,47,47,34,47,47,34,34,34,34,34,34,34,34,34,47,34,47,34,34,34,34,47,47,34,47,34,34,34,47,47,47,47,47,34,34,34,47,34,47,47,47,47,34,47,34,34,34,34,47,47,34,47,34,47,47,47,34,34,34,34,34,47,47,47,47,34,34,34,47,47,47,34,47,47,47,34,47,34,34,47,47,47,34,47,34,34,34,47,34,34,47,47,47,34,34,47,34,34,34,47,47,34,34,34,47,34,47,34,34,47,34,34,34,47,47,47,34,34,34,47,47,34,47,47,34,47,34,47,47,47,34,47,47,34,34,34,47,34,34,34,34,34,34,47,47,34,34,47,34,34,34,34,34,47,34,47,34,47,34,34,47,34,47,47,34,47,34,34,47,34,34,47,47,47,34,47,34,47,47,47,47,34,34,47,47,34,34,34,34,34,47,34,47,34,34,34,47,47,34,34,47,47,34,47,34,47,34,34,47,34,34,47,34,47,34,47,34,47,47,47,34,34,34,34,34,34,47,47,34,34,34,34,34,34,34,34,34,47,34,47,47,34,47,34,47,34,34,47,47,47,34,34,47,34,47,47,34,47,34,34,34,47,34,34,34,47,47,34,34,47,34,34,34,47,34,47,34,34,34,47,47,34,34,47,34,34,34,47,47,34,34,47,34,34,47,34,47,34,47,47,34,47,47,34,34,34,47,34,47,47,47,47,47,47,34,47,34,47,34,34,34,47,47,34,34,47,34,34,47,34,34,47,34,34,34,34,47,34,34,34,34,34,47,47,47,34,47,47,47,34,34,34,34,47,34,34,47,47,34,34,34,47,34,47,47,34,47,47,34,47,34,34,34,47,34,47,47,34,47,34,34,47,47,34,34,47,34,47,47,47,47,34,47,47,34,34,47,47,47,47,47,47,47,47,47,47,47,34,47,34,47,47,47,47,47,34,47,47,34,34,34,34,34,47,34,47,47,34,34,47,34,47,34,34,47,47,34,47,47,47,47,34,47,34,47,34,34,47,47,34,34,34,34,47,47,47,47,34,34,34,47,34,34,47,47,34,47,34,47,34,47,47,34,47,47,47,34,47,34,47,34,34,47,47,47,34,47,47,47,47,47,34,47,47,47,34,34,47,47,47,47,34,34,47,34,34,47,47,34,34,47,34,47,47,34,34,47,34,47,47,47,34,34,47,47,47,34,34,47,34,34,34,47,47,47,47,47,47,34,34,47,34,34,34,34,47,34,34,47,34,47,47,34,47,34,47,47,34,47,47,34,34,47,34,47,34,47,34,47,47,34,47,47,34,47,34,47,34,47,34,34,34,47,47,47,34,34,47,34,34,47,47,47,47,47,47,47,34,34,47,34,34,34,47,34,34,34,47,34,47,34,34,34,47,34,47,47,47,47,34,47,47,34,47,47,47,34,47,34,34,34,47,34,34,34,34,34,47,34,47,47,34,47,47,47,47,34,47,47,47,47,34,47,47,47,47,34,47,47,47,47,47,34,34,34,47,34,34,47,34,47,47,34,47,47,34,34,47,34,34,47,34,47,47,34,34,34,47,47,47,47,34,34,34,47,34,47,47,34,34,47,34,34,47,34,47,47,34,47,47,34,34,34,47,47,47,34,34,47,34,47,47,34,34,47,47,34,47,47,47,47,47,47,47,34,47,47,47,34,34,34,34,47,47,34,47,34,34,47,34,34,34,47,34,34,34,47,34,34,34,47,34,34,34,47,47,34,47,47,34,47,34,47,47,34,34,34,47,34,47,34,47,47,47,34,47,47,47,47,47,34,47,34,47,47,34,34,34,47,34,34,47,47,34,34,34,34,47,47,47,47,47,34,34,47,47,34,47,34,34,34,47,34,34,34,47,34,34,34,34,34,47,47,47,34,47,34,34,34,47,34,34,47,34,47,34,47,34,47,47,34,34,47,34,47,34,34,47,47,34,47,47,34,34,47,47,34,34,34,47,34,34,47,34,47,34,34,47,47,34,34,47,47,47,34,47,47,47,47,47,34,47,34,34,47,34,34,47,47,34,47,34,34,47,34,34,47,47,34,47,34,47,34,47,47,47,47,34,34,47,47,34,47,34,47,34,34,47,34,47,47,47,47,34,34,47,47,47,47,34,47,47,47,47,34,34,47,34,47,47,47,34,34,34,34,34,34,47,47,47,34,34,47,47,47,34,34,34,34,47,34,47,34,47,34,34,34,34,47,47,47,34,47,34,47,34,34,47,47,34,34,47,47,47,34,34,34,34,47,47,47,34,34,47,47,47,47,47,47,34,34,47,47,47,47,34,34,47,34,34,34,34,34,34,47,47,47,47,34,47,34,47,34,34,47,47,47,34,34,47,47,47,34,47,34,47,34,34,47,34,34,34,34,34,34,34,34,34,34,34,47,47,47,34,34,34,47,47,34,34,34,47,47,47,34,47,34,34,34,34,34,34,34,47,34,34,47,47,47,47,34,47,34,34,47,34,34,47,34,34,47,47,47,47,47,47,47,34,34,34,34,47,34,34,34,34,47,34,47,47,34,47,34,34,47,34,47,34,47,47,47,34,34,47,47,47,47,47,47,34,47,34,34,47,34,34,47,47,47,47,47,47,34,47,34,34,34,34,47,47,34,34,47,34,34,47,47,47,34,34,47,34,34,34,34,34,47,34,47,34,47,34,34,34,47,34,34,34,34,47,47,47,47,47,34,34,47,34,34,47,34,34,34,34,47,34,34,47,47,47,47,47,34,34,47,47,34,47,34,34,34,34,47,34,34,47,47,47,47,47,34,34,34,47,34,34,34,34,34,47,47,47,34,47,34,47,34,47,47,47,34,47,47,47,47,47,34,34,34,47,34,47,34,47,47,47,34,47,34,34,47,34,34,34,47,47,47,47,34,34,47,34,47,34,47,34,34,34,34,34,34,47,47,34,34,47,34,34,47,34,34,47,34,34,47,47,47,34,34,34,47,47,47,47,34,47,47,47,34,47,34,47,47,47,34,47,34,34,47,34,47,47,47,47,34,47,47,34,47,34,47,47,47,34,47,47,47,47,47,34,47,47,34,34,47,34,47,34,34,34,47,47,34,47,34,47,34,34,34,47,47,47,34,47,34,34,47,34,34,34,47,47,47,47,47,47,47,34,47,34,34,47,34,34,47,47,34,47,34,34,34,34,47,34,47,34,47,47,47,47,47,34,47,47,47,34,34,47,47,34,34,47,47,47,34,47,47,34,34,34,47,47,47,34,34,34,47,34,47,47,34,47,47,47,34,47,47,34,47,47,34,47,47,34,34,34,47,47,47,34,47,34,34,47,34,47,34,47,47,34,47,47,47,47,47,34,47,34,47,47,34,34,34,47,47,34,34,47,47,47,47,47,34,34,34,47,47,34,47,47,47,34,34,34,34,47,47,34,34,47,47,47,47,47,34,34,34,47,47,34,47,47,47,34,34,47,34,34,47,34,47,34,47,34,34,47,34,47,47,34,34,47,34,34,34,34,47,34,34,47,47,47,47,47,47,47,34,34,34,34,34,34,34,34,47,47,34,34,47,47,47,47,34,47,47,47,34,34,47,47,34,34,34,34,47,34,34,47,47,34,34,47,47,34,34,34,34,34,34,47,47,34,47,47,34,34,47,34,34,34,34,47,34,34,34,34,34,34,47,47,47,47,34,47,34,34,34,34,47,47,34,34,47,47,47,47,47,34,34,47,47,47,47,47,47,47,47,47,34,34,47,34,47,47,34,47,47,47,34,34,47,47,34,34,47,47,47,34,34,47,34,34,34,34,34,34,47,47,47,47,34,47,47,34,34,47,34,47,34,34,34,47,34,34,47,34,34,34,34,34,47,34,34,47,47,34,34,34,47,47,34,47,47,47,47,47,34,47,34,47,34,34,34,34,47,34,47,34,34,47,47,34,34,47,34,34,34,34,47,47,34,47,34,34,34,34,47,47,47,47,47,47,34,34,47,47,34,34,34,34,34,34,47,34,47,47,34,47,34,47,34,34,34,47,34,34,34,34,34,34,47,47,34,34,47,34,34,47,47,34,34,47,34,34,47,47,34,34,34,34,34,47,34,47,47,47,47,47,34,47,47,34,47,47,34,47,47,34,34,47,34,47,47,47,47,34,47,34,47,34,47,34,47,47,34,47,47,47,47,47,34,34,34,47,47,34,47,47,47,47,34,34,47,47,34,47,34,47,34,34,34,47,34,47,47,34,47,47,34,34,34,47,47,34,34,34,47,47,34,47,47,34,34,34,34,34,47,34,47,34,47,47,34,34,47,34,47,34,34,34,34,47,47,34,47,34,47,34,34,47,34,47,34,34,34,47,47,47,47,34,34,47,47,47,47,34,34,47,47,34,34,47,34,34,47,34,47,47,34,47,34,34,47,47,47,34,47,47,47,47,34,47,34,34,34,34,34,34,34,34,47,34,34,34,34,47,47,47,47,34,47,34,34,34,47,34,34,34,47,34,47,34,34,34,34,47,34,34,34,47,34,47,47,47,34,34,47,47,47,47,47,34,47,47,47,47,34,34,47,34,34,47,34,47,34,47,34,34,47,47,47,34,47,47,34,34,34,47,34,34,47,47,47,34,47,34,34,47,47,47,47,34,34,47,34,47,34,47,34,47,34,34,47,47,47,34,34,34,34,47,34,47,47,47,47,47,34,47,47,47,34,34,47,47,34,47,34,34,34,34,47,34,34,47,34,47,34,47,47,34,34,47,47,34,34,47,34,47,47,34,47,47,34,34,34,34,47,34,47,47,47,34,47,34,34,34,34,34,47,47,34,47,47,47,34,34,47,34,47,34,34,47,34,34,47,47,47,34,47,34,34,34,47,34,34,34,47,47,47,34,34,34,47,47,47,34,34,34,34,34,34,47,34,47,34,34,47,34,34,47,34,47,47,34,47,47,34,47,34,34,47,34,34,34,47,34,47,47,47,34,47,34,47,47,34,47,34,34,47,47,34,34,47,47,47,34,47,47,47,34,34,47,47,34,34,47,34,47,34,34,34,34,47,47,34,47,47,47,47,34,34,47,34,34,34,47,47,34,34,34,47,34,47,34,34,34,47,47,47,47,34,34,47,47,34,47,47,47,47,34,34,47,47,47,34,47,47,47,47,47,47,34,34,47,47,34,34,34,34,47,47,47,34,34,47,47,47,47,47,34,47,34,47,47,34,34,34,47,34,34,34,34,47,47,34,47,47,34,34,47,34,34,47,34,34,34,47,47,34,34,47,34,34,47,47,47,34,34,47,34,47,34,34,34,47,34,47,47,34,34,34,34,34,47,34,47,47,47,47,47,34,34,34,34,47,34,47,34,47,47,34,34,34,47,47,47,47,47,47,34,47,47,47,47,47,34,47,34,34,34,34,47,34,34,34,34,47,47,34,47,34,47,34,47,47,34,34,34,47,34,47,47,47,34,47,34,47,47,34,47,34,47,47,34,47,47,47,47,34,47,34,47,47,47,34,34,47,47,34,47,34,34,34,34,47,34,47,34,47,34,34,34,34,34,47,34,47,47,34,34,34,47,34,34,34,47,47,47,47,34,34,47,34,34,47,47,47,34,47,34,34,47,47,47,34,34,34,34,34,34,47,34,34,34,47,47,47,34,34,34,34,47,47,47,34,34,47,47,47,47,47,34,47,34,34,34,47,34,34,47,47,34,34,47,34,34,47,47,47,34,47,34,47,34,47,47,47,34,47,47,47,34,47,34,47,47,34,47,34,34,47,34,47,34,34,47,47,47,34,47,34,34,47,47,47,47,47,34,47,47,47,34,34,34,34,47,34,47,34,34,34,34,34,34,34,47,47,47,47,34,47,47,47,47,47,34,34,34,47,47,47,47,47,34,34,47,47,34,34,47,47,34,34,47,34,34,34,34,34,47,47,34,34,47,34,34,34,47,47,47,47,47,34,34,34,47,34,34,47,34,47,47,47,47,47,47,34,34,47,47,47,34,34,47,47,47,34,47,34,34,34,47,47,47,47,47,47,47,34,47,34,34,34,34,47,47,34,47,47,34,47,47,34,34,47,47,34,47,47,47,34,34,34,34,34,34,34,34,34,34,47,34,47,34,47,34,34,34,34,47,34,34,34,34,34,34,47,34,47,34,34,34,47,47,34,47,47,34,34,47,34,47,34,47,34,34,47,47,47,34,47,34,47,34,47,47,34,47,34,47,47,34,34,34,34,47,34,47,34,34,34,34,34,34,34,47,47,34,47,34,47,47,34,47,34,34,34,47,47,34,34,47,34,47,47,34,47,34,47,47,34,34,47,47,34,34,34,47,34,34,34,47,47,34,34,47,47,34,47,34,47,34,47,47,34,34,47,34,47,34,47,47,34,47,47,34,47,47,34,34,47,34,34,34,34,47,47,47,34,34,34,47,34,47,47,34,34,34,34,47,34,34,47,47,47,47,47,34,34,34,47,34,47,34,47,34,34,34,34,47,47,47,47,47,34,47,47,34,34,34,47,34,47,34,47,34,47,34,47,34,34,34,47,47,47,34,34,34,47,34,34,34,47,47,47,34,47,34,47,34,34,47,34,47,34,34,34,34,34,47,47,47,47,34,34,34,34,47,34,47,47,34,47,34,34,47,47,47,34,34,47,47,34,47,34,34,34,34,34,34,34,47,47,34,34,47,34,34,34,47,47,47,34,34,34,47,47,34,34,47,34,47,47,34,47,47,47,47,34,34,47,47,47,47,34,34,47,34,47,47,47,47,34,34,34,47,47,34,34,47,34,47,34,47,34,47,47,47,34,47,47,34,47,34,34,34,34,47,34,34,47,34,34,47,47,34,47,34,34,47,47,47,47,34,47,47,34,34,34,34,47,34,34,34,34,47,47,34,34,47,47,34,34,34,47,47,34,34,47,34,47,47,47,47,47,34,34,47,34,47,34,47,47,47,47,47,47,47,34,47,34,47,47,47,47,47,47,47,47,34,34,34,47,47,34,47,34,47,34,34,47,47,47,47,47,34,47,34,47,34,34,47,47,47,47,34,34,34,34,47,34,34,34,34,47,34,47,34,34,47,34,34,47,47,34,34,47,47,47,47,47,34,34,47,34,34,34,34,47,47,34,47,47,47,47,47,47,34,47,47,47,47,47,47,47,47,47,47,34,47,47,34,34,47,47,47,34,47,34,34,34,34,34,34,47,47,47,34,34,34,47,34,34,34,34,47,47,34,34,47,47,47,47,34,47,34,47,47,47,47,47,34,34,34,47,34,34,47,47,34,47,34,34,47,34,47,47,47,34,34,47,34,34,47,34,34,47,47,47,47,47,47,47,47,47,34,47,34,34,34,47,47,34,34,47,34,47,34,34,34,47,47,47,34,47,47,34,34,47,47,34,34,34,47,47,47,47,34,47,47,47,34,34,47,47,34,34,47,47,47,47,47,47,34,34,34,47,34,34,34,47,34,47,47,34,34,47,47,34,47,34,47,47,47,34,34,47,47,34,34,34,34,47,47,47,47,34,34,34,34,34,47,34,34,47,34,47,34,34,34,47,47,47,34,47,34,34,34,47,34,34,47,47,47,47,47,47,34,47,47,34,47,47,34,47,47,34,47,47,47,34,34,47,47,34,34,34,34,34,34,47,34,34,47,34,34,34,34,47,47,47,34,34,47,34,34,34,34,47,34,34,34,47,34,47,47,34,47,34,34,34,47,34,34,34,47,34,47,34,34,47,34,47,47,34,47,47,34,34,34,34,34,34,47,47,47,47,47,34,47,34,34,47,47,34,47,47,34,47,47,47,34,34,47,47,47,34,34,47,34,47,47,47,34,34,34,47,47,47,47,47,47,34,47,47,47,47,47,34,34,34,47,34,34,47,47,47,47,34,47,34,34,34,47,47,34,34,47,47,47,47,47,47,34,47,34,47,47,34,34,47,34,34,34,47,34,47,47,47,34,47,47,34,47,34,34,47,34,34,47,47,47,47,47,34,34,34,47,34,34,34,47,34,47,47,47,47,47,34,47,34,47,47,47,47,34,47,34,47,47,47,47,47,47,47,34,34,34,34,34,47,34,34,47,34,47,34,34,47,47,47,47,47,47,47,34,47,47,47,47,34,34,47,47,34,34,34,47,47,34,34,34,47,34,47,34,34,34,34,47,34,47,47,34,47,47,47,47,47,47,47,47,47,34,47,47,34,47,47,47,47,47,34,47,34,34,34,47,34,34,47,47,47,34,47,34,34,34,47,47,34,34,34,47,47,34,34,47,34,34,47,34,34,34,47,34,34,34,34,34,47,47,47,34,47,47,34,47,47,34,34,47,34,34,34,47,34,34,47,34,34,47,34,34,34,34,34,34,34,34,47,47,47,47,34,34,34,34,47,34,47,47,47,47,47,34,34,34,34,47,47,47,34,47,34,34,47,47,47,47,34,47,34,47,47,47,34,34,34,47,34,47,47,34,34,34,34,34,47,47,34,34,47,47,47,47,34,47,47,34,47,47,34,47,34,34,34,47,34,34,47,34,34,47,34,47,47,34,47,34,47,34,34,34,34,47,34,47,34,34,34,47,47,47,47,47,47,47,34,34,47,34,34,34,47,47,47,34,47,34,34,47,34,47,47,47,47,34,47,47,47,34,34,47,47,47,34,34,47,34,47,34,34,47,34,34,47,34,34,34,47,47,47,34,34,34,47,34,47,34,47,34,34,47,34,34,47,34,47,47,47,34,34,34,47,47,34,47,34,47,34,47,34,34,34,47,47,47,47,34,47,47,34,47,34,34,34,34,34,34,34,34,47,47,34,34,34,34,34,47,34,34,47,47,34,47,34,34,47,47,34,47,34,34,34,34,34,34,47,47,34,34,34,47,47,47,47,47,47,47,34,34,34,47,34,34,47,47,47,47,34,47,47,34,34,47,47,34,47,47,34,34,47,47,47,47,47,34,34,34,34,47,34,47,34,34,47,34,47,47,47,34,34,47,47,47,47,34,47,34,34,47,34,34,47,34,47,47,34,47,34,47,47,47,47,47,47,47,34,34,34,34,34,34,34,34,34,47,34,47,47,47,47,47,47,47,47,34,47,47,47,47,47,47,34,47,47,47,47,34,34,34,47,47,34,47,47,47,47,47,47,34,47,34,34,34,34,34,34,34,47,34,34,47,34,47,47,34,47,34,34,34,47,34,34,34,34,34,47,47,34,34,34,47,47,47,47,47,34,47,47,34,47,34,47,47,47,34,47,34,34,47,47,47,34,47,47,47,47,47,34,47,34,34,47,34,34,47,34,34,47,34,34,47,47,34,34,47,47,47,34,47,47,47,34,47,34,34,47,47,34,34,34,47,34,34,34,34,47,34,34,47,34,34,47,34,47,47,34,47,47,34,34,47,34,34,34,47,34,47,34,34,34,34,34,47,34,34,47,34,34,34,47,34,47,34,47,47,34,34,34,34,34,47,34,47,34,34,47,47,47,34,47,34,34,47,47,47,34,34,34,34,34,34,47,47,34,47,47,47,34,34,34,34,34,34,47,47,47,47,34,34,47,47,47,47,34,34,34,34,34,47,34,47,34,34,47,47,47,47,47,34,34,34,34,47,34,34,34,34,34,34,47,34,47,34,34,47,47,34,34,47,34,47,34,34,34,47,47,34,34,47,47,47,47,34,34,34,47,34,47,47,34,47,34,34,47,34,47,47,34,47,34,34,47,47,47,47,34,47,47,47,34,47,34,34,47,34,34,47,34,47,47,47,34,34,47,34,47,34,34,34,34,47,47,34,34,34,47,34,47,34,47,34,34,34,47,34,34,47,34,34,34,47,34,34,34,47,34,47,47,47,34,47,34,34,47,47,34,47,47,47,47,47,47,47,47,34,34,47,34,34,34,34,34,47,47,47,34,34,34,47,47,34,47,34,34,34,47,47,47,47,34,34,34,34,47,47,47,34,47,34,34,47,47,47,34,47,47,34,34,47,47,34,47,47,47,34,47,47,47,34,47,34,47,47,34,34,34,47,34,47,47,47,34,47,47,47,47,34,34,34,47,34,34,47,47,34,34,34,34,34,47,34,34,47,47,34,34,47,34,34,34,34,47,47,47,47,47,47,34,34,34,34,47,34,34,34,47,47,34,34,47,47,47,47,47,47,47,34,47,47,47,47,34,34,34,34,34,34,34,34,47,34,34,34,47,47,34,34,47,34,34,34,34,47,47,47,47,47,47,34,34,47,47,34,47,47,34,47,47,34,47,34,47,34,47,47,34,47,34,34,47,34,47,34,34,34,47,47,34,34,34,47,34,47,34,34,34,47,34,47,34,47,34,47,47,34,34,47,47,47,34,47,47,47,34,34,47,34,47,47,47,47,34,47,34,47,34,34,47,34,34,47,47,47,47,47,34,47,47,47,47,47,34,47,34,47,34,34,34,47,47,47,34,47,34,34,34,47,47,47,34,47,47,34,34,34,34,34,47,47,47,47,47,47,34,47,34,47,34,34,34,34,47,47,47,47,47,34,34,47,34,47,34,34,34,34]
temperatures = [73,74,75,71,69,72,76,73]

def dailyTemperatures(temperatures):
	for i in range(0,len(temperatures) - 1):
		if temperatures[i] < temperatures[i+1]:
			temperatures[i] = 1
	print(temperatures)



dailyTemperatures(temperatures)



# # Brute Force --> too slow
# def dailyTemperatures(temperatures):
# 	solution = []
# 	big_present = False
# 	for i in range(0,len(temperatures)):
# 		count = 0
# 		for j in range(i+1, len(temperatures)):
# 			if temperatures[j] > temperatures[i]:
# 				big_present = True
# 				count+=1
# 				break
# 			else: 
# 				count+=1
# 			big_present = False
# 		if big_present == True: 
# 			solution.append(count)
# 		else: 
# 			solution.append(0)
# 	return solution
# print(dailyTemperatures(temperatures))