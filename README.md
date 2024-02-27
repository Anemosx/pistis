# Pistis - System Test Suite

![pistis_banner](pistis_banner.png)

This repository contains a suite of scripts designed to gather and display system information and performance statistics across various components, including CPU, disk, GPU and memory. It leverages popular Python libraries such as psutil, py-cpuinfo, GPUtil, torch and PyCUDA to extract detailed information and present it in a user-friendly format.

## Installation

This project uses Poetry for dependency management and packaging. To set up the environment and install the necessary dependencies, follow these steps:

### Prerequisites

Ensure you have Poetry installed. If you don't have Poetry installed, you can install it with the following command:
```
curl -sSL https://install.python-poetry.org | python3 -
```

For detailed instructions, refer to the [Poetry documentation](https://python-poetry.org/docs/).

### Setting Up the Project

1. Clone the repository:
```
git clone https://github.com/Anemosx/pistis.git
cd pistis
```

2. Install the dependencies using Poetry:

```
poetry install
```

This command will create a virtual environment and install the dependencies specified in `pyproject.toml`.


## Components

The test suite is divided into the following components, each responsible for a specific aspect of the system:

- CPU Tests: Utilizes psutil, platform and py-cpuinfo to display detailed CPU information, including architecture, core counts and frequencies.
- Disk Tests: Employs psutil to show disk usage statistics for all mounted partitions, detailing total size, used space, free space and usage percentage.
- GPU Tests: Uses torch, GPUtil and PyCUDA to provide GPU-related information, including CUDA version, device details and memory usage statistics.
- Memory Tests: Leverages psutil to fetch and display the system's virtual memory statistics, such as total available RAM.

## Usage

To run the tests, execute the main script, which will sequentially perform and display results for each system component. The output provides a comprehensive overview of the system's hardware and its current state.

`python main.py`

## Contributing

Contributions to enhance the test suite or extend its capabilities are welcome. Please ensure to follow the existing code structure and document any changes.
