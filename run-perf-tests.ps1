# To use this PowerShell script please install the latest version from https://github.com/PowerShell/PowerShell

# How to use:
# .\run-perf-tests.ps1 - will create an infrastructure with 1 master node and 1 worker node
# .\run-perf-tests.ps1 3 - will create an infrastructure with 1 master node and 3 worker nodes

if ($args[0]) {
    $workers=$args[0]
} else {
    $workers=1
}

docker-compose build
docker-compose up --scale worker=$workers
docker-compose down