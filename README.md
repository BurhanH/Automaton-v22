# Automaton-v22
Performance/load testing based on [locust](https://locust.io/) 

[![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/BurhanH/automaton-v22/blob/master/LICENSE)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/aeacfa13d0854b5a8e24a6feb46e9461)](https://app.codacy.com/gh/BurhanH/Automaton-v22?utm_source=github.com&utm_medium=referral&utm_content=BurhanH/Automaton-v22&utm_campaign=Badge_Grade)

## Requirements
Python 3.8.\*, locust 2.5.1, <br>
Virtualenv (virtual environment manager), <br>
Docker and PowerShell (optional) <br>

## Project structure
```text
-- automaton-v22
   |-- .gitignore
   |-- LICENSE
   |-- README.md
   |-- requirements.txt
   `-- locust-files
       |-- test.py
   |-- DockerFile
   |-- docker-compose.yml
   |-- run-perf-tests.sh
   |-- run-perf-tests.ps1
   `-- screenshots
       |-- test-code.png
       |-- charts.png
       |-- statistics.png
       |-- statistics-2.png
       |-- workers.png
```

## How to prepare environment
1. Install [Python](https://www.python.org/downloads/)
2. Install and configure [virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
3. Clone or copy (download) the repository into your virtual environment
4. Activate virtual environment, move to `automaton-v22` folder, and execute command `pip install -r requirements.txt`

## How to run performance tests
1. Open a terminal window
2. Move to virtual environment folder
3. Activate virtual environment
4. Move to `automaton-v22` folder
5. Execute `locust -f locust-files/test.py`
6. Go to browser and open [localhost:8089](http://localhost:8089)
7. Enter necessary info
8. And hit button Start Swarming
9. Then observe results in realtime
10. When testing is done, click Stop button
11. Collect results and statistics
12. Shutdown locust via `Ctrl+C` combination in the terminal window

Warning! My test project is not for `real` load testing.
Please use other resources to perform load testing.

## How to use a swarm of machines (Docker)
1. Execute command `docker-compose up --build -d` (creates an image)
2. Create an infrastructure `docker-compose up --scale worker=2` (creates and ups 1 master node and 2 worker instances) <br>
   Note! Approximately 1 processor core for 1 worker, depends on your goals.
3. Repeat steps 6-12 from the previous section
4. Execute command `docker-compose down` (will shutdown the infrastructure)

## How to use a swarm of machines (shell script for Mac and Linux)
1. Execute command `./run-perf-tests.sh` or `./run-perf-tests.sh 2` in a terminal window <br>
2. Go to browser and open [localhost:8089](http://localhost:8089)
3. Enter necessary info
4. And hit button Start Swarming
5. Then observe results in realtime
6. When testing is done, click Stop button
7. Collect results and statistics
8. Shutdown script via `Ctrl+C` combination in the terminal window

## How to use a swarm of machines (PowerShell script for Windows)
1. Execute command `.\run-perf-tests.ps1` or `.\run-perf-tests.ps1 5` in a terminal window <br>
2. Go to browser and open [localhost:8089](http://localhost:8089)
3. Enter necessary info
4. And hit button Start Swarming
5. Then observe results in realtime
6. When testing is done, click Stop button
7. Collect results and statistics
8. Shutdown script via `Ctrl+C` combination in the terminal window

## How it looks like
![alt text](/screenshots/test-code.png "Test code") <br>
![alt text](/screenshots/statistics.png "Statistics") <br>
![alt text](/screenshots/charts.png "Charts") <br>
![alt text](/screenshots/statistics-2.png "Statistics 2") <br>
![alt text](/screenshots/workers.png "Workers") <br>

## Technology stack and helpful info
[Python 3.8](https://docs.python.org/3.8/) <br>
[VirtualEnv](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/) <br>
[GitHub, cloning repository](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository) <br>
[Locust](https://locust.io/) <br>
[Docker](https://www.docker.com/) <br>
[Docker Compose](https://docs.docker.com/compose/) <br>
[PowerShell](https://github.com/PowerShell/PowerShell) <br>
