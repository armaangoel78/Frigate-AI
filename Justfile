redis: 
    ! redis-server && echo "Redis already running!"

orch-py:
    python3 app.py

orch-c:
    gcc orch-c/main.c -o orch-c/main

orch-pp:
    g++ -std=c++17 -o orch-pp/main orch-pp/main.cpp /usr/local/lib/libredis++.a /usr/local/lib/libhiredis.a -pthread
    